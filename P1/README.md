|              |                |
|    :---      |      ---:      |
| Nombre: Kevin Martin Samayoa Urizar | Curso: Software Avanzado |
| Carnet: 200915348                   | Fecha: 07/08/2024        |

# Principios SOLID

Los principios SOLID son un conjunto de reglas y buenas prácticas de diseño de software creados para hacer el código más mantenible, escalable y fácil de entender. Estos principios fueron formulados por Robert C. Martin y son ampliamente utilizados en la programación orientada a objetos.

## 1. Principio de Responsabilidad Única (SRP - Single Responsibility Principle)

Una clase, componente o microservicio debe hacer una cosa y, por lo tanto, debe tener una sola razón para cambiar. Si por el contrario, una clase tiene varias responsabilidades, esto implica que el cambio en una responsabilidad provocará la modificación en otra responsabilidad.

```javascript
class Producto {
    constructor(nombre, precio, cantidad) {
        this.nombre = nombre;
        this.precio = precio;
        this.cantidad = cantidad;
    }
}

class Inventario {
    constructor() {
        this.productos = [];
    }
    
    agregarProducto(producto) {
        this.productos.push(producto);
    }
}
```

Para este ejemplo la clase `producto` tiene la unica responsabilidad de almacenar la información del producto, mientras que `inventario` se ocupa de la gestión de productos y representa el conjunto de productos.

---

## 2. Principio de Abierto/Cerrado (OCP - Open/Closed Principle)

Exige que las entidades (clases, módulos y funciones) deban estar abiertas a la extensión y cerradas a la modificación.

```python
class OrdenadorInventario:
    def ordenar_por_precio(self, productos):
        return sorted(productos, key=lambda p: p["precio"])

    def ordenar_por_cantidad(self, productos):
        return sorted(productos, key=lambda p: p["cantidad"])
```

Si se necesita otro criterio de ordenación, se puede agregar (crear) un nuevo método sin modificar el código existente.

---

## 3. Principio de Sustitución de Liskov (LSP - Liskov Substitution Principle)

Establece que las subclases deben ser sustituibles por sus clases base. Es decir, las subclases deben poder usarse en lugar de su clase base (super clase) sin que afecte el funcionamiento del programa.

```python
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


class ProductoPerecedero(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion
```

Para este caso `ProductoPerecedero` extiende de `Producto` y puede utilizarse en cualquier función que espere un `Producto`

---

## 4. Principio de Segregación de Interfaces (ISP - Interface Segregation Principle)

Este principio establece que los clientes no deberían verse obligados a implementar interfaces que no necesitan. En otras palabras, `muchas interfaces específicas del cliente son mejores que una interfaz ded propósito general`. 

Es decir, cuando un cliente depende de una clase que implementa una interfaz cuya funcionalidad este cliente no usa, pero que otros clientes sí usan, este cliente estará siendo afectado por los cambios que fuercen otros clientes en dicha interfaz.

```python
class BuscadorPorNombre:
    def buscar_por_nombre(self, productos, nombre):
        # Devuelve el primer producto que tenga el mismo nombre exacto
        return next((producto for producto in productos if producto.nombre == nombre), None)


class BuscadorPorPrecio:
    def buscar_por_precio(self, productos, precio):
        # Devuelve todos los productos que tengan el precio exacto
        return [producto for producto in productos if producto.precio == precio]
```

Para este ejemplo hay dos clases, ambas buscan productos, pero por criterios diferentes. De esta manera se evita que una sola clase tenga mas responsabilidades de las que pueda necesitar.

---

## 5. Principio de Inversión de Dependencias (DIP - Dependency Inversion Principle)

Establece que las clases deben depender de interfaces o clases abstractas en lugar de clases y funciones concretas.. Es decir:

Los módulos de alto nivel no deberían depender de módulos de bajo nivel. Ambos deberían depender de abstracciones.

Las abstracciones no deberían depender de detalles. Los detalles deberían depender de abstracciones.

Si algo cambia en los detalles, no rompe todo el sistema. Este es un caso en el que debeos usar `inyeccion de dependencias (darle a una clase u objeto las herramientas que necesita desde afuera)` ya que esto permitirá decidir desde un solo lugar qué implementación usar, haciendo el código más fácil de mantener, probar y mejorar.

```javascript
class BaseDatos {
    guardar(producto) {
        throw new Error("Método no implementado");
    }
}

class BaseDatosSQL extends BaseDatos {
    guardar(producto) {
        console.log(`Guardando ${producto.nombre} en la base de datos SQL`);
    }
}

class Inventario {
    constructor(db) {
        this.db = db;
    }
    
    agregarProducto(producto) {
        this.db.guardar(producto);
    }
}
```

En este ejemplo podemos observar que `Inventario` no depende directamente de una base de datos concreta, sino de la abstracción `BaseDatos`. De esta forma se puede usar `BaseDatosSQL` u otra implementación sin cambiar la clase `Inventario`.

---
# Referencia:

Rodriguez, D. S. (2022, noviembre 28). Los principios SOLID de programación orientada a objetos explicados en Español sencillo. freecodecamp.org. https://www.freecodecamp.org/espanol/news/los-principios-solid-explicados-en-espanol/


