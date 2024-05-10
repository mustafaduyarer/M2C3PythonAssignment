
# PREGUNTAS
 >QUESTIONS



## ¿Qué tipo de bucles hay en JS?

## ¿Cuáles son las diferencias entre const, let y var?

## ¿Qué es una función de flecha?

## ¿Qué es la deconstrucción de variables?

## ¿Qué hace el operador de extensión en JS?

## ¿Qué es la programación orientada a objetos?

## ¿Qué es una promesa en JS?

## ¿Qué hacen async y await por nosotros?
## -------------------------------------------------------------------------------------

## 1-¿Qué tipo de bucles hay en JS?
> What kind of loops are in JS?

Un bucle en programación se refiere a una estructura de flujo de control que le permite ejecutar repetidamente un conjunto de instrucciones o un bloque de código siempre que se cumpla una condición especificada. Los bucles son fundamentales para el concepto de iteración en la programación, ya que mejoran la eficiencia del código, la legibilidad y promueven la reutilización de la lógica  del código. Estos son los principales tipos de bucles en programación:

> A loop in programming refers to a control flow structure that allows you to repeatedly execute a set of instructions or a code block as long as a specified condition is met. Loops are fundamental to the concept of iteration in programming, enhancing code efficiency, readability, and promoting the reuse of code logic. Here are the main types of loops in programming:

En JavaScript, hay varios tipos de bucles que le permiten ejecutar un bloque de código repetidamente. Vamos a explorarlos:
> In JavaScript, there are several types of loops that allow you to execute a block of code repeatedly. Let’s explore them:

### For Loop: Bucle For:
* The for loop is commonly used for iterating over a sequence of values (such as an array).
  El for bucle se usa comúnmente para iterar sobre una secuencia de valores (como una matriz).
* It has three expressions:
  Tiene tres expresiones:
  - **Initialization** (expression 1): Executed once before the loop starts.
    - Inicialización ( expression 1 ): Se ejecuta una vez antes de que comience el bucle.
  - **Condition** (expression 2): Determines whether the loop should continue.
    - Condición ( expression 2 ): Determina si el bucle debe continuar.
  - **Update** (expression 3): Executed after each iteration.
    - Actualización ( expression 3 ): Se ejecuta después de cada iteración.

#### Example: Ejemplo:
```javascript
for (let i = 0; i < 5; i++) {
    console.log("The number is " + i);
}

//This loop will run from i = 0 to i = 4
//Este bucle se ejecutará de i = 0 a i = 4
```


### While Loop: Bucle while:

* El while bucle ejecuta un bloque de código mientras se cumple una condición especificada.
> The while loop executes a block of code while a specified condition is true.
 


#### Example: Ejemplo:
```javascript
let count = 0;
while (count < 5) {
    console.log("Count: " + count);
    count++;
}

```

### Do…while Loop: Do... while Bucle

* Similar al while bucle, pero siempre ejecuta el bloque de código al menos una vez, incluso si la condición es falsa inicialmente.
> Similar to the while loop, but it always executes the code block at least once, even if the condition is false initially.
 

#### Example: Ejemplo:
```javascript
let num = 0;
do {
    console.log("Number: " + num);
    num++;
} while (num < 5);

```
### For/In Loop: For/En bucle

* Se utiliza para iterar sobre las propiedades de un objeto.
> Used to iterate over the properties of an object.
 

#### Example: Ejemplo:
```javascript
const person = { name: "Alice", age: 30 };
for (const key in person) {
    console.log(key + ": " + person[key]);
}


```
### For/Of Loop: Bucle For/Of

* Itera sobre los valores de un objeto iterable (por ejemplo, matrices, cadenas, mapas, conjuntos).
>Iterates over the values of an iterable object (e.g., arrays, strings, maps, sets).
 

#### Example: Ejemplo:
```javascript
const colors = ["red", "green", "blue"];
for (const color of colors) {
    console.log("Color: " + color);
}
```

### forEach loop: Bucle forEach

* Este método entra dentro del grupo de Iterables sin devolver una nueva matriz, lo que hace el forEach es ejecutar una función por cada elemento del array. En cada iteración se tendrá acceso a 3 variables: valor (del elemento), índice (del elemento) y array (que estamos recorriendo) y con ello la función que se ejecutará para cada elemento de una matriz.
  * Este método es muy útil cuando solo necesitamos ejecutar una función a través de cada elemento del array, sin necesidad de obtener un retorno. El forEach() también se puede utilizar en mapas y conjuntos.
>This method enters the group of Iterables without returning a new array, what forEach does is execute a function for each element of the array. In each iteration we will have access to 3 variables: value (of the element), index (of the element) and array (which we are going through) and with it the function that will be executed for each element of an array.
>> This method is very useful when we only need to execute a function through each element of the array, without needing to obtain a return. The forEach() can also be used on maps and sets.
 

#### Example: Ejemplo:
```javascript
let students = ['John', 'Sara', 'Jack'];

// using forEach
students.forEach(myFunction);

function myFunction(item) {

    console.log(item);
}

// salida
/* John
   Sara
   Jack */
```
> Recuerda, cada tipo de bucle sirve para diferentes propósitos, ¡así que elige el que mejor se adapte a tu tarea específica! Si tiene más preguntas, 

> Remember, each type of loop serves different purposes, so choose the one that best fits your specific task! If you have any more questions, 

#### -------------------------------------------------------------------------------------------------------------------------------------------------

## 2- ¿Cuáles son las diferencias entre const, let y var?
> What are the differences between const, let and var?
> 
- Certainly! Let’s explore the differences between var, let, and const in JavaScript:
- ¡Ciertamente! Exploremos las diferencias entre var , let y const en JavaScript:


## var 
* **Scope:** Variables declared with var are globally scoped or function-scoped.
* **Ámbito:** las variables declaradas con var tienen un ámbito global o un ámbito de función.

  - If declared outside a function, they are available for use throughout the entire window.
  - Si se declaran fuera de una función, están disponibles para su uso en toda la ventana.
- 
  - If declared within a function, they are accessible only within that function.
  - Si se declaran dentro de una función, solo se puede acceder a ellos dentro de esa función.

* **Hoisting**: var variables are hoisted to the top of their scope and initialized with a value of undefined.
* **Elevación:** var las variables se elevan a la parte superior de su ámbito y se inicializan con un valor de undefined
####
* **Re-declaration and Updates:** You can re-declare and update var variables within their scope.
* **Redeclaración y actualizaciones:** puede volver a declarar y actualizar var variables dentro de su ámbito.

#### Example: Ejemplo:
```javascript
var greeter = "hey hi";
var greeter = "say Hello instead"; // No error

```
## let 
* **Scope:** Variables declared with let are block-scoped (limited to the nearest enclosing curly braces { ... }).
* **Ámbito:** las variables declaradas con let ámbito de bloque (limitadas a las llaves { ... } envolventes más cercanas).
####
* **Hoisting**: Like var, let variables are also hoisted, but they are not initialized until the actual declaration is encountered.
* **Elevación:** Al igual var que , let las variables también se elevan, pero no se inicializan hasta que se encuentra la declaración real.
####
* **Re-declaration and Updates:** You can update let variables within their scope, but you cannot re-declare them
* **Redeclaración y actualizaciones:** puede actualizar let las variables dentro de su ámbito, pero no puede volver a declararlas.

#### Example: Ejemplo:
```javascript
let greeting = "hello";
greeting = "hi"; // Valid
let greeting = "hey"; // Error: Identifier 'greeting' has already been declared

```

## const 
* **Scope:** Variables declared with const are also block-scoped.
* **Ámbito:** las variables declaradas con const también tienen ámbito de bloque.
####
* **Hoisting**: Like let, const variables are hoisted but not initialized until the actual declaration.
* **Elevación:** Al igual let que , const las variables se elevan pero no se inicializan hasta la declaración real.
####
* **Re-declaration and Updates:** You cannot re-declare or update const variables after their initial assignment
* **Redeclaración y actualizaciones:** no se pueden volver a declarar ni actualizar const variables después de su asignación inicial.

#### Example: Ejemplo:
```javascript
const pi = 3.14;
pi = 3.14159; // Error: Assignment to constant variable

```
In summary: En resumen:

- Use var when you want global or function-scoped variables.
  > Utilícelo var cuando desee variables globales o de ámbito de función.
- Use let when a variable’s value may change over time.
  >Se usa let cuando el valor de una variable puede cambiar con el tiempo.
- Use const for variables that should remain constant after their initial assignment.
  >Se usa const para variables que deben permanecer constantes después de su asignación inicial.

>Remember, avoiding var is recommended due to its potential issues, and using let and const provides better scoping and clarity in your code.
> 
> Recuerde que se recomienda evitarlo var debido a sus posibles problemas, y el uso let y const proporciona un mejor alcance y claridad en su código

![varLetConst.png](..%2FImages%2FvarLetConst.png)



## 3- ¿Qué es una función de flecha?
> What is an arrow function?
> 

###### Una función de flecha en JavaScript es una forma concisa de escribir funciones. Se introdujo en ECMAScript 6 (ES6) y proporciona una sintaxis más compacta para definir funciones. Estos son algunos puntos clave sobre las funciones de flecha:

###### An arrow function in JavaScript is a concise way of writing functions. It was introduced in ECMAScript 6 (ES6) and provides a more compact syntax for defining functions. Here are some key points about arrow functions:

## Syntax: Sintaxis:
* Arrow functions use the => syntax.
> Las funciones de flecha utilizan la => sintaxis.
####
* They are often assigned to variables, making them anonymous functions.
> A menudo se asignan a variables, lo que las convierte en funciones anónimas.
####

#### Example: Ejemplo:
```javascript
// Regular function
let add = function(a, b) {
    return a + b;
};

// Arrow function
let addArrow = (a, b) => a + b;

```


## Shorter Syntax: Sintaxis más corta:
* If an arrow function has only one statement, you can omit the curly braces {} and the return keyword.
> Si una función de flecha solo tiene una instrucción, puede omitir las llaves {} y la return palabra clave.


#### Example: Ejemplo:
```javascript
// Regular function
let greet = function() {
    return "Hello World!";
};

// Arrow function (shorter)
let greetArrow = () => "Hello World!";

```
## Parameters: Parámetros:
* If the function takes parameters, they are enclosed in parentheses.
> Si la función toma parámetros, se encierran entre paréntesis.


#### Example: Ejemplo:
```javascript
// Arrow function with parameters
let greetWithName = (name) => "Hello " + name;

```


## this Keyword Behavior:
## this Comportamiento de las palabras clave:
* Arrow functions behave differently from regular functions regarding the this keyword.
> Las funciones de flecha se comportan de manera diferente a las funciones normales con respecto a la this palabra clave.
####
* In regular functions, this represents the object that calls the function.
> En funciones regulares, this representa el objeto que llama a la función.
####
* In arrow functions, this always represents the object that defined the arrow function.
> En las funciones de flecha, this siempre representa el objeto que definió la función de flecha.
####

#### Example: Ejemplo:
```javascript
// Regular function
let regularFunc = function() {
    console.log(this); // Represents the caller (window or button)
};

// Arrow function
let arrowFunc = () => {
    console.log(this); // Represents the owner of the function (window)
};

```


## Browser Support: Compatibilidad con navegadores
* Arrow functions are supported in modern browsers (e.g., Chrome, Firefox, Safari).
> Las funciones de flecha son compatibles con los navegadores modernos (por ejemplo, Chrome, Firefox, Safari).


#### How to Convert a Regular Function to an Arrow Function Easily
You can follow these three easy steps to convert a regular function to an arrow function:

    1-Replace the function keyword with the variable keyword const
    2-Add the = symbol after the function name and before the parentheses
    3-Add the => symbol after the parentheses

Usually, a function is never changed after the declaration, so we use the const keyword instead of let.

The code below should help you visualize the steps:

```javascript
function greetings(name) {
  return `Hello, ${name}!`;
}

// step 1: replace function with const
const greetings(name) {
  return `Hello, ${name}!`;
}

// step 2: add = after the function name
const greetings = (name) {
  return `Hello, ${name}!`;
}

// step 3: add => after the parentheses
const greetings = (name) => {
  return `Hello, ${name}!`;
}


```

The three steps above are enough to convert any old JavaScript function syntax to the new arrow function syntax.

> When you have a single line function, there’s a fourth optional step to remove the curly brackets and the return keyword as follows:

```javascript
// from this
const greetings = (name) => {
  return `Hello, ${name}!`;
};

// to this
const greetings = (name) => `Hello, ${name}!`;


```
> When you have exactly one parameter, you can also remove the parentheses:

```javascript
// from this
const greetings = (name) => `Hello, ${name}!`;

// to this
const greetings = name => `Hello, ${name}!`;


```

> In summary, arrow functions provide a more concise syntax for writing functions, but their behavior with this differs from regular functions. Use them when appropriate for cleaner code! 
>
> En resumen, las funciones de flecha proporcionan una sintaxis más concisa para escribir funciones, pero su comportamiento difiere this del de las funciones normales. ¡Úselos cuando sea apropiado para un código más limpio! 

#### -------------------------------------------------------------------------------------------------------

## 4-¿Qué es la deconstrucción de variables?
> 4- What is the deconstruction of variables?

* The deconstruction of variables, also known as destructuring assignment, is a powerful feature in programming languages that allows you to unpack values from arrays or properties from objects into distinct variables. Let’s explore how it works in different contexts:
* La deconstrucción de variables, también conocida como asignación de desestructuración, es una característica poderosa en los lenguajes de programación que le permite desempaquetar valores de matrices o propiedades de objetos en variables distintas. Exploremos cómo funciona en diferentes contextos:

#### * Array Destructuring (in JavaScript):
Desestructuración de matrices (en JavaScript):
* You can extract values from an array and assign them to individual variables.
> Puede extraer valores de una matriz y asignarlos a variables individuales.

#### Syntax example: Ejemplo de sintaxis
```javascript
const x = [1, 2, 3, 4, 5];
const [y, z] = x;
console.log(y); // 1
console.log(z); // 2

In this example, y gets the value 1, and z gets the value 2.
En este ejemplo, y obtiene el valor 1 , y z obtiene el valor 2 .
```

#### * Object Destructuring (also in JavaScript):
Desestructuración de objetos (también en JavaScript):
* You can extract properties from an object and assign them to variables.
> Puede extraer propiedades de un objeto y asignarlas a variables.

#### Syntax example: Ejemplo de sintaxis
```javascript
const obj = { a: 1, b: 2 };
const { a, b } = obj;
// Equivalent to:
// const a = obj.a;
// const b = obj.b;

Here, a gets the value 1, and b gets the value 2.
Aquí, a obtiene el valor 1 , y b obtiene el valor 2 .
```

#### * Advanced Object Destructuring:
Desestructuración avanzada de objetos:
* You can also destructure nested objects and rename properties.
> También puede desestructurar objetos anidados y cambiar el nombre de las propiedades.

#### Syntax example: Ejemplo de sintaxis
```javascript
const obj = { a: 1, b: { c: 2 } };
const { a, b: { c: d } } = obj;
// Two variables are bound: `a` and `d`

In this case, a gets the value 1, and d gets the value 2.
En este caso, a obtiene el valor 1 , y d obtiene el valor 2 .
```
> Remember that destructuring can make your code more concise and expressive, especially when working with complex data structures!
> 
>Recuerde que la desestructuración puede hacer que su código sea más conciso y expresivo, ¡especialmente cuando trabaja con estructuras de datos complejas! 

#### -------------------------------------------------------------------------------------------------------

## 5- ¿Qué hace el operador de extensión en JS?
> What does the extension operator do in JS?

> El operador de extensión en JavaScript se llama en realidad la extends palabra clave. Se utiliza en declaraciones de clase o expresiones de clase para crear una clase que es un elemento secundario de otra clase 1 . Así es como funciona:
> 
The extension operator in JavaScript is actually called the extends keyword. It is used in class declarations or class expressions to create a class that is a child of another class1. Here’s how it works:

#### Subclassing with extends: Subclases con extends :
>Puede usarlo extends para crear una nueva clase que herede de una clase existente (la clase principal). La nueva clase se denomina subclase y la clase existente es la clase principal.

You can use extends to create a new class that inherits from an existing class (the parent class). The new class is called a subclass, and the existing class is the parent class.

#### Syntax example: Ejemplo de sintaxis
```javascript
class ChildClass extends ParentClass {
    // Additional properties and methods for ChildClass
}

```
* El ChildClass hereda todas las propiedades y métodos de ParentClass .
  - The ChildClass inherits all properties and methods from ParentClass.

* También puede crear subclases de objetos integrados mediante extends .
   - You can also subclass built-in objects using extends.

####  Conditions for Parent Class: Condiciones para la clase principal:
>La clase primaria debe ser una función constructora (incluida una clase) o null .

The parent class must be a constructor function (including a class) or null.

>La propiedad prototype de la clase primaria debe ser un objeto o null .

The prototype property of the parent class must be an object or null.

####  example: Ejemplo 
```javascript
function OldStyleClass() {
    this.someProperty = 1;
}
OldStyleClass.prototype.someMethod = function () {};

class ChildClass extends OldStyleClass {}

class ModernClass {
    someProperty = 1;
    someMethod() {}
}
class AnotherChildClass extends ModernClass {}


```
#### Static and Instance Inheritance: Herencia estática y de instancias:
>Extends Permite la herencia de propiedades estáticas (nivel de clase) e instancias (nivel de objeto).

Extends allows inheritance of both static (class-level) and instance (object-level) properties.

####  example: Ejemplo 
```javascript
Object.getPrototypeOf(ChildClass) === ParentClass; // Allows inheritance of static properties
Object.getPrototypeOf(ChildClass.prototype) === ParentClass.prototype; // Allows inheritance of instance properties

```


#### Expression as the Right-Hand Side: Expresión como el lado derecho:
>El lado derecho de extends no tiene que ser un identificador. Puede usar cualquier expresión que se evalúe como un constructor (útil para mezclas).

The right-hand side of extends doesn’t have to be an identifier. You can use any expression that evaluates to a constructor (useful for mixins).

####  example: Ejemplo 
```javascript
class SomeClass extends class {
    constructor() {
        console.log("Base class");
    }
} {
    constructor() {
        super();
        console.log("Derived class");
    }
}
new SomeClass(); // Output: "Base class" followed by "Derived class"

```
#### Return Value from Constructors: Valor devuelto por los constructores:
>Mientras que el constructor de la clase base puede devolver cualquier cosa, el constructor de la clase derivada debe devolver un objeto o undefined . De lo contrario, se lanzará a TypeError .

While the base class constructor can return anything, the derived class constructor must return an object or undefined. Otherwise, a TypeError will be thrown.
####  example: Ejemplo 
```javascript
class SomeClass extends class {
    constructor() {
        console.log("Base class");
    }
} {
    constructor() {
        super();
        console.log("Derived class");
    }
}
new SomeClass(); // Output: "Base class" followed by "Derived class"

```
>En resumen, la extends palabra clave permite crear jerarquías de clases y establecer relaciones de herencia en JavaScript. ¡Es una poderosa herramienta para crear código modular y reutilizable! 
>
> In summary, the extends keyword allows you to create class hierarchies and establish inheritance relationships in JavaScript. It’s a powerful tool for building modular and reusable code! 

#### -------------------------------------------------------------------------------------------------------


## 6-¿Qué es la programación orientada a objetos?
> 6- What is object -oriented programming?

> La programación orientada a objetos (POO) es un paradigma de programación fundamental utilizado por casi todos los desarrolladores en algún momento de su carrera. Es el paradigma de programación más popular para el desarrollo de software y se enseña como la forma estándar de codificar durante la mayor parte de la carrera  educativa de un programador. Analicemos los conceptos básicos de la POO:

Object-oriented programming (OOP) is a fundamental programming paradigm used by nearly every developer at some point in their career. It’s the most popular programming paradigm for software development and is taught as the standard way to code for most of a programmer’s educational career. Let’s break down the basics of OOP:

#### Concepto de Clases y Objetos: -  Concept of Classes and Objects:

* La POO se basa en el concepto de clases y objetos.
  - OOP relies on the concept of classes and objects.

* Una clase es un plano abstracto que define la estructura y el comportamiento de los objetos. Representa una categoría de objetos con atributos y métodos compartidos.
  - A class is an abstract blueprint that defines the structure and behavior of objects. It represents a category of objects with shared attributes and methods.

* Un objeto es una instancia de una clase. Es una realización concreta del plano de clase, con valores específicos para sus atributos.
  - An object is an instance of a class. It’s a concrete realization of the class blueprint, with specific values for its attributes.

* Por ejemplo, considere una clase llamada "Coche". La clase define atributos como el color, la marca y el modelo. Un objeto de tipo "Car" (por ejemplo, myCar) tendría valores específicos para estos atributos.
  - For example, consider a class called “Car.” The class defines attributes like color, brand, and model. An object of type “Car” (e.g., myCar) would have specific values for these attributes.

#### Atributos y métodos: - Attributes and Methods: 

**Atributos:**
Representan los datos asociados a un objeto. En nuestro ejemplo de "Coche", el color, la marca y el modelo son atributos.

**Attributes:**
These represent the data associated with an object. In our “Car” example, color, brand, and model are attributes.

**Métodos:**
Son funciones definidas dentro de una clase. Realizan acciones relacionadas con el tipo de objeto específico. Por ejemplo, un método de "repintado" en la clase Car podría cambiar el atributo de color de un coche

**Methods:**
These are functions defined within a class. They perform actions related to the specific object type. For instance, a “repaint” method in the Car class could change the color attribute of a car

#### Plantillas e instancias de clase: -  Class Templates and Instances:

* Una clase sirve como modelo para crear objetos individuales.
  - A class serves as a blueprint for creating individual objects.

* Cuando creamos una instancia de una clase (por ejemplo, myCar), representa un objeto específico con valores únicos para las propiedades definidas en la clase.
  - When we create an instance of a class (e.g., myCar), it represents a specific object with unique values for the properties defined in the class.

* Podemos reutilizar la misma clase para representar cualquier número de objetos similares (por ejemplo, otros coches).
  - We can reuse the same class to represent any number of similar objects (e.g., other cars).

>En resumen, la POO permite a los desarrolladores estructurar el software en piezas de código reutilizables (clases) que crean instancias individuales (objetos) con atributos y comportamientos específicos. Simplifica el desarrollo de software al modelar conceptos del mundo real de una manera 2 más intuitiva. Si está interesado en obtener más información, explore lenguajes como JavaScript, C++, Java o Python, que admiten los principios 1 de programación orientada a objetos. 
>
>In summary, OOP allows developers to structure software into reusable pieces of code (classes) that create individual instances (objects) with specific attributes and behaviors. It simplifies software development by modeling real-world concepts in a more intuitive way2. If you’re interested in learning more, explore languages like JavaScript, C++, Java, or Python, which support OOP principles1. 

#### ¿Cuáles son los principios fundamentales de la POO?
What are the main principles of OOP?

* ¡Ciertamente! Los principios fundamentales de la Programación Orientada a Objetos (POO) son conceptos esenciales que guían el diseño y la implementación de software utilizando un enfoque orientado a objetos. Exploremos estos principios:
   - Certainly! The main principles of Object-Oriented Programming (OOP) are essential concepts that guide the design and implementation of software using an object-oriented approach. Let’s explore these principles:

#### Encapsulación  - Encapsulation
* La encapsulación se refiere a la agrupación de datos (atributos) y métodos (funciones) que operan sobre esos datos en una sola unidad llamada clase.
> Encapsulation refers to bundling data (attributes) and methods (functions) that operate on that data into a single unit called a class.

* La clase oculta los detalles internos de su implementación, exponiendo solo una interfaz bien definida (métodos públicos) para interactuar con el mundo exterior.
> The class hides the internal details of its implementation, exposing only a well-defined interface (public methods) to interact with the outside world.

* La encapsulación garantiza la integridad, la seguridad y la modularidad de los datos.
> Encapsulation ensures data integrity, security, and modularity.

#### Abstracción  - Abstraction
* La abstracción se centra en simplificar sistemas complejos dividiéndolos en partes más pequeñas y manejables
> Abstraction focuses on simplifying complex systems by breaking them down into smaller, more manageable parts.

* En POO, la abstracción se logra a través de clases e interfaces.
> In OOP, abstraction is achieved through classes and interfaces.

* Las clases abstractas definen propiedades y métodos comunes que las subclases pueden heredar y ampliar.
> Abstract classes define common properties and methods that subclasses can inherit and extend.

* Las interfaces definen un contrato al que deben adherirse las clases, especificando las firmas de método sin detalles de implementación.
> Interfaces define a contract that classes must adhere to, specifying method signatures without implementation details.

#### Herencia  - Inheritance

* La herencia permite que una nueva clase (denominada subclase o clase derivada) herede propiedades y comportamientos de una clase existente (denominada clase base o clase primaria).
> Inheritance allows a new class (called a subclass or derived class) to inherit properties and behaviors from an existing class (called a base class or parent class).

* Promueve la reutilización del código y establece una relación "es-a" entre las clases.
> It promotes code reuse and establishes an “is-a” relationship between classes.

* Por ejemplo, una clase "Dog" puede heredar de una clase "Animal" más general.
> For example, a “Dog” class can inherit from a more general “Animal” class.

#### Polimorfismo  - Polymorphism
* Polimorfismo significa "muchas formas".
> Polymorphism means “many forms.”

* Permite que los objetos de diferentes clases se traten de manera uniforme a través de una interfaz común.
> It allows objects of different classes to be treated uniformly through a common interface.

* El polimorfismo se puede lograr mediante la anulación de métodos (cambiar el comportamiento de los métodos heredados) y la sobrecarga de métodos (definir varios métodos con el mismo nombre pero diferentes parámetros).
> Polymorphism can be achieved through method overriding (changing the behavior of inherited methods) and method overloading (defining multiple methods with the same name but different parameters).

> En resumen, los principios de POO proporcionan una forma estructurada de modelar entidades del mundo real, promover la reutilización del código y mejorar la capacidad de mantenimiento del software. Al comprender y aplicar estos principios, los desarrolladores pueden crear sistemas de software sólidos, flexibles y eficientes.
> 
> In summary, OOP principles provide a structured way to model real-world entities, promote code reusability, and enhance software maintainability. By understanding and applying these principles, developers can create robust, flexible, and efficient software systems. 


## 7-¿Qué es una promesa en JS?
> 7- What is a promise in JS?

* En JavaScript, una promesa es un objeto especial que representa la finalización final (o el error) de una operación asincrónica y su valor resultante. Déjame desglosártelo:
---
* In JavaScript, a promise is a special object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value. Let me break it down for you:

**Operación asincrónica:**  **Asynchronous Operation:**
- cuando se realiza una acción que tarda algún tiempo en completarse (como la obtención de datos de un servidor, la lectura de un archivo o la espera de una entrada del usuario), se considera asincrónica. En lugar de bloquear la ejecución de su código, JavaScript le permite continuar con otras tareas mientras espera el resultado de esa operación.

- When you perform an action that takes some time to complete (like fetching data from a server, reading a file, or waiting for a user input), it’s considered asynchronous. Instead of blocking the execution of your code, JavaScript allows you to continue with other tasks while waiting for the result of that operation.

**Creación de promesas:**  **Promise Creation:**
- Una promesa actúa como marcador de posición para el valor que estará disponible una vez que finalice la operación asincrónica. Se crea una promesa mediante el Promise constructor. He aquí un ejemplo básico:
- A promise acts as a placeholder for the value that will be available once the asynchronous operation finishes. You create a promise using the Promise constructor. Here’s a basic example:

####  Example: Ejemplo 
```javascript
const myPromise = new Promise((resolve, reject) => {
  // Asynchronous operation (e.g., fetching data)
  // If successful, call resolve(value)
  // If there's an error, call reject(error)
});
w SomeClass(); // Output: "Base class" followed by "Derived class"

```
**Estados de una promesa:**    **States of a Promise:** 
**Pendiente:** el estado inicial cuando se crea la promesa. Ni se cumple ni se rechaza.
**Pending:** The initial state when the promise is created. It’s neither fulfilled nor rejected.

**Cumplido:** la operación se ha completado correctamente y la promesa tiene un valor.
**Fulfilled:** The operation completed successfully, and the promise has a value.

**Rechazada:** se produjo un error en la operación y la promesa tiene un motivo de error.
**Rejected:** The operation failed, and the promise has an error reason.

### **Manejadores y encadenamientos:**  **Handlers and Chaining:**
* Puede asociar controladores (devoluciones de llamada) a una promesa mediante el .then() método. Se llama a estos controladores cuando se cumple o se rechaza la promesa.
   - You can associate handlers (callbacks) with a promise using the .then() method. These handlers are called when the promise is either fulfilled or rejected.

* Las promesas le permiten encadenar operaciones asincrónicas. Cada uno .then() devuelve una nueva promesa, lo que le permite controlar el resultado de la operación anterior.
   - Promises allow you to chain asynchronous operations together. Each .then() returns a new promise, allowing you to handle the result of the previous operation.

####  Example: Ejemplo 
```javascript
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // Simulating fetching data
      const data = { id: 1, name: 'John' };
      resolve(data); // Fulfilled with the data
    }, 1000);
  });
}

fetchData()
  .then((result) => {
    console.log('Data received:', result);
    // You can return another promise here
    return fetchMoreData();
  })
  .then((moreData) => {
    console.log('More data received:', moreData);
  })
  .catch((error) => {
    console.error('Error fetching data:', error);
  });

```
> Remember, promises make handling asynchronous code more manageable and avoid callback hell. They allow you to write cleaner, more readable code while ensuring proper error handling. 
>
> Recuerde que las promesas hacen que el manejo de código asincrónico sea más manejable y evitan el infierno de las devoluciones de llamada. Le permiten escribir código más limpio y legible al tiempo que garantizan un manejo adecuado de los errores. 

## 8- ¿Qué hacen async y await por nosotros?
> What do Async and Await for us?

* Async/await es una característica eficaz de JavaScript que le permite trabajar con promesas de una manera más cómoda y sincrónica. Vamos a desglosarlo:
  * Async/await is a powerful feature in JavaScript that allows you to work with promises in a more comfortable and synchronous-like fashion. Let’s break it down:

### Funciones asíncronas:   -  Async Functions: 
###### * Una función asincrónica se define mediante la palabra clave antes de una declaración o expresión de async función.
      - An async function is defined using the async keyword before a function declaration or expression.

###### * Cuando marca una función como async , siempre devuelve una promesa. Si la función devuelve explícitamente un valor que no es de promesa, se encapsula automáticamente en una promesa resuelta.
      - When you mark a function as async, it always returns a promise. If the function explicitly returns a non-promise value, it is automatically wrapped in a resolved promise.
####  Example: Ejemplo 
```javascript
async function f() {
    return 1;
}
Here, f() returns a resolved promise with the value 1.
Aquí, f() devuelve una promesa resuelta con el valor 1 .

```

### Esperar:  -  Await: 

###### * La await palabra clave solo se puede usar dentro de funciones asincrónicas.
      - The await keyword can only be used inside async functions.

###### * Hace que JavaScript espere hasta que una promesa se liquide (ya sea se resuelva o se rechace) y luego devuelve su resultado.
      - It makes JavaScript wait until a promise settles (either resolves or rejects) and then returns its result.

####  The syntax is: La sintaxis es:
```javascript
let value = await promise;


```
####  Here’s an example: He aquí un ejemplo:

```javascript
async function f() {
    let promise = new Promise((resolve, reject) => {
        setTimeout(() => resolve("done!"), 1000);
    });
    let result = await promise;
    alert(result); // "done!"
}
f();

//En este ejemplo, la ejecución de la función se detiene en la await línea y se reanuda cuando se liquida la promesa (después de 1 segundo en este caso).
//In this example, the function execution pauses at the await line and resumes when the promise settles (after 1 second in this case).
```

### Beneficios de Await -  Benefits of Await: 

###### * El uso await es más elegante que el encadenamiento de .then() llamadas para controlar los resultados prometidos.
      - Using await is more elegant than chaining .then() calls for handling promise results.

###### * Hace que el código asincrónico sea más fácil de leer y escribir.
      - It makes asynchronous code easier to read and write.

###### * Es importante destacar que, mientras la función espera a que se liquide la promesa, el motor de JavaScript puede realizar otras tareas (como ejecutar otros scripts o controlar eventos) sin consumir recursos adicionales de la CPU.
      - Importantly, while the function is waiting for the promise to settle, the JavaScript engine can perform other tasks (such as executing other scripts or handling events) without consuming additional CPU resources.


### Limitaciones: - Limitations: 


###### * No se puede usar await fuera de una función asincrónica. Si intenta hacerlo, se producirá un error de sintaxis.
      - You cannot use await outside of an async function. Attempting to do so will result in a syntax error.

###### * Por ejemplo, el código siguiente produciría un error:
      - For example, the following code would throw an error:

```javascript
function f() {
    let promise = Promise.resolve(1);
    let result = await promise; // Syntax error
}

```
####  Example with Fetch API and Async/Await:  -  Ejemplo con Fetch API y Async/Await:

```javascript
//Supongamos que desea obtener datos de usuario de un archivo JSON y, a continuación, recuperar el avatar de GitHub del usuario:
// Suppose you want to fetch user data from a JSON file and then retrieve the user’s GitHub avatar:

async function showAvatar() {
    // Read user data from JSON
    let response = await fetch('/article/promise-chaining/user.json');
    let user = await response.json();

    // Fetch GitHub user data
    let githubResponse = await fetch(`https://api.github.com/users/${user.name}`);
    let githubUser = await githubResponse.json();

    // Display the avatar
    let img = document.createElement('img');
    img.src = githubUser.avatar_url;
    img.className = "promise-avatar-example";
    document.body.append(img);

    // Wait for 3 seconds
    await new Promise((resolve, reject) => setTimeout(resolve, 3000));
}

// Call the function
showAvatar();

//En este ejemplo, usamos await para manejar las promesas devueltas por fetch() y response.json() , haciendo que el código sea más legible y conciso 
//In this example, we use await to handle promises returned by fetch() and response.json(), making the code more readable and concise1.

```

> Recuerde que async/await simplifica el trabajo con código asincrónico, lo que facilita la administración de promesas y el control de sus resultados.
>
>> Remember that async/await simplifies working with asynchronous code, making it easier to manage promises and handle their results. 



## Promise basics explained using my birthday

![varLetConst.png](..%2FImages%2FasyncWait.png)

My friend Kayo promises to make a cake for my birthday in two weeks.
- Mi amiga Kayo promete hacer un pastel para mi cumpleaños en dos semanas.

If everything goes well and Kayo doesn't get sick, we'll have a certain number of cakes. (Cakes are a countable in this tutorial ). Otherwise, if Kayo gets sick, we'll have no cakes.
 - Si todo va bien y Kayo no se enferma, tendremos un cierto número de pasteles. (Los pasteles son un contable en este tutorial ). De lo contrario, si Kayo se enferma, no tendremos pasteles.

Either way, we're still going to have a party.
 - De cualquier manera, todavía vamos a tener una fiesta.

For this first task, we'll translate this story into code. First, let's create a function that returns a Promise:
 - Para esta primera tarea, traduciremos esta historia a código. Primero, vamos a crear una función que devuelva un Promise :

```javascript
const onMyBirthday = (isKayoSick) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (!isKayoSick) {
        resolve(2);
      } else {
        reject(new Error("I am sad"));
      }
    }, 2000);
  });
};

```

In JavaScript, we can create a new Promise with new Promise(), which takes in a function as an argument: (resolve, reject) => {}.
 - En JavaScript, podemos crear un nuevo Promise con new Promise() , que toma una función como argumento: (resolve, reject) => {} .

In this function, resolve and reject are callback functions that are provided by default in JavaScript.
 - En esta función, resolve y reject son funciones de devolución de llamada que se proporcionan de forma predeterminada en JavaScript.

Let's take a closer look at the code above.
 - Echemos un vistazo más de cerca al código anterior.

When we run the onMyBirthday function, after 2000ms:
 - Cuando ejecutamos la función, después de onMyBirthday 2000ms :

If Kayo is not sick, then we run resolve with 2 as the argument
 - Si Kayo no está enfermo, entonces corremos resolve con 2 el argumento

If Kayo is sick then we run reject with new Error("I am sad") as the argument. Even though you can pass anything to reject as an argument, it's recommended to pass it an Error object.
 - Si Kayo está enfermo, entonces corremos reject con new Error("I am sad") el argumento. Aunque puedes pasar cualquier cosa como reject argumento, se recomienda pasarle un Error objeto.

Now, because onMyBirthday() returns a Promise, we have access to the then, catch, and finally methods.
 - Ahora, debido a que onMyBirthday() devuelve un Promise , tenemos acceso a los then métodos , catch , y finally .

And we also have access to the arguments that were passed into resolve and reject earlier within then and catch.
 - Y también tenemos acceso a los argumentos que se pasaron a resolve y reject antes dentro de then y catch .

Let's take a closer look at the code.
 - Echemos un vistazo más de cerca al código.

If Kayo is not sick:
 - Si Kayo no está enfermo:

```javascript
onMyBirthday(false)
  .then((result) => {
    console.log(`I have ${result} cakes`); // In the console: I have 2 cakes  
  })
  .catch((error) => {
    console.log(error); // Does not run
  })
  .finally(() => {
    console.log("Party"); // Shows in the console no matter what: Party
  });

```
If Kayo is sick:
 - Si Kayo está enfermo:
```javascript
onMyBirthday(true)
  .then((result) => {
    console.log(`I have ${result} cakes`); // does not run 
  })
  .catch((error) => {
    console.log(error); // in console: Error: I am sad
  })
  .finally(() => {
    console.log("Party"); // Shows in the console no matter what: Party
  });

```

Alright, so by now, I hope you get the basic idea of Promise. Let's move onto task 2.
 - Muy bien, a estas alturas, espero que tengas la idea básica de Promise . Pasemos a la tarea 2.



