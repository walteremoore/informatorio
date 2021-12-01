# Hola Mundo - por pantalla
# print("Hola Mundo")
# Variables <nombre_variable> = <valor> | Por ejemplo: x = 10
# Se puede asignar un mismo valor a múltiples variables a la vez a = b = c = 1
# nombre = input("Ingrese su nombre")
# print(f"Hola {nombre}")
# print("este es un programa que suma dos numeros")
# numero1 = input("Ingrese el primer numero ")
# numero2 = input("Ingrese el segundo numero ")
# print("la suma es = ", int(numero1)+int(numero2))
# nombre = "walter"
# print(nombre.capitalize())
# if True:
#     print("Hola")
# cont = 0
# suma = 0
# n = int(input("Ingrese un tope maximo"))
# while cont<n :
#     suma = suma + cont
#     cont = cont + 1
#     print("la suma total es: ", suma)
#edad = int(input("Por favor ingrese su edad"))
#if (edad >= 18):
#    print("Usted es mayor de edad")
#else:
#    print("Usted es menor de edad")
#intentos = int(input("Por favor ingrese la cantidad de intentos fallidos"))
#if (intentos > 5):
#    print("Su cuenta se encuentra bloqueada")
#else:
#    print("Su cuenta no se encuentra bloqueada")
#preg = int(input("Ingrese la cantidad total de preguntas del cuestionario"))
#correc = int(input("Ingrese la cantidad de respuestas correctas"))
#porcentaje = correc * 100 / preg
#if (porcentaje >= 90):
#    print("El resultado es EXCELENTE")
#elif (porcentaje >= 70):
#    print("El resultado es BUENO")
#elif (porcentaje >= 60):
#    print("El resultado es APROBADO")
#else:
#    print("El resultado es NO ALCANZO")
#ventas1 = int(input("Ingrese las ventas del día 1"))
#ventas2 = int(input("Ingrese las ventas del día 2"))
#if ventas1>ventas2:
#    print("Se vendio más el día 1")
#else:
#    if ventas1<ventas2:
#        print("Se vendio más el día 2")
#    else: 
#        print("Se vendio lo mismo en ambos días")
#print("Bienvenido a la Pizzeria Bella Napoli. \nTipos de pizza \n\t1 - Vegetariana \n\t2 - No Vegetariana\n")
#tipo = int(input("Ingrese el número correspondiente a la pizza que quieres: "))
#if tipo == 1:
#    print("Ingredientes de pizzas Vegetarianas \n\t 1 - Pimiento \n\t 2 - Rúcula \n")
#    ingrediente = int(input("Introduce el número correspondiente al ingrediente que deseas: "))
#    print("Pizza Vegetariana con mozzarella, tomate y ", end="")
#    if ingrediente == 1:
#        print("Pimiento")
#    else:
#        print("Rúcula")
#else:
#    print("Ingredientes de pizzas No Vegetariana \n\t 1 - Jámon Crudo \n\t 2 - Jámon Cocido \n\t 3 - Panceta \n")
#    ingrediente = int(input("Introduce el número correspondiente al ingrediente que deseas: "))
#    print("Pizza No Vegetariana con mozzarella, tomate y ", end="")
#    if ingrediente == 1:
#        print("Jámon Crudo")
#    elif ingrediente == 2:
#        print("Jámon Cocido")
#    else:
#        print("Panceta")
#turno = input(print("Por favor ingrese su turno\n Turnos = mañana, tarde, noche"))
#nombre = input(print("Por favor ingrese su nombre. Ejemplo = Juan >>> "))
#if (turno == "tarde" and nombre.lower() < "m"):
#    print("Pertenece al grupo A")
#elif (turno == "noche" and nombre.lower() > "n"):
#    print("Pertenece al grupo A")
#else:
#    print("Pertenece al grupo B")
#var = 10
#while var>0:
#    var = var -1
#    if var == 5:
#        continue   salta la iteración actual
#    print("Valor actual de la variable :", var)
#var = 10
#while var>0:
#    var = var -1
#    if var == 5:
#        break   suspende la ejecución del blucle
#    print("Valor actual de la variable :", var)
#\\\\\\\\ CONDICIONALES \\\\\\\\\\
#Desafíos Condicionales / https://sites.google.com/view/nivel1-desafios/condicionales?authuser=0
#DESAFÍO 1
#En nuestro rol de Devs (Programador o Programadora de Software), debemos elaborar un programa en Python que permita emitir un mensaje de acuerdo a lo que una persona ingresa como cantidad de años que viene usando insecticida en su plantación. Si hace 10 o más añoss, debemos emitir el mensaje "Por favor solicite revisión de suelos en su plantación". Si hace menos de 10 años, debemos emitir el mensaje "Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación".
#anios=int(input("Ingrese la cantidad de años que viene usando insecticidas en su plantación >>> "))
#if anios >= 10:
#    print("Por favor solicite revisión de suelos en su plantación")
#else:
#    print("Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación")
#DESAFÍO 2
#Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en Python que dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 opciones:
#Tamaño Normal: Mensaje "Pez en buenas condiciones"
#Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
#Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
#Tamaño sobredimensionado: Mensaje "Pez contaminado"
#print("Indique el tamaño del pez >> \n(Seleccione algunas de las siguientes opciones)\n\t1-Tamaño Normal \n\t2-Tamaño por debajo de lo Normal \n\t3-Tamaño un poco por encima de lo Normal \n\t4-Tamaño sobredimensionado")
#opcion = int(input("Ingrese el número de opción correspondiente >>> "))
#if opcion == 1:
#    print("Pez en buenas condiciones")
#elif opcion == 2:
#    print("Pez con problemas de nutrición")
#elif opcion == 3:
#    print("Pez con síntomas de organismo contaminado")
#elif opcion == 4:
#    print("Pez contaminado")
#else:
#    print("Ingreso una opción incorrecta")
#DESAFÍO 3
#Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el cual debe existir en una cantidad de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL. Escribir un programa que determine si es factible la utilización de fertilizantes.
#hectarea = int(input("Ingrese la cantidad de Hectáreas (1 hectárea = 10.000 m2) >>> "))
#fertilizante = int(input("Ingrese el tipo de fertilizante a utilizar \n seleccione un item de la lista \n\t1-Nitrógeno (N) \n\t2-Fósforo (P2O5) \n\t3-Potasio (K2O) \n\t4-Azufre (S) "))
#kilos=int(input("Ingrese la cantidad de kilos a utilizar (1 saco = 50 kg) >>> "))
#if fertilizante == 1:
#    if hectarea*kilos<=(150*hectarea):
#        print("La cantidad de fertilizante de tipo nitrógeno (N) es correcta")
#    else:
#        print("La cantidad de fertilizante es INCORRECTA")
#elif fertilizante == 2:
#    if hectarea*kilos<=(300*hectarea):
#        print("La cantidad de fertilizante de tipo fósforo (P2O5) es correcta")
#    else:
#        print("La cantidad de fertilizante es INCORRECTA")
#elif fertilizante == 3:
#    if hectarea*kilos<=(100*hectarea):
#        print("La cantidad de fertilizante de tipo potasio (K2O) es correcta")
#    else:
#        print("La cantidad de fertilizante es INCORRECTA")
#elif fertilizante == 4:
#    if hectarea*kilos<=(30*hectarea):
#        print("La cantidad de fertilizante de tipo azufre (S) es correcta")
#    else:
#        print("La cantidad de fertilizante es INCORRECTA")
#else:
#    print("Ingreso una opción incorrecta")
#DESAFÍO 4
#Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.
#Ingredientes comunes: Verduras y berenjena.
#Ingredientes Receta 1: Lentejas y apio.
#Ingredientes Receta 2: Morrón y Cebolla..
#Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo de receta. Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.
#print("Bienvenido, por favor seleccione alguna de las dos recetas ecológicas. \nIngredientes en cada receta \n\t1 - Receta 1 \n\t2 - Receta 2\n")
#tipo = int(input("Ingrese el número correspondiente a la receta que quieres: "))
#if tipo == 1:
#    print("Ingredientes de Receta 1\n\t 1 - Lentejas \n\t 2 - Apio \n")
#    ingrediente = int(input("Introduce el número correspondiente al ingrediente que deseas: "))
#    print("Receta ecológica 1 con Verduras, Berenjenas y ", end="")
#    if ingrediente == 1:
#        print("Lentejas")
#    else:
#        print("Apio")
#else:
#    print("Ingredientes de Receta 2\n\t 1 - Morrón \n\t 2 - Cebolla \n")
#    ingrediente = int(input("Introduce el número correspondiente al ingrediente que deseas: "))
#    print("Receta ecológica 1 con Verduras, Berenjenas y ", end="")
#    if ingrediente == 1:
#        print("Morrón")
#    elif ingrediente == 2:
#        print("Cebolla")
#DESAFÍO 5
#La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
#La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
#Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.
#nombre = input("Ingrese el nombre del barrio")
#tipo = int(input("Ingrese el tipo de barrio \n Seleccione la opción correspondiente \n\t 1 - Céntrico \n\t 2 - No Céntrico"))
#print("La recolección de residuos pertenece a la zona: ", end="")
#if ((tipo==1 and nombre.lower()<"m") or (tipo==2 and nombre.lower()>"m")):
#    print("A")
#else:
#    print("B")
#\\\\ Repetitivas \\\\\\ https://sites.google.com/view/nivel1-desafios/repetitivas?authuser=0
#DESAFÍO 1
#Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.
#a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
#b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. 
# a) SIN LIMITES DE INTENTO
#usuariocorrecto = "admin"
#clavecorrecta = "password"
#bandera = True
#while bandera:
#    usuario=input("Ingrese su usuario >> ")
#    clave=input("Ingrese su clave >> ")
#    if usuario == usuariocorrecto and clave == clavecorrecta:
#        print("Usuario Validado, procediendo al sistema")
#        bandera = False
#    else:
#        print("Usuario o Clave incorrectos, por favor ingrese nuevamente sus datos")
# b) CON LIMITE DE 3 INTENTOS
#usuariocorrecto = "admin"
#clavecorrecta = "password"
#contador = 0
#for i in range(3):
#    usuario=input("Ingrese su usuario >> ")
#    clave=input("Ingrese su clave >> ")
#    contador = i 
#    if usuario == usuariocorrecto and clave == clavecorrecta:
#        print("Usuario Validado, procediendo al sistema")
#        break
#    elif i != 2:
#        print("Usuario o Clave incorrectos, por favor ingrese nuevamente sus datos")
#        print("Le restan ", 2-i, " intentos, luego se bloqueara su usuario por seguridad")
#if contador == 2:
#    print("Su usuario fue BLOQUEADO por SEGURIDAD. Comuniquese con el Administrador")
#DESAFÍO 2
#Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.
#Realizá un programa que permita registrar cantidad de colillas recolectadas por un número determinado de personas. Luego obtener estadísticas al respecto informando porcentaje de personas que han encontrado menos de 100 colillas, más de 100 y menos de 200, más de 200 colillas.
#contador = 0
#porc1 = 0
#porc2 = 0
#porc3 = 0
#colillas = 0
#cantidad = int(input("Ingrese la cantidad de personas recolectando colillas >> "))
#while (contador < cantidad):
#    contador = contador + 1
#    print("Ingrese la cantidad de colillas recolectadas por la persona número: ", contador)
#    colillas = int(input("Cantidad >> "))
#    if colillas<100:
#        porc1=porc1+1
#    elif colillas>=100 and colillas<=200:
#        porc2=porc2+1
#    elif colillas>200:
#        porc3=porc3+1
#print("Porcentaje de personas que han encontrador menos de 100 colillas: ", (porc1/cantidad)*100, "%")
#print("Porcentaje de personas que han encontrador más de 100 pero menos de 200 colillas: ", (porc2/cantidad)*100, "%")
#print("Porcentaje de personas que han encontrador más de 200 colillas: ", (porc3/cantidad)*100, "%")
#DESAFÍO 3
#En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra llegan a la caja y ofrecen tapitas para reciclar, de acuerdo a la cantidad que lleven en la caja le entregan un código de descuento que se aplicará sobre el total de su compra. Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta que cierra. 
#Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es amarilla un 25% y si es blanca no obtendrá descuento.
#blanco = 0
#amarillo = 0
#rojo = 0
#acumcompra = 0
#cantidadcompras = 0
#continuar = 0
#salir = False
#while not salir:
#    compra = float(input("Ingrese el importe de su compra >> "))
#    codigo= int(input("Ingrese el codigo de descuento >> \n Seleccione un item \n\t1-Rojo\n\t2-Amarillo\n\t3-Blanco\n Ingrese el número correspondiente al tipo de descuento >> "))
#    acumcompra = acumcompra + compra
#    cantidadcompras = cantidadcompras + 1
#    if codigo == 1:
#        rojo = rojo + 1
#        print("El importe total de su compra con el DESCUENTO del 40%, es de: $", (compra-compra*0.4))
#    elif codigo == 2:
#        amarillo = amarillo + 1
#        print("El importe total de su compra con el DESCUENTO del 25%, es de: $", (compra-compra*0.25))
#    elif codigo == 3:
#        blanco = blanco + 1
#        print("El importe total de su compra, es de: $", compra)
#    else:
#        print("Ingreso un codigo incorrecto de descuento")
#    continuar = input("Si desea continuar presione la tecla s, si desea finaliza, cualquier otra tecla >> ")
#    if continuar != "s":
#        salir = True
#print("El total de compras fue de: $", acumcompra, " en un total de ", cantidadcompras, " operaciones")
#print("la cantidad de DESCUENTOS de tipo ROJO fue de: ", rojo)
#print("la cantidad de DESCUENTOS de tipo AMARILLO fue de: ", amarillo)
#print("la cantidad de DESCUENTOS de tipo BLANCO fue de: ", blanco)
#DESAFÍO 4
#Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño indicado. Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6
#x=int(input("Ingrese el número de filas: "))
#y=int(input("Ingrese el número de columnas: "))
#for i in range(x):
#    for j in range(y):
#        if ((j + i) % 2) == 1:
#            print("\033[4;35;47m"+chr(32)+'\033[0;m', end=" ")
#        else:
#            print("\033[4;35;42m"+chr(32)+'\033[0;m', end=" ")
#    print('\n', end='')
#DESAFÍO 5
#Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos de basura a la vía pública.
#Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y un valor numérico de 5 dígitos a la Central con el siguiente significado:
#3 letras: Correspondientes a la patente.
#Del valor numérico:
#Los 3 primeros números corresponden a la patente
#El 4 número indica
#1- Tiró basura a la vía pública
#0 - No tiró basura a la vía pública
#El 5 número indica
#1- Ya había sido multado el vehículo
#0 - Vehículo sin multas.
#Deberás informar cantidad de vehículos observados, cantidad de vehículos que han tirado basura y porcentaje de éstos que ya habían sido multados.
#basura = 0
#multado = 0
#patente = 0
#vehiculos = 0
#while True:
#    patente = input("Ingrese la Patente del vehiculo >> \n Si desea salir ingrese: s\n >>>")
#    if patente == "s":
#        break
#    vehiculos = vehiculos + 1
#    if patente[6] == "1":
#        basura = basura + 1
#    if patente[7] == "1":
#       multado = multado + 1
#    print("la cantidad de vehiculos observados fué de: ", vehiculos)
#    print("la cantidad de vehiculos que han tirado basura fue de: ", basura)
#    print("el porcentaje de vehiculos que ya habian sido multados fue de: ", multado/basura*100, "%")
# //////////// listas-tuplas-diccionarios //////////////////
#Desafío 1
#Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10, almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor. 
#lista = []
#ordenada = []
#saber = 0
#continuar = "x"
#while True:
#    saber = int(input("Del 1 al 10, Cuánto conoce sobre contaminación?"))
#    lista += [saber]
#    continuar = input("Si desea continuar presione cualquier tecla.\n Si desea salir, pulse la letra: s >>>")
#    if continuar == "s":
#        break
#ordenada = sorted(lista)
#print(ordenada)
#Desafío 2
#Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua crea un programa que pida números, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
#El programa termina cuando el usuario introduce un cero.
#factores = ("Las aguas residuales", "Las sustancias químicas tóxicas", "Las aguas pluviales", "El vertido de plásticos", "Los vertidos de petróleo", "La actividad minera en alta mar", "El cambio climático", "Acidificación", "Eutrofización", "Toxinas")
#pedido = 0
#continuar = "a"
#while True:
#    pedido=int(input("Por favor ingrese un número >>> "))
#    if pedido <= len(factores):
#        print("El factor que afecta al mar es: >> ", factores[pedido])
#    else:
#        print("Error, número incorrecto, fuera de rango")
#    continuar=input("Si desea continuar ingrese cualquier letra, \npara salir pulse la letra >> s\n >>>")
#    if continuar == "s":
#        break
#Desafío 3
#Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos.
#nombre = "a"
#correo = "b"
#continuar = "c"
#diccionario = {}
#while True:
#    nombre = input("Ingrese por favor el nombre del biólogo/a >> ")
#    correo = input("Ingrese por favor el correo electronico del biólogo/a >> ")
#    if nombre in diccionario:
#        print("No se puede ingresar nombres repetidos a la agenda")
#    else:
#        diccionario[nombre] = correo
#    continuar=input("Si desea continuar ingrese cualquier letra, \npara salir pulse la letra >> s\n >>>")
#    if continuar == "s":
#        break
#print(diccionario)
#Desafío 4
#Escribir un programa que cargue una tupla con nombres de especie, y para cada nombre de especie imprima el mensaje Hola soy ......, cuidame.
#Modificá el programa anterior y dada una posición inicial p y una cantidad n, imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición i.
#especies = ("Mamíferos", "Aves", "Reptiles", "Ranas y sapos", "Peces", "Ciempiés y milpiés", "Arañas y alacranes", "Insectos", "Cangrejos y camarones", "Estrellas y erizos", "	Caracoles, almejas y pulpos", "Lombrices y gusanos marinos", "Rotíferos", "Gusanos planos", "Medusas y corales", "Esponjas")
#inicio = int(input("Hola por favor ingresa la posición inicial >> "))
#cantidad = int(input("Por favor ingresa la cantidad de elementos >> "))
#for i in range(inicio, inicio+cantidad, 1):
#    print("Hola soy ", especies[i], " cuidame.")
# //// COMPLEMENTARIOSSSS ///////
# condicionales
# Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.
#n1 = int(input("Por favor ingrese el primer número >> "))
#n2 = int(input("Por favor ingrese el segundo número >> "))
#n3 = int(input("Por favor ingrese el tercer número >> "))
#if n1 > n2 and n1 > n3:
#    print("El mayor es: ", n1)
#elif n2>n1 and n2>n3:
#    print("El mayor es: ", n2)
#elif n3>n1 and n3>n2:
#    print("El mayor es: ", n3)
#if (n1 > n3 and n1 < n2) or (n1 < n3 and n1 > n2):
#    print("El siguiente es: ", n1)
#elif (n2 < n1 and n2 > n3) or (n2 > n1 and n2 < n3):
#    print("El siguiente es: ", n2)
#elif (n3 < n1 and n3 > n2) or (n3 > n1 and n3 < n2):
#    print("El siguiente es: ", n3)
#if n1 < n2 and n1 < n3:
#    print("El menor es: ", n1)
#elif n2<n1 and n2<n3:
#    print("El menor es: ", n2)
#elif n3<n1 and n3<n2:
#    print("El menor es: ", n3)
#Desarrolle un programa que permita determinar si un número X ingresado es par o impar.
#num = int(input("Por favor ingrese un número >> "))
#if num % 2 == 0:
#    print("El número ingresado es par")
#else:
#    print("El número ingresado es impar")
#Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.
#n1 = int(input("Por favor ingrese el primer número >> "))
#n2 = int(input("Por favor ingrese el segundo número >> "))
#n3 = int(input("Por favor ingrese el tercer número >> "))
#if n1 < n2 and n1 < n3:
#    print("El primer número ingresado es menos a los otros dos")
#else: 
#    print("El primer número ingresado no es menor a los otros dos")
#Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.
#n1 = int(input("Por favor ingrese el primer número >> "))
#n2 = int(input("Por favor ingrese el segundo número >> "))
#if n1 % n2 == 0:
#    print("El número ", n1, " es divisible por ", n2, " su modulo es 0")
#else:
#    print("El número ", n1, " NO es divisible por ", n2, " su modulo es distinto 0")
#Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué tipo de triángulo es, de acuerdo a los siguientes casos. Suponiendo que A determina el mayor de los tres lados y B y C corresponden con los otros dos, entonces:
#Si A>=B + C à No se trata de un triángulo
#Si A2 = B2 + C2 à Es un triángulo rectángulo
#Si A2 > B2 + C2 à Es un triángulo obtusángulo
#Si A2 < B2 + C2 à Es un triángulo acutángulo
#l1 = float(input("Por favor ingrese el primer lado del triángulo >> "))
#l2 = float(input("Por favor ingrese el segundo lado del triángulo >> "))
#l3 = float(input("Por favor ingrese el tercer lado del triángulo >> "))
#if (l1 >= l2 + l3):
#    print("No se trata de un triángulo")
#elif (l1**2 == l2**2 + l3**2):
#    print("Es un triángulo rectángulo")
#elif (l1**2 > l2**2 + l3**2):
#    print("Es un triángulo obtusángulo")
#elif (l1**2 < l2**2 + l3**2):
#    print("Es un triángulo obtusángulo")
#Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario para la siguiente campaña. Los sueldos deben ajustarse de la siguiente forma:
#Sueldo Actual (en $)    Aumento
#0 – 6000							15%
#6000 – 7900					   10%
#7900 – 12000					6%
#Más de 12000				   0%
#Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por ciento de aumento, el sueldo actual y el sueldo aumentado.
#while True:
#    actual = (input("Por favor ingrese el salario actual del jugador >> \nsi desea salir pulse la tecla s \n >>> "))
#    if actual == "s":
#        break
#    else:
#        actual = float(actual)
#    if actual<=6000:
#        print("Su nuevo salario tendra un aumento del 15%, pasando de: $", actual, "a la nueva suma: $", (actual*0.15+actual))
#    elif actual>6000 and actual<=7900:
#        print("Su nuevo salario tendra un aumento del 10%, pasando de: $", actual, "a la nueva suma: $", (actual*0.10+actual))
#    elif actual>7900 and actual<=12000:
#        print("Su nuevo salario tendra un aumento del 6%, pasando de: $", actual, "a la nueva suma: $", (actual*0.06+actual))
#    elif actual>12000:
#        print("Su salario no tiene un aumento programado, quedando en la suma de $", actual)
#Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. Obtenga para determinado cliente cuánto deberá pagar finalmente por su compra y el descuento obtenido, si es que corresponde.
# prueba