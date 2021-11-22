from configuraciones.conf import *

bandera = True
while bandera:
    limpiar_pantalla()
    print("===========================================")
    print("#             MI CALCULADORA              #")
    print("===========================================")
    print(f"Programa desarrollado por Walter Moore V{version}")
    print("Ingrese una de las siguientes opciones: ")
    print("S - Salir del programa.")
    print("A - Acerca De...")
    opcion = input("Ingrese la opción seleccionada >> ")
    if opcion.lower() == "s":
        print("Gracias por utilizar la Calculadora")
        bandera = False
    elif opcion.lower() == "a":
        mostrar_acerca_de()
print("Finalizando programa ----")
tiempo_espera()
print("Adios.")