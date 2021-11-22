class Persona:
    def __init__(self, nombre, edad, sexo, estatura, peso):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.estatura = estatura
        self.peso = peso
    
    def hablar(self):
        print("Hola soy {}".format(self.nombre))
    
    def correr(self):
        print("{} está corriendo".format(self.nombre))
    
    def caminar(self):
        print("{} está caminando".format(self.nombre))

persona1 = Persona("Juan", 23, "Masculino", 170, 90)
persona2 = Persona("Maria", 25, "Femenino", 160, 70)

print(persona1.nombre)
print(persona1.edad)
print(persona1.sexo)
print(persona1.estatura)
print(persona1.peso)
persona1.hablar()
persona1.correr()
persona1.caminar()


""" En Python no existen los modificadores de acceso, y lo que se suele hacer es usar convenciones
a la hora de nombrar métodos y atributos, de forma que se señale su carácter privado, para su
exclusión del espacio de nombres, o para indicar una función especial, normalmente asociada a
funcionalidades estándar del lenguaje.
● _nombre: Los nombres que comienzan con un único guión bajo indican de forma débil
un uso interno. Además, estos nombres no se incorporan en el espacio de nombres de
un módulo al importarlo con "from ... import *".
● __nombre: Los nombres que empiezan por dos guiones bajos (y no termina también con
dos guiones bajos) indican su uso privado en la clase.
● __nombre__: Los nombres que empiezan y acaban con dos guiones bajos indican
atributos "mágicos", de uso especial y que residen en espacios de nombres que puedemanipular el usuario. Solamente deben usarse en la manera que se describe en la
documentación de Python y debe evitarse la creación de nuevos atributos de este tipo.
Algunos ejemplos de nombres "singulares" de este tipo son:
○ __init__, método de inicialización de objetos
○ __del__, método de destrucción de objetos
○ __doc__, cadena de documentación de módulos, clases...
○ __class__, nombre de la clase
○ __str__, método que devuelve una descripción de la clase como cadena de texto
○ __repr__, método que devuelve una representación de la clase como cadena de
texto
○ __module__, módulo al que pertenece la clase
En el siguiente ejemplo sólo se imprimirá la cadena correspondiente al método publico(),
mientras que al intentar llamar al método __privado() Python lanzará una excepción debido a
que no existe, evidentemente existe pero no lo podemos ver porque es privado. """

class Ejemplo:
    def publico(self):
        print("Publico")
    def __privado(self):
        print("Privado")
ej = Ejemplo()
ej.publico()
ej.__privado() # falla al ejecutarlo 

#uso de trampa para midificar un atriburto privado
ej._Ejemplo__privado() 
""" trampa para que no falle (Este mecanismo se basa en que los nombres que comienzan con un doble guión bajo se
renombran para incluir el nombre de la clase (característica que se conoce con el nombre de
name mangling). Esto implica que el método o atributo no es realmente privado, y podemos
acceder a él mediante una pequeña trampa) """

class Fecha():
    def __init__(self):
        self.__dia = 1
    def getDia(self):
        return self.__dia
    def setDia(self, dia):
        if dia > 0 and dia <= 31:
            self.__dia = dia
        else:
            print("Error")
mi_fecha = Fecha()
mi_fecha.setDia(33) # da error
mi_fecha.__dia= 30
print(mi_fecha.getDia()) # devuelve 1

# uso de propiedades para abstraer del uso de metodos para cambiar los valores de las variables.
class Fecha(object):
    def __init__(self):
        self.__dia = 1
    def getDia(self):
        return self.__dia
    def setDia(self, dia):
        if dia > 0 and dia <= 31:
            self.__dia = dia
        else:
            print("Error")
    dia = property(getDia, setDia)
mi_fecha = Fecha()
mi_fecha.dia = 30
print(mi_fecha.dia) # devuelve 30


# HERENCIA

class Instrumento:
    def __init__(self, precio):
        self.precio = precio
    def tocar(self):
        print("Estamos tocando música")
    def precio(self):
        print("El precio de este instrumento es: $", self.precio)
class Bateria(Instrumento): # Para indicar que una clase hereda de otra se coloca el nombre de la clase de la que se hereda
    pass                    #  entre paréntesis después del nombre de la clase
class Guitarra(Instrumento):
    pass

""" puede ocurrir en algunos casos que necesitemos sobreescribir un método de la
clase padre, pero que en ese método queramos ejecutar el método de la clase padre porque
nuestro nuevo método no necesite más que agregar un par de instrucciones extra. En ese caso
usamos la sintaxis SuperClase.metodo(self, args) para llamar al método de igual nombre de la
clase padre. Por ejemplo, para llamar al método __init__ de Instrumento desde Guitarra
usaríamos Instrumento.__init__(self, precio). """

class Instrumento:
    def __init__(self, precio):
        self.precio = precio
    def tocar(self):
        print("Estamos tocando música")
    def correr(self):
        print("El precio de este instrumento es: $", self.precio)
class Bateria(Instrumento):
    pass
class Guitarra(Instrumento):
    def __init__(self, tipo_cuerda, precio):
        Instrumento.__init__(self, precio)
        self.tipo_cuerda = tipo_cuerda

# Herencia múltiple

class Terrestre:
    def __init__(self):
        pass
    def desplazar(self):
        print("El animal anda")
class Acuatico:
    def __init__(self):
        pass
    def desplazar(self):
        print("El animal nada")
class Cocodrilo(Terrestre, Acuatico):
    pass

""" En el caso de que alguna de las clases padre tuvieran métodos con el mismo nombre y número
de parámetros las clases sobreescribirían la implementación de los métodos de las clases más a
su derecha en la definición.
En el siguiente ejemplo, como Terrestre se encuentra más a la izquierda, sería la definición de
desplazar() de esta clase la que prevalecerá, y por lo tanto si llamamos al método desplazar de
un objeto de tipo Cocodrilo lo que se imprimiría sería “El animal anda”. """

class Terrestre:
    def __init__(self):
        pass
    def desplazar(self):
        print("El animal anda")
class Acuatico:
    def __init__(self):
        pass
    def desplazar(self):
        print("El animal nada")
class Cocodrilo(Terrestre, Acuatico):
    pass
c = Cocodrilo()
c.desplazar()
# Resultado -> El animal anda

""" Lo mismo ocurre para el caso de constructor, en caso de que se requiera el uso de el constructor
de alguna clase específica puede usarse la sintaxis anteriormente vista,
SuperClase.metodo(self, args). """


class Terrestre:
    def __init__(self):
        print("Este es el constructor de la clase Terrestre")
    def desplazar(self):
        print("El animal anda")
class Acuatico:
    def __init__(self):
        print("Este es el constructor de la clase Acuático")
    def desplazar(self):
        print("El animal nada")
class Cocodrilo(Terrestre, Acuatico):
    pass
c = Cocodrilo()
# Resultado -> Este es el constructor de la clase Terrestre


class Terrestre:
    def __init__(self):
        print("Este es el constructor de la clase Terrestre")
    def desplazar(self):
        print("El animal anda")
class Acuatico:
    def __init__(self):
        print("Este es el constructor de la clase Acuático")
    def desplazar(self):
        print("El animal nada")
class Cocodrilo(Terrestre, Acuatico):
    def __init__(self):
        Acuatico.__init__(self)
c = Cocodrilo()
# Resultado -> Este es el constructor de la clase Acuático


# Herencia multinivel en Python


class Figura:
    def __init__(self, area):
        self.area = area
    def retornar_area(self):
        print("El área de la figura es:", self.area)

class Poligono(Figura):
    def __init__(self, lados, area):
        Figura.__init__(self, area)
        self.lados = lados
    def retornar_lados(self):
        print("Los lados del poligono son:", self.lados)

class Cuadrilatero(Poligono):
    def __init__(self, area):
        Poligono.__init__(self, 4, area)

""" Poligono se deriva de Figura, y Cuadrilatero se deriva de Poligono por lo que
Cuadrilatero tendra los métodos y atributos tanto de las clase Poligono como de la clase
Figura. Si en la clase Poligono alguno de las métodos de Figura es redefinido Cuadrilatero
heredara el método redefinido. """

# Método de resolución de orden en Python

""" Cada clase en Python se deriva de la clase object. En el escenario de herencia múltiple, cualquier atributo especificado se busca primero en la
clase actual. Si no se encuentra, la búsqueda continúa en clases primarias en profundidad, de
izquierda a derecha, sin buscar la misma clase dos veces.
Por lo tanto, en el ejemplo anterior de la clase Cuadrilatero el orden de búsqueda es
[Cuadrilatero, Poligono, Figura, object]. Este orden también se denomina linealización de la
clase Cuadrilatero y el conjunto de reglas que se utiliza para encontrar este orden se denomina
Orden de resolución de métodos, MRO por sus siglas en inglés (Method Resolution Order).
El MRO de una clase puede verse como el atributo __mro__ o el método mro(). El primero
devuelve una tupla mientras que el segundo devuelve una lista. """

class Figura:
    def __init__(self, area):
        self.area = area
    def retornar_area(self):
        print("El área de la figura es:", self.area)

class Poligono(Figura):
    def __init__(self, lados, area):
        Figura.__init__(self, area)
        self.lados = lados
    def retornar_lados(self):
        print("Los lados del poligono son:", self.lados)

class Cuadrilatero(Poligono):
    def __init__(self, area):
        Poligono.__init__(self, 4, area)

print(Cuadrilatero.__mro__)
print(Cuadrilatero.mro())
""" Resultado -> (<class '__main__.Cuadrilatero'>, <class '__main__.Poligono'>, <class
'__main__.Figura'>, <class 'object'>)
[<class '__main__.Cuadrilatero'>, <class '__main__.Poligono'>, <class
'__main__.Figura'>, <class 'object'>] """

# Polimorfismo
""" la capacidad que tienen los objetos de una clase de responder al mismo mensaje o evento en función de los parámetros
utilizados durante su invocación.  """

# Sobrecarga de métodos
""" permite sustituir un método proveniente de la Clase Base, en la Clase Derivada debe definir un método con la
misma forma (es decir, mismo nombre de método y mismo número de parámetros que como
está definido en la Clase Base). """

class Persona():
    def __init__(self, cedula):
        self.cedula = cedula
    def mensaje(self):
        print("Mensaje desde la clase Persona")
class Obrero(Persona):
    def __init__(self, cedula):
        Persona.__init__(self, cedula)
        self.__especialista = 1
    def mensaje(self):
        print("Mensaje desde la clase Obrero")
obrero_planta = Obrero(12345)
obrero_planta.mensaje()
# Resultado -> Mensaje desde la clase Obrero

""" Lo que se logra definiendo el método mensaje() en la Clase Derivada (Obrero) se conoce como
Método Overriding haciendo que cuando se cree el objeto (en este caso obrero_planta) y se
llame al método mensaje(), este será tomado de la propia clase y no de la Clase Base Persona).
Si comenta o borra el método mensaje() de la clase Obrero (Clase Derivada) y corre nuevamente
el código, el método llamado será el mensaje() de la Clase Base Persona. """

# Sobrecarga de Operadores
""" básicamente de lo mismo que la sobrecarga de métodos pero pertenece en esencia al ámbito de
los operadores aritméticos, binarios, de comparación y lógicos. """

class Punto:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return x, y

punto1 = Punto(4,6)
punto2 = Punto(1,-2)
print(punto1 + punto2)
# Resultado -> (5, 4)

# Ejemplo de aplicación de Herencia
""" El inconveniente más evidente de ir sobreescribiendo es que tenemos que volver a escribir el código de la superclase y luego el específico de la subclase.
Para evitarnos escribir código innecesario, podemos utilizar un truco que consiste en llamar el método de la superclase y luego simplemente escribir el código de la clase:
 """
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


c = Coche("azul", 4, 150, 1200)
print(c)

""" Determinar constantemente la superclase puede ser molesto, para facilitarlo Python nos permite utilizar un acceso directo mucho más cómodo llamado super().
Hacerlo de esta forma además nos permite llamar cómodamente los métodos o atributos de la superclase sin necesidad de especificar el self, pero ojo!!, sólo se aconseja utilizarlo cuando tenemos una única superclase:
 """
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

c = Coche("azul", 4, 150, 1200)
print(c)


# POO versus Programación Estructurada
""" Te presentamos dos soluciones, ambas implementan una estructura para gestión de datos de clientes, pero en una se utiliza el enfoque de programación estructurada (la clásica cuyas bases hemos estudiado hasta ahora) y la otra con programación orientada a objetos.
En esta lección solo debes probar ambos códigos (sin necesidad de analizarlos), luego sacar tus propias conclusiones sobre cuál te parece más útil e intuitivo de aplicar y extender en el mundo real.
Arrancamos? """

# Solución en Programación Estructurada
# Definimos unos cuantos clientes

clientes= [
    {'Nombre': 'Hector', 'Apellidos':'Costa Guzman', 'dni':'11111111A'},
    {'Nombre': 'Juan', 'Apellidos':'González Márquez', 'dni':'22222222B'} 
]

# Creamos una función que muestra un cliente en una lista a partir del DNI
def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c['dni']):
            print('{} {}'.format(c['Nombre'],c['Apellidos']))
            return
    print('Cliente no encontrado')

# Creamos una función que borra un cliente en una lista a partir del DNI
def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):
        if (dni == c['dni']):
            del( clientes[i] )
            print(str(c),"> BORRADO")
            return

    print('Cliente no encontrado')    

### Observa muy bien cómo se utiliza el código estructurado

print("==LISTADO DE CLIENTES==")
print(clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
mostrar_cliente(clientes, '11111111A')
mostrar_cliente(clientes, '11111111Z')

print("\n==BORRAR CLIENTES POR DNI==")
borrar_cliente(clientes, '22222222V')
borrar_cliente(clientes, '22222222B')

print("\n==LISTADO DE CLIENTES==")
print(clientes)

#Solución en Programación Orientada a Objetos
### No intentes entender este código, sólo fíjate en cómo se utiliza abajo  

# Creo una estructura para los clientes
class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)

# Y otra para las empresas
class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")

### Ahora utilizaremos ambas estructuras 

# Creemos un par de clientes
hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")

# Creemos una empresa con los clientes iniciales
empresa = Empresa(clientes=[hector, juan])

# Se muestran todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
# Se consulta clientes por DNI
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")

print("\n==BORRAR CLIENTES POR DNI==")
# Se borra un cliente por DNI
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")

# Se muestran de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)


