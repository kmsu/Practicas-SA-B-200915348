# Programa de Gestión de Inventario de Productos

def mostrar_menu():
    """Muestra el menú de opciones disponibles."""
    print("\n===== MENÚ DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar lista de productos")
    print("4. Mostrar productos ordenados")
    print("5. Buscar producto por nombre")
    print("6. Salir")


def agregar_producto(inventario):
    """Agrega un nuevo producto al inventario."""
    nombre = input("Ingrese el nombre del producto: ").strip()
    
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return

    # Verificar si el producto ya existe
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print("❌ El producto ya existe en el inventario.")
            return

    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
    except ValueError:
        print("❌ Entrada inválida. Cantidad debe ser entero y precio debe ser decimal.")
        return

    nuevo_producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
    inventario.append(nuevo_producto)
    print("✅ Producto agregado correctamente.")


def eliminar_producto(inventario):
    """Elimina un producto del inventario por su nombre."""
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto)
            print("✅ Producto eliminado correctamente.")
            return

    print("❌ Producto no encontrado.")


def mostrar_productos(inventario):
    """Muestra todos los productos en el inventario."""
    if not inventario:
        print("📭 No hay productos en el inventario.")
        return

    print("\n📦 LISTA DE PRODUCTOS:")
    for idx, producto in enumerate(inventario, start=1):
        print(f"{idx}. Nombre: {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: Q{producto['precio']:.2f}")


def ordenar_productos(inventario):
    """Muestra productos ordenados por precio o cantidad."""
    if not inventario:
        print("📭 No hay productos en el inventario.")
        return

    print("\n¿Ordenar por?")
    print("1. Precio")
    print("2. Cantidad")
    opcion = input("Seleccione una opción (1-2): ")

    if opcion == "1":
        productos_ordenados = sorted(inventario, key=lambda x: x["precio"])
    elif opcion == "2":
        productos_ordenados = sorted(inventario, key=lambda x: x["cantidad"])
    else:
        print("❌ Opción inválida.")
        return

    print("\n📊 PRODUCTOS ORDENADOS:")
    for idx, producto in enumerate(productos_ordenados, start=1):
        print(f"{idx}. Nombre: {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: Q{producto['precio']:.2f}")


def buscar_producto(inventario):
    """Busca un producto por su nombre."""
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print(f"🔍 Producto encontrado:")
            print(f"Nombre: {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: Q{producto['precio']:.2f}")
            return

    print("❌ Producto no encontrado.")


def main():
    """Función principal que ejecuta el programa."""
    inventario = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            eliminar_producto(inventario)
        elif opcion == "3":
            mostrar_productos(inventario)
        elif opcion == "4":
            ordenar_productos(inventario)
        elif opcion == "5":
            buscar_producto(inventario)
        elif opcion == "6":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
