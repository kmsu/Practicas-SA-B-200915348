import express from "express";
import cookieParser from "cookie-parser";
import cors from "cors";
import dotenv from "dotenv";
import authRoutes from "./routes/auth.js";
import sequelize from "./config/db.js";
import User from "./models/User.js";

dotenv.config();
const app = express();

app.use(express.json());
app.use(cookieParser());
app.use(cors({
    origin: "http://localhost:3000", // frontend
    credentials: true
}));

// Rutas
app.use("/api/auth", authRoutes);

const PORT = process.env.PORT || 4000;

// Sincronizar DB y arrancar servidor
sequelize.sync({ alter: true })
  .then(() => {
    console.log("✅ Base de datos sincronizada");
    app.listen(PORT, () => {
      console.log(`🚀 Servidor corriendo en http://localhost:${PORT}`);
    });
  })
  .catch(err => console.error("❌ Error DB:", err));
