inventario = {}

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible del producto: "))
    inventario[nombre] = cantidad
    print("Producto agregado al inventario correctamente!")

def buscar_producto():
    nombre = input("Ingrese el nombre del producto que desea buscar: ")
    if nombre in inventario:
        print(f"La cantidad disponible de {nombre} es: {inventario[nombre]}")
    else:
        print("El producto no se encuentra en el inventario.")

while True:
    print("\n1. Agregar producto")
    print("2. Buscar producto")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        buscar_producto()
    elif opcion == "3":
        print("chao")
        break
    else:
        print("seleccione una opción válida.")