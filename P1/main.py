
#Para mostrar el menu, es la funcion predeterminada del programa
def main():
    # Lista que guarda los productos (inventario) 
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

def agregar_producto(inventario):
    print("agregar producto")

def eliminar_producto(inventario):
    print("eliminar producto")

def mostrar_productos(inventario):
    print("mostrar producto")

def ordenar_productos(inventario):
    print("ordenar producto")

def buscar_producto(inventario):
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