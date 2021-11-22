# En python todo son funciones, los procedimientos son funciones que no devuelven nada.
# Una función devuelve un valor y un procedimiento solo ejecuta comandos.

#def saludar(): #ejemp. procedimiento (Devuelve None al ser invocada)
#    print("Hola")

#def devuelve_1(): #ejemp. función (Devuelve 1 con el return al ser invocada)
#    print("Hola nuevamente")
#    return 1

# paso de parametros por posición

#def sumar(x,y):
#    return x + y

# variables locales, ejemplo con variable z (si quiero llamar a la variable z afuera de la función multiplicar, la misma no funcionara, dira que no esta definida)

#def multiplicar(n,m):
#    z = n * m
#    return z

# paso de parametros por referencia (le indico a la funcion que valor asignar a cada posición mediante la referencia a su nombre de variable)

#a = 3
#b = 5
#suma = sumar(x=b, y=a) --> necesito identificar cada parametro por su nombre
#print(suma)

# pasar muchos valores a una funcion y guardarlos en una tupla, ideal cuando no se cuantas cosas me van a pasar.

#def acumular(*tupla):
#    for x in tupla:
#        print(x)
#acumular(3,5,77,-2,0.874,"hola mundo")

# def suma_args(*args):
#   suma = 0
#   for x in args:
#       suma +=x
#   return suma


# paso de parametros por valor
# cuando llamamos a la función, le pasamos los valores para que opere
# los valores que le pasamos no se alteran posterior al procesamiento.

#Ejemplo paso por valor (defino una función valor que recibe un parametro, 
# defino una variable z con un valor 1, llamo a la funcion con esa variable como parametro,
# luego imprimo el valor de z y me arroja por pantalla el 1. eso es porque no se altero
# el valor contenido en el parametro, porque se apuntan a diferentes lugares de memoria.)
# los tipos de datos que se pasan por copia son: integer, float, string, bool, etc.
# Paso por valor: Se crea una copia local de la variable dentro de la función

#def valor(x):
#    x = "asd"

#z = 1
#valor(z)
#print(z)

# paso de parametro por referencia
# al llamar a la función le pasa la referencia de donde esta ubicado el objeto
# la función puede alterar el valor almacenado en esa referencia a memoria interna.

# ejemplo paso por referencia, defino la misma funcion, pero en vez de usar numero o string, 
# uso una lista, este tipo de estructura permiten la referencia de memoria, entonces se va a producir
# una alteración del contenido, porque ambos apuntan al mismo lugar de memoria interna.
# los tipos de datos que se pueden modificar son: listas, diccionarios, conjuntos.
# Paso por referencia: Se maneja directamente la variable, los cambios realizados dentro de la función le afectarán también fuera.

#cambio

#def valor(x):
#    x.append(2)

#z = [1]
#valor(z)
#print(z)

# Uso de modulos para contener las funciones en un archivo y solo importarlas luego para utilizarlas. 
# para renombrar las funciones usando alias, tengo que colocar lo siguiente: from funciones.mis_funciones import sumar as sumar2 
# entonces ahora la funcion sumar que importamos, se va a llamar sumar2
# para importar todo lo que esta en un archivo contenedor uso la sintaxys = from funciones.mis_funciones import *
# con el * le digo que importe todo lo que esta adentro de ese archivo-modulo
# para saber donde estoy parado, si soy padre, hijo, etc. uso la variable: __name__

from funciones.mis_funciones import *
#x = int(input("Ingrese un número por favor >> "))
#y = int(input("Ingrese otro número por favor >> "))
#z = sumar(x, y)
#print(f"La suma es: {z}")

# ejemplo para saber desde donde estoy realizando las invocaciones. 

#if __name__ == "__main__":
#    print(f"Estoy en el modulo principal Unidad4.py: {__name__}")

# paso de parametros mediante diccionarios (estructura de datos compuesta por clave y valor)

#def suma_kwarg(**kwargs):
#    print(kwargs) # si quiero obtener el valor de una posición especifica, consulto de esta manera: kwarg["parametro1"], esto me devuelve con el print el 1.
#suma_kwarg(parametro1=1, parametro2=2, parametro3=3)

#Desafio1 - https://sites.google.com/view/nivel1-desafios/funciones?authuser=0
#print("Por favor ingrese el tipo de producto para evaluar su impacto ")
#elemento = input("Bolsa de Plastico / Botella PET / Envase Tetrabik / Chicle >> ")
#anios_degradacion = desafio1(elemento)
#if anios_degradacion == None:
#    print("Ingreso un parametro incorrecto")
#else:
#    print(f"El elemento {elemento.lower()} tarda {anios_degradacion} años en degradarse." )

#elementos_validos = [
#    {"clave": 1, "nombre": "Bolsa de Plastico", "anios_degradacion": 150},
#    {"clave": 2, "nombre": "Botella PET", "anios_degradacion": 1000},
#    {"clave": 3, "nombre": "Envase Tetrabik", "anios_degradacion": 30},
#    {"clave": 4, "nombre": "Chicle", "anios_degradacion": 5},
#]

#desafio1_1()
#elemento = int(input("Por favor ingrese el valor correspondiente al producto para evaluar su impacto >> "))
#opcion, nombre_elto = validar_entrada(elementos_validos, elemento) # como la funcion devuelve dos cosas, debo almacenarlas en dos variables diferentes 
#if opcion == None:
#    print("Ingreso un parametro incorrecto")
#else:
#    print(f"El elemento {nombre_elto} tarda {opcion} años en degradarse." )

#buscar segun la clave ejemplo, siempre debo reccorrer con un para buscando el elemento. 
#a = 2
#for x in elementos_validos:
#    if x['clave'] == a:
#        print(f"El elemento {x['nombre']} tarda {x['anios_degradacion']} años en degradarse.")
#        break # una vez que encontre el elemento, puedo cortar la iteración bucle.


# Desafio 2 

#ciudad1 = "Resistencia"
#ciudad2 = "Corrientes"
#toneladas_recicladas_c1 = 2500
#toneladas_recicladas_c2 = 2500

#resultado = relacion((toneladas_recicladas_c1,ciudad1), (toneladas_recicladas_c2,ciudad2)) #uso de tuplas
#print(resultado) # es una buena practica, que una funcion siempre devuelva la misma cantida de valores, despues nosotros los tratamos afuera.

#resultado = relaciondiccionario(a={"nombre_ciudad": ciudad1, "toneladas_recicladas": toneladas_recicladas_c1}, b={"nombre_ciudad": ciudad2, "toneladas_recicladas": toneladas_recicladas_c2})
#print(resultado)

#ultimo