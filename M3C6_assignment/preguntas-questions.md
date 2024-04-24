
# PREGUNTAS
 >QUESTIONS



# ¿Para qué usamos Clases en Python?
 >Why do we use classes in Python?
Classes are incredibly useful in Python, serving as the building blocks of object-oriented programming (OOP). Here are some reasons why you might want to use classes:

* Managing State: 
    When you need to keep track of data and behavior together, classes are essential. 
For example, if you’re managing a group of students and their grades or building a game that tracks attempts and scores, 
using a class makes sense1.
Code Organization and Reusability: 
* In larger projects, classes help organize your code and promote reusability.
Consider a Report class: you can have a base class with shared attributes (like report name and location), 
and then create subclasses for specific formats (XML, JSON, HTML). This hierarchy allows for better code 
organization, less duplication, and reusable code. If you have many subclasses and need to make a fundamental 
change, modifying the base class affects all child classes, keeping things DRY (Don’t Repeat Yourself)1.
* Encapsulation: 
Classes allow you to separate internal vs. external interfaces, hiding implementation details. 
This isolation protects your data and provides consumers of your classes with specific access 
rights (similar to API design). Think of it like driving a car without needing to understand its mechanics. 
You interact with the common interface (gas, brake, steering wheel) without knowing how the engine works. 
* Similarly, classes hide complexity and group related data together, making your code more elegant and maintainable1.

* Enforcing Contracts: 
Abstract base classes (ABCs) let you force derived classes to implement certain behaviors. 
By using the abstractmethod decorator in your base class, you ensure that subclasses implement specific methods

>In summary, classes in Python offer benefits such as better organization, encapsulation, 
and reusability, making them a powerful tool for structuring your code

   ``` class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("Guau!")

    perro = Perro("Niebla", "Mastín")
    print(perro.nombre)
    print(perro.raza)
    perro.ladrar()
    
 ```
* En este ejemplo, se define una clase llamada Perro que tiene dos atributos, nombre y raza, y un método, ladrar. Luego se crea un objeto perro a partir de esta clase y se accede a sus atributos y métodos.

    Como se ve, una clase en Python consiste generalmente en las siguientes partes:

    Nombre de la clase: es el nombre que se le da a la clase y que se usa para crear objetos a partir de ella.
Método __init__: es un método especial que se llama automáticamente cuando se crea un objeto a partir de una clase. Este método se usa para inicializar los atributos del objeto. Atributos: son las variables o valores que definen el estado de un objeto.
Métodos: son las funciones que definen el comportamiento de un objeto y que permiten interactuar con otros objetos y realizar tareas específicas.

    Estas son las partes principales de una clase en Python, aunque también existen otras partes como los métodos especiales, las propiedades, los métodos estáticos y las clases anidadas. Sin embargo, la estructura básica de una clase es la descrita anteriormente.





# ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?
 >What method is automatically executed when an instance of a class is created?

* El método __init__ es un método especial (también llamado método dunder) en Python que se utiliza para inicializar una instancia de una clase. Cuando se crea una instancia de una clase, el método __init__ es llamado automáticamente por el intérprete de Python y se utiliza para realizar cualquier inicialización que sea necesaria para la instancia.

* El método __init__ se usa para asignar valores iniciales a los atributos de una instancia de la clase. Los atributos son las variables que pertenecen a una instancia particular de la clase. Al llamar al método __init__, podemos establecer los valores de estos atributos y configurar la instancia de la clase para su uso posterior.

> The method that is automatically executed when an instance of a class is created in Python is the __init__ method12. This special method initializes the data members of a class and is usually the first method inside a class definition. When you create an instance of the class, the __init__ method runs automatically, allowing you to set up initial values and perform any necessary setup tasks

    class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

* En este ejemplo, el método __init__ toma dos parámetros: nombre y edad. Estos se utilizan para inicializar los atributos nombre y edad de la instancia de la clase.

Al crear una instancia de la clase Persona, se debe proporcionar un valor para cada uno de los parámetros nombre y edad, como en el siguiente ejemplo:

    persona1 = persona('Juan', 30)










# ¿Cuáles son los tres verbos de API?
> What are the three API verbs?
> API es el acrónimo de interfaz de programación de aplicaciones (application programming interface en inglés). Es un conjunto de reglas bien definidas que se utilizan para especificar formalmente la comunicación entre dos componentes de software.

En la actualidad existen distintas clases de API, pero en este caso nos enfocaremos un poco más en las API REST (ya que son ellas las que tienen relación con la pregunta).

Una API REST es una interfaz de comunicación entre sistemas de información que usa el protocolo de transferencia de hipertexto (hypertext transfer protocol o HTTP, por su siglas en inglés) para obtener datos o ejecutar operaciones sobre dichos datos en diversos formatos, como pueden ser XML o JSON.
* Los verbos de la API RESTful son acciones estándar utilizadas para realizar operaciones en los recursos dentro de una arquitectura RESTful. Aquí están los tres verbos más comunes:
  - 1- GET: Este verbo recupera una representación de un recurso. Es una operación de solo lectura y no modifica ningún dato en el servidor. Por ejemplo:

    >GET /estudiantes
    
     Esta solicitud recupera una lista de todos los estudiantes.

  - 2- POST: El verbo POST crea un nuevo recurso. Envía datos al servidor para crear una nueva entrada. Por ejemplo:

    >  POST /estudiantes
    
       Esta solicitud crea una nueva entrada de estudiante con los datos proporcionados en el cuerpo de la solicitud.

  - 3- PUT: El verbo PUT actualiza un recurso existente. Reemplaza la representación actual del recurso con los nuevos datos proporcionados. Por ejemplo:

    > PUT /estudiantes/1
    
    Esta solicitud actualiza los datos del estudiante con el ID 1.

    > Además de estos tres, también existen otros verbos como PATCH (que actualiza un recurso existente de manera selectiva) y DELETE (que elimina un recurso existente)







# ¿Es MongoDB una base de datos SQL o NoSQL?
  > Is Mongodb a SQL or Nosql database?

Certainly! Let me explain the differences between SQL and NoSQL databases.

## SQL Databases:
- **Data Storage Model:** SQL databases use a tabular structure with fixed rows and columns.
- **Development History:** They were developed in the 1970s with a focus on reducing data duplication.
- **Examples:** Some popular SQL databases include Oracle, MySQL, Microsoft SQL Server, and PostgreSQL.
- **Primary Purpose:** SQL databases are general-purpose and widely used.
- **Schemas:** They have rigid, complex schemas.
- **Scaling:** SQL databases typically require vertical scaling (upgrading to a larger server).
- **Multi-Record ACID Transactions:** Most SQL databases do not support multi-record ACID transactions.
- **Joins:** SQL databases typically require joins.

## NoSQL Databases:
#### Data Storage Model: NoSQL databases come in various models:
- Document-oriented (e.g., MongoDB, CouchDB)
- Key-value pairs (e.g., Redis, DynamoDB)
- Wide-column (e.g., Cassandra, HBase)
- Graph (e.g., Neo4j, Amazon Neptune)

#### Development History: They were developed in the late 2000s with a focus on scaling and rapid application changes.
#### Benefits:
- Flexible Data Models: NoSQL databases have flexible schemas, allowing easy changes as requirements evolve.
- Horizontal Scaling: They scale horizontally (across commodity servers) rather than vertically.
- Fast Queries: NoSQL databases offer incredibly fast queries.
- Developer-Friendly: They are easy for developers to work with.

#### Drawbacks: 
- Most NoSQL databases do not support multi-record ACID transactions.
#### Data to Object Mapping: 
- Many NoSQL databases do not require ORMs; MongoDB documents map directly to data structures in popular programming languages

  > In summary, SQL databases are well-established and suitable for structured data, while NoSQL databases provide flexibility, scalability, and speed for various use cases. The choice depends on your specific requirements!
  
  >En resumen, las bases de datos SQL son sólidas y adecuadas para datos estructurados, mientras que las bases de datos NoSQL ofrecen flexibilidad, escalabilidad y velocidad para diversos casos de uso. ¡La elección depende de tus requisitos específicos!

  > #### MongoDB es una base de datos NoSQL. ---- MongoDB is a NoSQL database. 






# ¿Qué es una API?

- An API, or Application Programming Interface, is a set of rules or protocols that enables software applications to communicate with each other and exchange data, features, and functionality1. Here are some key points about APIs:
- Una API, o interfaz de programación de aplicaciones, es un conjunto de reglas o protocolos que permiten que las aplicaciones de software se comuniquen entre sí e intercambien datos, características y funcionalidades 1 . Estos son algunos puntos clave sobre las API:

- ### Communication Bridge: 
  - APIs act as a bridge between different software components. They allow applications to request and share information seamlessly.
    ##### Puente de comunicación: 
  - Las API actúan como un puente entre diferentes componentes de software. Permiten que las aplicaciones soliciten y compartan información sin problemas.

- ### Integration: 
  - Developers use APIs to integrate data, services, and capabilities from other applications into their own software. Instead of building everything from scratch, they can leverage existing APIs to enhance their applications.
    ##### Integración: 
  - los desarrolladores utilizan las API para integrar datos, servicios y capacidades de otras aplicaciones en su propio software. En lugar de crear todo desde cero, pueden aprovechar las API existentes para mejorar sus aplicaciones.

    - ### Third-Party Services: 
      - A common example is third-party payment processing. When you make an online purchase and choose to pay with PayPal or another system, APIs facilitate the connection. The buyer’s request triggers an API call to retrieve information, and the server responds with the requested data1.
        ##### Servicios de terceros: 
      - Un ejemplo común es el procesamiento de pagos de terceros. Cuando realiza una compra en línea y elige pagar con PayPal u otro sistema, las API facilitan la conexión. La solicitud del comprador desencadena una llamada a la API para recuperar información y el servidor responde con los datos 1 solicitados.

- ### Security and Privacy: 
  - APIs enable controlled access to resources. They allow sharing only the necessary information while keeping internal system details hidden. This helps maintain system security.
  ##### Seguridad y privacidad: 
  - las API permiten un acceso controlado a los recursos. Permiten compartir solo la información necesaria mientras mantienen ocultos los detalles internos del sistema. Esto ayuda a mantener la seguridad del sistema.

  - ### Documentation: 
    - API documentation provides details for developers on how to work with an API and its services. Well-designed documentation promotes a better API experience and successful integration1.
    ##### Documentación: 
    - la documentación de la API proporciona detalles para los desarrolladores sobre cómo trabajar con una API y sus servicios. Una documentación bien diseñada promueve una mejor experiencia de API y una integración 1 exitosa.

  >  In summary, APIs simplify development, enable integration, offer flexibility, and enhance security in software applications2. If you have any specific questions about APIs, 
  >
  >En resumen, las API simplifican el desarrollo, permiten la integración, ofrecen flexibilidad y mejoran la seguridad en las aplicaciones 2 de software. Si tiene alguna pregunta específica sobre las API,

# ¿Qué es Postman?
![What is POSTMAN?](C:\Users\musta\PycharmProjects\pythonProject2\1_emYNEj5w5MwFVJAgdRyoZQ.png "selam")

- Postman es una aplicación especialmente útil en el desarrollo web y de apps móviles que se comunican con servicios web a través de APIs.
##### Postman qué es y para qué sirve

Postman es una herramienta de colaboración y desarrollo que permite a los desarrolladores interactuar y probar el funcionamiento de servicios web y aplicaciones, proporcionando una interfaz gráfica intuitiva y fácil de usar para enviar solicitudes a servidores web y recibir las respuestas correspondientes.

Con esta plataforma se puede gestionar diferentes entornos de desarrollo, organizar las solicitudes en colecciones y realizar pruebas automatizadas para verificar el comportamiento de los sistemas.

Postman es utilizado por los desarrolladores para testear colecciones y catálogos APIs (tanto a nivel front-end como back-end), para gestionar el ciclo de vida de las APIs, mejorar el trabajo colaborativo y mejorar la organización del proceso de diseño y desarrollo.
#### Cómo funciona Postman

Este entorno ofrece una GUI que facilita a los desarrolladores el envío de solicitudes HTTP y HTTPS a una API y a gestionar las respuestas recibidas.

- ##### Las principales características y funcionalidades de Postman son:

    - Envío de solicitudes. Permite enviar solicitudes GET, POST, PUT, DELETE y otros métodos HTTP a una API especificando los parámetros, encabezados y cuerpo de la solicitud.
    - Gestión de entornos. Facilita la configuración para diferentes entornos (por ejemplo, desarrollo, prueba, producción) y el cambio sencillo entre ellos (para realizar pruebas y desarrollo en diferentes contextos).
    - Colecciones de solicitudes. Agrupa las solicitudes relacionadas en colecciones, lo que facilita la organización y ejecución de pruebas automatizadas.
    - Pruebas automatizadas. Es ideal para crear y ejecutar pruebas automatizadas para verificar el comportamiento de una API (detectar errores e incrementar la calidad del software).
    - Documentación de API. Genera de forma automatizada, documentación detallada de la API a partir de las solicitudes y respuestas realizadas, lo que facilita su comprensión y uso por parte de otros desarrolladores.

    > You can sign up and get started with Postman for free. Additionally, Postman offers paid plans with advanced options and flexibility. If you want to explore real-world use cases, check out the Postman case studies page1. Overall, Postman aims to simplify API development and collaboration, making it easier to create better APIs faster! 
    >
    > Puede registrarse y comenzar a usar Postman de forma gratuita. Además, Postman ofrece planes de pago con opciones avanzadas y flexibilidad. Si desea explorar casos de uso del mundo real, consulte la página 1 de estudios de casos de Postman . En general, Postman tiene como objetivo simplificar el desarrollo y la colaboración de las API, lo que facilita la creación de mejores API más rápido.





# ¿Qué es el polimorfismo?

  - Polymorphism is one of the core concepts in object-oriented programming (OOP). It describes situations in which something occurs in several different forms. 
  - El polimorfismo es uno de los conceptos centrales de la programación orientada a objetos (POO). Describe situaciones en las que algo ocurre de varias formas diferentes. 
  
    - In computer science, polymorphism refers to the concept that you can access objects of different types through the same interface.
    - En informática, el polimorfismo se refiere al concepto de que se puede acceder a objetos de diferentes tipos a través de la misma interfaz.
    - Each type can provide its own independent implementation of this interface.
    - Cada tipo puede proporcionar su propia implementación independiente de esta interfaz.
    - Essentially, polymorphism allows you to treat different objects as if they share a common base, even though they may have distinct behaviors or properties11.
    - Esencialmente, el polimorfismo le permite tratar diferentes objetos como si compartieran una base común, aunque puedan tener comportamientos o propiedades 1 distintas.

   > La palabra "polimorfismo" significa "muchas formas" y en programación se refiere a métodos/funciones/operadores con el mismo nombre que se pueden ejecutar en muchos objetos o clases.

### Polimorfismo de función

- Un ejemplo de una función de Python que se puede utilizar en diferentes objetos es la función len().
String / Cadena

- Para cadenas len() devuelve el número de caracteres:

```
x = "Hello World!"
     print(len(x))
     
- Tuple / Tupla

  -Para tuplas, len() devuelve el número de elementos de la tupla:

mytuple = ("apple", "banana", "cherry")

print(len(mytuple))

  - Dictionary / Diccionario

  - Para diccionarios, len() devuelve el número de pares clave/valor en el diccionario:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))
```

### Class Polymorphism:
- In Python, class methods can exhibit polymorphism. You can have multiple classes with the same method name.
  - For instance, consider three classes: Car, Boat, and Plane. Each has a move() method

```
class Car:
    def move(self):
        print("Drive!")

class Boat:
    def move(self):
        print("Sail!")

class Plane:
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

}
   - Due to polymorphism, we can execute the same move() method for all three classes
```




# ¿Qué es un método dunder?

  - In Python, dunder methods (also known as magic methods) are special methods that allow instances of a class to interact with built-in functions and operators of the language. The term “dunder” comes from “double underscore,” as these methods start and end with two underscores (e.g., __str__ or __add__). Let’s explore some essential dunder methods:


  - En Python, los métodos dunder (también conocidos como métodos mágicos) son métodos especiales que permiten que las instancias de una clase interactúen con funciones y operadores integrados del lenguaje. El término "dunder" proviene de "doble guión bajo", ya que estos métodos comienzan y terminan con dos guiones bajos (por ejemplo, __str__ o __add__ )  . Exploremos algunos métodos esenciales de dunder:

1- **__init__ (Initializer):  
__init__ (Inicializador):**

- The __init__ method is not a constructor (despite often being confused with one). It initializes an object’s attributes when an instance of the class is created.
- El __init__ método no es un constructor (a pesar de que a menudo se confunde con uno). Inicializa los atributos de un objeto cuando se crea una instancia de la clase.
  - It takes arguments (usually self and other parameters) and sets instance variables.
  - Toma argumentos (generalmente self y otros parámetros) y establece variables de instancia.

Example: Ejemplo
```
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)

```

2- **__repr__ (String Representation):
__repr__ (Representación de cadenas):**

- The __repr__ method customizes an object’s string representation.
- El __repr__ método personaliza la representación de cadena de un objeto.


- It’s helpful for debugging and when using the Python REPL.
- Es útil para la depuración y cuando se usa el REPL de Python.

Example: Ejemplo
```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))  # Output: Point(3, 4)

```
3- **__eq__ (Equality):  
__eq__ (Igualdad):**

- The __eq__ method defines what it means for objects to be equal.
- El __eq__ método define lo que significa que los objetos sean iguales.


- It returns True, False, or NotImplemented.
- Devuelve True , False o NotImplemented .

Example: Ejemplo
```
class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

p1 = Person("Alice")
p2 = Person("Alice")
print(p1 == p2)  # Output: True

```
> Remember, dunder methods allow you to customize how your custom classes interact with Python’s features, making your code more expressive and powerful!
>
>Recuerde, los métodos dunder le permiten personalizar la forma en que sus clases personalizadas interactúan con las características de Python, lo que hace que su código sea más expresivo y poderoso.




# ¿Qué es un decorador de python?
- A Python decorator is a powerful concept that allows you to modify or extend the behavior of functions or methods without directly altering their code. Let’s break it down:
- Un decorador de Python es un concepto poderoso que le permite modificar o extender el comportamiento de funciones o métodos sin alterar directamente su código. Vamos a desglosarlo:

######  Los decoradores son una funcionalidad relativamente importante en Python. Se podría decir que son funciones que modifican la funcionalidad de otras funciones, y ayudan a hacer nuestro código más corto y Pythonic. A continuación veremos lo que son, cómo se crean y cómo podemos usarlos.

### Todo es un objeto en Python
- Antes de entrar en materia con los decoradores, vamos a entender bien las funciones.
```
def hola(nombre="Covadonga"):
    return "Hola " + nombre

print(hola())
# Salida: 'Hola Covadonga'


- Podemos ahora asignar una variable a nustra función:

saluda = hola

- Aquello implica lo siguiente:

print(saluda())
Salida: 'Hola Covadonga'

- Es decir, obtenermos el mismo resultado en ambos casos.
```
### Definir funciones dentro de funciones

- En Python podemos definir funciones dentro de otras funciones. Veamos un ejemplo:

```
def hola(nombre="Covadonga"):
    print("Estás dentro de la función hola()")

    def saluda():
        return "Estás dentro de la función saluda()"

    def bienvenida():
        return "Estás dentro de la función bienvenida()"

    print(saluda())
    print(bienvenida())
    print("De vuelta a la función hola()")

hola()

Salida: Estas dentro de la función hola()
        Estás dentro de la función saluda()
        Estás dentro de la función bienvenida()
        De vuelta a la función hola()

- Este ejemplo demuestra que cada vez que llamamos a la función hola(), llamamos también a las funciones saluda() y bienvenida().

- Ahora bien, es importante recalcar que las funciones subyacentes, para llamarlas de algun modo, no son accesibles fuera de la función principal (en este caso hola()). Si intentamos llamar a una, obtendremos un error.

saluda()
Salida: NameError: name 'saluda' is not defined

- Dichas funciones se conocen como funciones anidadas. 
  Pero para entender bien los decoradores, necesitamos ir un paso más allá. 
  Las funciones también pueden devolver otras funciones.
```

### Devolviendo funciones desde funciones

- En el siguiente ejemplo, vemos que no es necesario ejecutar la función que se encuentra dentro de la otra; podemos simplemente devolverla como salida.

```
def hola(nombre="Covadonga"):
    def saluda():
        return "Estás dentro de la función saluda()"

    def bienvenida():
        return "Estás dentro de la función bienvenida()"

    if nombre == "Covadonga":
        return saluda
    else:
        return bienvenida

a = hola()
print(a)

  #Salida: <function hola.<locals>.saluda at 0x000001D2F529A020>

- Ahora bien, en el caso que queramos ejecutar la función subyacente es necesario que que coloquemos paréntesis al final de la función.

print(a())

  #Salida: Estás dentro de la función saluda()

```

### Usando funciones como argumento de otras

- Por último, podemos hacer que una función tenga a otra como entrada y que además la ejecute dentro de sí misma. En el siguiente ejemplo podemos ver como hazEstoAntesDeHola() es una función que de alguna forma encapsula a la función que se le pase como parámetro, añadiendo una determinada funcionalidad. En este ejemplo simplemente imprimimos algo por pantalla antes de llamar a la función.

```
def hola():
    return "¡Hola!"

def hazEstoAntesDeHola(func):
    print("Hacer algo antes de llamar a func")
    print(func())

hazEstoAntesDeHola(hola)

Salida: Hacer algo antes de llamar a func
        ¡Hola!

   - Los decoradores son funciones que decoran a otras funciones, 
   pudiendo ejecutar código antes y después de la función que está siendo 
   decorada.
```

### Primer decorador
```
- En el ejemplo anterior ya vimos cómo crear un decorador. Ahora vamos a modificarlo y hacerlo un poco realista.

def nuevo_decorador(a_func):

    def envuelveLaFuncion():
        print("Haciendo algo antes de llamar a a_func()")

        a_func()

        print("Haciendo algo después de llamar a a_func()")

    return envuelveLaFuncion

def funcion_a_decorar():
    print("Soy la función que necesita ser decorada")

funcion_a_decorar()
Salida: "Soy la función que necesita ser decorada"

funcion_a_decorar = nuevo_decorador(funcion_a_decorar)

funcion_a_decorar()
Salida: Haciendo algo antes de llamar a a_func()
        Soy la función que necesita ser decorada
        Haciendo algo después de llamar a a_func()
```
- Así es exactamente como funcionan los decoradores en Python; envuelven una función para modificar su comportamiento de una manera determinada.

- Ahora bien, a menudo se usa el signo @ en el código. Esto es debido a que @ es simplemente una forma de hacerlo más corto, pero ambas opciones son perfectamente válidas.
```
@nuevo_decorador
def funcion_a_decorar():
    print("Soy la función que necesita ser decorada")

funcion_a_decorar()
Salida: Haciendo algo antes de llamar a a_func()
        Soy la función que necesita ser decorada
        Haciendo algo después de llamar a a_func()
```
- El uso de @nuevo_decorador es simplemente una forma acortada de hacer lo siguiente:

```funcion_a_decorar = nuevo_decorador(funcion_a_decorar)```
























