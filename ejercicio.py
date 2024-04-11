
import os
agenda = {}
def fnt_limpiar():
    os.system("cls")
    print("\nBienvenido al sistema de calificacion de estudiantes")
    print("Autor: Yasuan S Caicedo")
    print("Institucion: Universidad CLA")
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")
    agenda[nombre] = telefono
    print("Contacto agregado ")

def buscar_contacto():
    nombre = input("ingrese el nombre del contacto que desea buscar: ")
    if nombre in agenda:
        print(f"el número de teléfono de {nombre} es: {agenda[nombre]}")
    else:
        print("el contacto no se encuentra en la agenda.")

while True:
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        print("chao")
        break
    else:
        print("errorrr, seleccione una opción válida.")