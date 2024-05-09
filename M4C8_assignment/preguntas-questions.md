
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












