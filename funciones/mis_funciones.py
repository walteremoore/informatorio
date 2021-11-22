#def sumar(param1, param2):
#    return param1 + param2

#def desafio1(tipo_elemento):
#    if tipo_elemento.lower() == "Bolsa de Plastico".lower():
#        return 150
#    elif tipo_elemento.lower() == "Botella PET".lower():
#        return 1000
#    elif tipo_elemento.lower() == "Envase Tetrabrik".lower():
#        return 30
#    elif tipo_elemento.lower() == "Chicle".lower():
#        return 5
#    else:
#        return None

def mostrar_menu(lista):
    print("Por favor ingrese el tipo de producto para evaluar su impacto ")
    for op in lista:
        print(f"{op['clave']} - {op['nombre']}")

def desafio1_1():
    mostrar_menu(elementos_validos)

elementos_validos = [
    {"clave": 1, "nombre": "Bolsa de Plastico", "anios_degradacion": 150},
    {"clave": 2, "nombre": "Botella PET", "anios_degradacion": 1000},
    {"clave": 3, "nombre": "Envase Tetrabik", "anios_degradacion": 30},
    {"clave": 4, "nombre": "Chicle", "anios_degradacion": 5},
]

def validar_entrada(lista, elemento):
    for op in lista:
        if op['clave'] == elemento:
            return (op['anios_degradacion']), op['nombre'] # devuelvo 2 cosas, los años que demora en degradarse y el nombre del elemento
    return None, None # debo devolver dos none, si ingreso una clave que no esta en el diccionario, dado que estoy retornando dos parametros

def relacion(a,b):
    if a[0] > b[0]:
        return a[1], None
    elif a[0] < b[0]:
        return b[1], None
    else:
        return a[1], b[1]

def relaciondiccionario(a,b):
    if a["toneladas_recicladas"] > b["toneladas_recicladas"]:
        return a["nombre_ciudad"], None
    elif a["toneladas_recicladas"] < b["toneladas_recicladas"]:
        return b["nombre_ciudad"], None
    else:
        return a["nombre_ciudad"], b["nombre_ciudad"]