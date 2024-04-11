registro_libros = {}

while True:
    print("\nBienvenido al sistema de registro de libros.")
    print("1. Registrar libro")
    print("2. Buscar libro")
    print("3. Salir")

    opcion = input("Por favor, seleccione una opción: ")

    if opcion == "1":
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        registro_libros[titulo] = {"Autor": autor, "Género": genero}
        print("Libro registrado exitosamente.")
    elif opcion == "2":
        titulo = input("Ingrese el título del libro que desea buscar: ")
        if titulo in registro_libros:
            info_libro = registro_libros[titulo]
            print(f"Información del libro '{titulo}':")
            print(f"Autor: {info_libro['Autor']}")
            print(f"Género: {info_libro['Género']}")
        else:
            print("El libro no se encuentra registrado.")
    elif opcion == "3":
        print("Gracias por usar el sistema de registro de libros. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")