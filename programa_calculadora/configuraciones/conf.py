# Variables

version = 1.0

# Funciones y/o Procedimientos

import os # Libreria del sistema para ejecutar comandos sobre consola cmd.
def limpiar_pantalla():
    os.system("clear") # Comando para limpiar la pantalla cada vez que se ejecuta. En windows es cls. En linux clear

import time # Libreria para trabajar con tiempo del sistema.
def tiempo_espera():
    time.sleep(2) # Espera 2 segundos antes de ejecutar la proxima linea de codigo.

def mostrar_acerca_de(): # Opción del menu para mostrar info del programa.
    limpiar_pantalla()
    print("Programa desarrollado en el Informatorio")
    print("Tecnologia: Python 3")
    print("Desarrollado por Walter Moore")
    print(f"Versión de la aplicación: {version}")
    input("")

def validar_numero(cadena): #valida que lo que ingresa el usuario sea un número.
    while not cadena.isdigit():
        print("Ingrese un número valido por favor")
        cadena = input(" >> ")
    return int(cadena)