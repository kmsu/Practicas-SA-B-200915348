#Clase para crear productos
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    #__str__ Es un metodo de python como mostrar el objeto para imprimirlo o verlo en consola
    def __str__(self):
        return f"{self.nombre} - {self.cantidad} unidades - Q{self.precio:.2f}"

#Para mostrar el menu, es la funcion predeterminada del programa
def main():
    # Lista que guarda los productos (inventario) 
    listaProductos = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            agregar_producto(listaProductos)
        elif opcion == "2":
            eliminar_producto(listaProductos)
        elif opcion == "3":
            mostrar_productos(listaProductos)
        elif opcion == "4":
            ordenar_productos(listaProductos)
        elif opcion == "5":
            buscar_producto(listaProductos)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def agregar_producto(listaProductos):
    # Ingresa un nuevo producto
    nombre = input("Ingrese el nombre del producto: ").strip()

    #Validar que el nombre no se ingrese vacio
    if not nombre:
        print("El nombre no puede estar en blanco.")
        return
    
    #Validar que el producto no exista en el inventario
    for producto in listaProductos:
        if producto.nombre.lower() == nombre.lower():
            print("El producto ya existe")
            return
    
    # Ingresar la cantidad y el precio y convertirlo en un valor numerico
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
    except ValueError:
        print("Entrada invalida. Cantidad debe ser entero y precio debe ser decimal.")
    
    #Crear el producto
    nuevoProducto = Producto(nombre, cantidad, precio)
    #Agregar a la lista de productos (inventario)
    listaProductos.append(nuevoProducto)
    print("Producto agregado correctamente")

def eliminar_producto(listaProductos):
    # Ingresar el nombre del producto a eliminar
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()

    for producto in listaProductos:
        if producto.nombre.lower() == nombre.lower():
            listaProductos.remove(producto)
            print("Producto ", nombre, " eliminado correctamente.")
            return
    #Si no encontro nada en el for llega hasta aqui
    print("Producto no encontrado.")

def mostrar_productos(listaProductos):
    #Validar si la lista (inventario) esta vacio
    if not listaProductos:
        print("No hay productos en el inventario")
        return
    
    print("\n LISTA DE PRODUCTOS")
    for id, producto in enumerate(listaProductos, start=1):
        print(f"{id}. Nombre: {producto.nombre} | Cantidad: {producto.cantidad} | Precio: Q{producto.precio:.2f}")

def ordenar_productos(listaProductos):
    print("ordenar producto")

def buscar_producto(listaProductos):
    print("buscar producto")

def mostrar_menu():
    # Menu a mostrar con sus respectivas opciones
    print("\n===== MENÚ DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar productos")
    print("4. Mostrar productos ordenados (precio y/o cantidad)")
    print("5. Buscar producto por nombre")
    print("6. Salir")

if __name__ == "__main__":
    main()