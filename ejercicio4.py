peliculas = {}

while True:
    print("\nBienvenido al sistema de registro de películas.")
    print("1. Registrar película")
    print("2. Buscar película")
    print("3. Salir")

    opcion = input("Por favor, seleccione una opción: ")

    if opcion == "1":
        titulo = input("Ingrese el título de la película: ")
        genero = input("Ingrese el género de la película: ")
        año = input("Ingrese el año de la película: ")
        peliculas[titulo] = {"Género": genero, "Año": año}
        print("Película registrada exitosamente.")
    elif opcion == "2":
        titulo = input("Ingrese el título de la película que desea buscar: ")
        if titulo in peliculas:
            info_pelicula = peliculas[titulo]
            print(f"Información de la película '{titulo}':")
            print(f"Género: {info_pelicula['Género']}")
            print(f"Año: {info_pelicula['Año']}")
        else:
            print("La película no se encuentra registrada.")
    elif opcion == "3":
        print("Gracias por usar el sistema de registro de películas. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")