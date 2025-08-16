import express from "express";
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import { sendConfirmationEmail } from "../utils/mailer.js";
import User from "../models/User.js";

const router = express.Router();

// Registro
router.post("/register", async (req, res) => {
    try {
        const { email, password } = req.body;

        const userExist = await User.findOne({ where: { email } });
        if (userExist) return res.status(400).json({ msg: "Usuario ya existe" });

        const hashedPass = await bcrypt.hash(password, 10);

        const newUser = await User.create({
            email,
            password: hashedPass,
            verified: false
        });

        // Generar token de verificación
        const token = jwt.sign({ email }, process.env.JWT_SECRET, { expiresIn: "1h" });
        await sendConfirmationEmail(email, token);

        res.json({ msg: "Usuario registrado, revisa tu correo para confirmar." });
    } catch (err) {
        console.error(err);
        res.status(500).json({ msg: "Error en registro" });
    }
});

// Confirmar correo
router.get("/verify/:token", async (req, res) => {
    try {
        const { token } = req.params;
        const decoded = jwt.verify(token, process.env.JWT_SECRET);

        const user = await User.findOne({ where: { email: decoded.email } });
        if (!user) return res.status(400).json({ msg: "Usuario no encontrado" });

        user.verified = true;
        await user.save();

        res.json({ msg: "Cuenta verificada, ya puedes iniciar sesión" });
    } catch (err) {
        res.status(400).json({ msg: "Token inválido o expirado" });
    }
});

// Login
router.post("/login", async (req, res) => {
    try {
        const { email, password } = req.body;

        const user = await User.findOne({ where: { email } });
        if (!user) return res.status(400).json({ msg: "Usuario no existe" });

        if (!user.verified) return res.status(400).json({ msg: "Debes verificar tu correo" });

        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) return res.status(400).json({ msg: "Contraseña incorrecta" });

        const token = jwt.sign({ email }, process.env.JWT_SECRET, { expiresIn: process.env.JWT_EXPIRES });

        res.cookie("token", token, {
            httpOnly: true,
            secure: true, // ⚠️ activa HTTPS en producción
            sameSite: "strict"
        });

        res.json({ msg: "Login exitoso" });
    } catch (err) {
        res.status(500).json({ msg: "Error en login" });
    }
});

// Logout
router.post("/logout", (req, res) => {
    res.clearCookie("token");
    res.json({ msg: "Sesión cerrada" });
});

export default router;
