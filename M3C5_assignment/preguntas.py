print("#################   PREGUNTAS 1  ######################")

"""
What is a conditional in python?
¿Qué es un condicional?

In Python, a conditional is a fundamental concept that allows code to execute differently based on certain conditions.
It helps you make decisions within your program. Let’s explore the different types of conditionals in Python:

En Python, un condicional es un concepto fundamental que permite que el código se ejecute de manera diferente en
función de ciertas condiciones. Le ayuda a tomar decisiones dentro de su programa. Exploremos los diferentes
tipos de condicionales en Python:

1- If Statement:
The simplest form of a conditional is the if statement. It allows you to execute a block of code only if a specified condition is true.

Syntax:

if condition:
	# Statements to execute if condition is true

"""
print('--------------Example:----------------')
x = 3
if x == 4:
    print("Yes")
else:
    print("No")
# Output: No

"""
2- If-Else Statement:
An if-else statement combines an additional block of code (the else block) that is executed when the if condition is false.

Syntax:
if condition:
	# Executes this block if condition is true
else:
	# Executes this block if condition is false

"""
print('--------------Example:----------------')
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

"""
3-Nested If-Else Statement:


A nested if-else statement means an if-else statement inside another if statement. It’s useful for handling multiple conditions.
"""
print('--------------Example:----------------')
letter = "A"
if letter == "B":
    print("letter is B")
else:
    if letter == "C":
        print("letter is C")
    else:
        if letter == "A":
            print("letter is A")
        else:
            print("letter isn't A, B, or C")
# Output: letter is A

"""
4- If-Elif-Else Statement:
The if-elif-else statement allows you to check multiple conditions in sequence. As soon as one condition is true, the associated block is executed.

"""
print('--------------Example:----------------')
letter = "A"

if letter == "B":
    print("letter is B")

elif letter == "C":
    print("letter is C")

elif letter == "A":
    print("letter is A")

else:
    print("letter isn't A, B, or C")
# Output: letter is A


"""

5- Ternary Expression (Conditional Operator):

Certainly! In Python, the ternary operator (also known as the conditional operator) provides a concise way to 
express conditional logic. It allows you to write an if-else statement in a single line of code.

Syntax:
value = true_value if condition else false_value

If the condition evaluates to True, the expression returns value_if_true.
Otherwise, it returns value_if_false.
"""
print('--------------Example:----------------')
a, b = 10, 20

minimum = a if a < b else b

print(minimum)  # Output: 10

print("#################   PREGUNTAS 2  ######################")

"""
¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?
What are the different types of loops in Python? Why are they useful?

Why loops are  useful in python?  ¿Por qué los bucles son útiles en Python?

Loops are a fundamental aspect of programming languages, including Python. They allow you to execute a piece of 
code repeatedly until a specific condition is met. Here’s why loops are useful in Python:
Los bucles son un aspecto fundamental de los lenguajes de programación, incluido Python. 
Le permiten ejecutar una pieza de código repetidamente hasta que se cumpla una condición específica. 
He aquí por qué los bucles son útiles en Python:

Automation and Repetition:
Loops help automate repetitive tasks. 
Instead of writing the same code over and over, you can use loops to perform actions multiple times.
For example, if you want to print numbers from 1 to 10, 
you can use a loop to avoid manually writing print(1), print(2), and so on.

Iterating Over Collections:
Loops allow you to iterate over collections (such as lists, arrays, or dictionaries) and process each item.
For instance, you can loop through a list of names and perform an action for each name.

Processing Data Efficiently:
When dealing with large datasets, loops help process data efficiently.
For example, you can calculate the sum of all elements in an array using a loop.

Types of Loops in Python:

For Loop: 
Used when you want to execute a block of code a fixed number of times. 
You start with an iterable (e.g., a list) and loop through its contents.

While Loop: 
Executes a block of code as long as a specified condition remains true

"""
print('--------------Example 2:----------------')

data = [2, 5, 3, 7]

for element in data:
    print(element)

    # Output: 2, 5, 3, 7

count = 0
while count < 5:
    print("Hello")
    count += 1
# Output: Hello (printed 5 times)


print("#################   PREGUNTAS 3  ######################")

"""
¿Qué es una lista por comprensión en Python?
What is a list by understanding in Python?

In Python, a list is a versatile container that allows you to store and manipulate various pieces of 
information called elements. Imagine it as your digital backpack with compartments for different items.
Here’s what you need to know:

En Python, una lista es un contenedor versátil que le permite almacenar y manipular varias piezas de
 información llamadas elementos. Imagínalo como tu mochila digital con compartimentos para diferentes artículos. 
 Esto es lo que necesitas saber:

Definition:
A Python list is a dynamic, mutable, and ordered collection of elements enclosed within square brackets []. 
These elements can be of different data types, including numbers, strings, booleans, 
and even other lists (creating nested structures).
Definición: Una lista de Python es una colección dinámica, mutable y ordenada de elementos encerrados entre corchetes [] . 
Estos elementos pueden ser de diferentes tipos de datos, incluidos números, cadenas, booleanos e incluso otras listas
(creando estructuras anidadas).


Flexibility: Python lists allow you to rearrange, add, remove, or update elements as needed. 
Whether you’re organizing data, managing tasks, or solving complex problems, lists provide a powerful
 way to store and manipulate information in your Python programs1.
Flexibilidad: Las listas de Python le permiten reorganizar, agregar, eliminar o actualizar elementos 
según sea necesario. Ya sea que esté organizando datos, administrando tareas o resolviendo problemas complejos, 
las listas proporcionan una forma poderosa de almacenar y manipular información en sus programas 1 de Python .


Example:
Suppose you’re planning a trip to the grocery store. You can create a Python list called grocery_list 
to keep track of items you need to buy. Each item, such as “apples,” “bananas,” or “milk,” becomes an element in your list. 
Here’s a simple grocery list in Python:
Ejemplo: Supongamos que estás planeando un viaje al supermercado. 
Puede crear una lista de Python llamada grocery_list para realizar un seguimiento de los artículos que necesita comprar.
 Cada elemento, como "manzanas", "plátanos" o "leche", se convierte en un elemento de la lista. 
 Aquí hay una lista de compras simple en Python:

"""
grocery_list = ["apples", "bananas", "milk"]
print(grocery_list)

print("#################   PREGUNTAS 4  ######################")

"""
¿Qué es un argumento en Python?
 What is an argument in Python?

In Python, an argument is a value that you provide to a function when you call it. 
Let’s explore the different types of arguments in Python:

En Python, un argumento es un valor que se proporciona a una función cuando se la llama. 
Exploremos los diferentes tipos de argumentos en Python:

1--Positional Arguments: Argumentos posicionales:

These are the most common type of arguments.
Estos son los tipos de argumentos más comunes.

They are specified in the order they appear in the function definition.
Se especifican en el orden en que aparecen en la definición de la función.

Example: Ejemplo:
"""


def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)


add_numbers(2, 3)  # Output: Sum: 5
# In this example, add_numbers() takes two positional arguments: a and b.
# En este ejemplo, add_numbers() toma dos argumentos posicionales: a y b .

"""
2--Default Arguments: Argumentos predeterminados:

You can provide default values to function arguments using the = operator.
Puede proporcionar valores predeterminados a los argumentos de función mediante el = operador.

These default values are used if no value is passed during the function call.
Estos valores predeterminados se utilizan si no se pasa ningún valor durante la llamada a la función.

Example: Ejemplo:
"""
def add_numbers(a=7, b=8):
    sum = a + b
    print('Sum:', sum)


add_numbers(2)  # Output: Sum: 10
add_numbers()  # Output: Sum: 15

# Here, a defaults to 7 and b defaults to 8.
# Aquí, a el valor predeterminado es 7 y b el valor predeterminado es 8.

"""
3--Keyword Arguments: Argumentos de palabras clave:

Arguments are assigned based on their names.
Los argumentos se asignan en función de sus nombres.

The order of arguments doesn’t matter.
El orden de los argumentos no importa.

Example: Ejemplo:
"""
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name='Cartman', first_name='Eric')
# Output: First Name: Eric, Last Name: Cartman

"""
4-- Arbitrary Arguments: Argumentos arbitrarios:

Used when you don’t know the number of arguments in advance.
Se utiliza cuando no se conoce el número de argumentos de antemano.

Denoted by an asterisk (*) before the parameter name.
Se indica con un asterisco ( * ) antes del nombre del parámetro.

Example: Ejemplo:
"""
def find_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    print("Sum =", result)

find_sum(1, 2, 3)  # Output: Sum = 6
find_sum(4, 9)     # Output: Sum = 13

#Here, you can pass any number of values to find_sum().
#Aquí, puede pasar cualquier número de valores a find_sum() .

"""
Remember, arguments allow you to customize how a function behaves, making your Python code more flexible and powerful! 
Recuerda, los argumentos te permiten personalizar cómo se comporta una función, lo que hace que tu código Python sea más flexible y potente.
"""

print("#################   PREGUNTAS 5  ######################")

"""
¿Qué es una función Lambda en Python?
 What is a Lambda function in Python?

Lambda
----------------------
Syntax: Sintaxis:

A lambda function can take any number of arguments but only one expression.
Una función lambda puede tomar cualquier número de argumentos, pero solo una expresión.
The syntax is: lambda arguments: expression.   La sintaxis es: lambda arguments: expression .
The expression is executed, and the result is returned.  Se ejecuta la expresión y se devuelve el resultado.
"""
print('--------------Examples Lambda:----------------')

#Adding 10 to an argument a and returning the result:
#Sumando 10 a un argumento a y devolviendo el resultado:

x = lambda a: a + 10
print(x(5))  # Output: 15

#Multiplying a with b and returning the result:
#Multiplicando a y b devolviendo el resultado:

print('--------------Examples Lambda:----------------')

#Multiplying a with b and returning the result:
#Multiplicando a y b devolviendo el resultado:

x = lambda a, b: a * b
print(x(5, 6))  # Output: 30

print('--------------Examples Lambda:----------------')

#Summarizing a, b, and c and returning the result:
#Resumiendo a , b y c devolviendo el resultado:

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))  # Output: 13


print("#################   PREGUNTAS 6  ######################")

"""
What is a PIP package?
¿Qué es un paquete PIP?

pip is the package installer for Python.  pip es el instalador de paquetes para Python

pip is the package installer for Python. It serves as a crucial tool for managing Python libraries and dependencies 
that are not part of the standard library. Here are some key points about pip:

pip es el instalador de paquetes para Python. Sirve como una herramienta crucial para administrar bibliotecas 
y dependencias de Python que no forman parte de la biblioteca estándar. Estos son algunos puntos clave sobre pip:

Purpose: Pip allows you to install, upgrade, and uninstall Python packages. These packages can be obtained 
from various sources, including the Python Package Index (PyPI) and other repositories.
Propósito: Pip le permite instalar, actualizar y desinstalar paquetes de Python. 
Estos paquetes se pueden obtener de varias fuentes, incluido el Python Package Index (PyPI) y otros repositorios.

Origin of the Name: The name pip was introduced by Ian Bicking in 2008.
 It stands for “PIP Installs Packages” and succinctly describes its primary function: installing Python packages.
Origen del nombre: El nombre pip fue introducido por Ian Bicking en 2008. 
Son las siglas de "PIP Installs Packages" y describe sucintamente su función principal: instalar paquetes de Python.

Standard Inclusion: Since Python versions 3.4 and 2.7.9, pip has been included as part of the Python installers. 
This makes it an essential tool for every Python developer.
Inclusión estándar: Desde las versiones 3.4 y 2.7.9 de Python, pip se ha incluido como parte de los instaladores de Python.
Esto lo convierte en una herramienta esencial para todo desarrollador de Python.

Similar to Other Package Managers: If you’ve worked with other programming languages, 
you might be familiar with package managers like npm (for JavaScript), gem (for Ruby), and NuGet (for .NET). 
In Python, pip has become the standard package manager.
Similar a otros administradores de paquetes: si ha trabajado con otros lenguajes de programación, 
es posible que esté familiarizado con administradores de paquetes como npm (para JavaScript), gem (para Ruby) y
 NuGet (para .NET). En Python, pip se ha convertido en el administrador de paquetes estándar.


Using pip: Usando pip

Installing Packages: You can use pip to install packages from PyPI or other repositories. For example, pip install package-name.
Instalación de paquetes: Puede usar pip para instalar paquetes desde PyPI u otros repositorios. Por ejemplo, pip install package-name .

Managing Dependencies: Pip helps you manage project dependencies using requirements files.
Gestión de dependencias: Pip le ayuda a gestionar las dependencias del proyecto mediante archivos de requisitos.

Uninstalling Packages: To remove a package, use pip uninstall package-name.
Desinstalación de paquetes: Para eliminar un paquete, utilice pip uninstall package-name .
"""

#Remember, pip is a powerful tool that simplifies package management in Python,
# making it easier to work with external libraries and extend your Python projects123.

#Recuerde, pip es una poderosa herramienta que simplifica la administración de paquetes en Python,
# lo que facilita el trabajo con bibliotecas externas y la extensión de sus proyectos 1 2 3 de Python .




