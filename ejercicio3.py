estudiantes = {}

while True:
    print("\nBienvenido al sistema de registro de estudiantes.")
    print("1. Registrar estudiante")
    print("2. Buscar estudiante")
    print("3. Salir")

    opcion = input("Por favor, seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = input("Ingrese la edad del estudiante: ")
        carrera = input("Ingrese la carrera del estudiante: ")
        estudiantes[nombre] = {"Edad": edad, "Carrera": carrera}
        print("Estudiante registrado exitosamente.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante que desea buscar: ")
        if nombre in estudiantes:
            info_estudiante = estudiantes[nombre]
            print(f"Información de {nombre}:")
            print(f"Edad: {info_estudiante['Edad']}")
            print(f"Carrera: {info_estudiante['Carrera']}")
        else:
            print("El estudiante no se encuentra registrado.")
    elif opcion == "3":
        print("Gracias por usar el sistema de registro de estudiantes. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")