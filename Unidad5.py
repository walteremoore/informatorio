#tuplas
#listas
#diccionarios
#set


#tuplas son estructuras de datos inmutables, que no pueden cambiar. 
t = (1, "hola", True)
print("Iterando sobre una tupla")
for x in t:
    print(x)

print("hola" in t) # preguntar si un elemento esta en una tupla.


# listas son estructuras de datos que pueden cambiar, crecer, etc.

l = ["hola", 1, True]
print("Iterando sobre una lista")
for x in l:
    print(x)

l.append("mundo") # agregar un objeto a la lista

print("Iterando la misma lista")
for x in l:
    print(x)

print(l[0]) # podemos mostrar un elemento buscandolo por su posición arrancando en cero.

# diccionarios 

d = { "nombre": "Walter",
        "apellido": "Moore"}

print(d["nombre"]) # podemos mostrar elementos a traves de las claves usando corchetes.
print(d.get("apellido", None)) # tambien podemos acceder al valor de una clave, usando la funcion get(). El none es un valor por defecto si no encuentra el valor

# set