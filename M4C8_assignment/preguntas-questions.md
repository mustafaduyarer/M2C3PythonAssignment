
# PREGUNTAS
 >QUESTIONS



## ¿Qué diferencia a Javascript de cualquier otro lenguaje de programación?
> What differentiates Javascript from any other programming language?

### ¿Qué es JavaScript? What is Javascript?

JavaScript es un lenguaje de programación, de secuencias de comandos, capaz de aportar soluciones eficaces en la mayoría de los ámbitos de la tecnología. Te permite crear contenido de actualización dinámica, controlar multimedia, animar imágenes, etc.
> Javascript is a programming language, command sequences, capable of providing effective solutions in most technology areas. It allows you to create dynamic update content, control multimedia, encourage images, etc.
### ¿Para qué se utiliza JavaScript?

Los usos más importantes de JavaScript son los siguientes:

* Desarrollo de sitios web del lado del cliente (front end, en el navegador).
* Desarrollo de aplicaciones para dispositivos móviles, híbridas o que compilan a nativo.
* Construcción de servidores web y aplicaciones de servidor.
* Desarrollo de aplicaciones de escritorio para sistemas Windows, Linux y Mac.
* Desarrollo de juegos.

### JavaScript: características y beneficios

* **Simplicidad:** Posee una estructura sencilla que lo vuelve más fácil de aprender e implementar.&#x20;
* **Velocidad:** Se ejecuta más rápido que otros lenguajes y favorece la detección de los errores.
* **Versatilidad:** Es compatible con otros lenguajes, como: PHP y Java. Además, hace que la ciencia de datos y el aprendizaje automático sean accesibles.
* **Popularida:** Existen numerosos recursos y foros disponibles para ayudar a los principiantes con habilidades y conocimientos limitados.
* **Carga del servidor**: La validación de datos puede realizarse a través del navegador web y las actualizaciones solo se aplican a ciertas secciones de la página web.
* **Actualizaciones:** Se actualiza de forma continua con nuevos frameworks y librerías, esto le asegura relevancia dentro del sector.

### ¿Cuáles son las desventajas de JavaScript?

* **Compatibilidad con los navegadores:** Los diferentes navegadores web interpretan el código JavaScript de forma distinta. Por lo tanto, necesitarás probarlo en todos los navegadores populares, incluyendo las versiones más antiguas.
* **Depuración:** Aunque algunos editores de HTML admiten la depuración, son menos eficaces que otros editores. Encontrar el problema puede ser un reto, ya que los navegadores no muestran ninguna advertencia sobre los errores.

### Principales diferencias entre JavaScript y Java.

En un artículo anterior, ya te contamos acerca del lenguaje de programación Java. Aquí aprovechamos para descubrirte las diferencias que tiene con JavaScript:

* Java se utiliza para crear aplicaciones en variados dispositivos o en navegadores, mientras que JavaScript se usa principalmente para documentos HTML y navegadores.
* Tanto Java como JavaScript emplean diferentes complementos. Incluso las extensiones de archivo son distintas, siendo Java «.Java» y JavaScript «.js».
* Java es un lenguaje compilado e interpretado, mientras que los códigos JavaScript son ejecutados directamente por un navegador.
* Java es un lenguaje de programación multiplataforma orientado a objetos y centrado en la red, mientras que JavaScript es un lenguaje de secuencias de comandos que permite a los desarrolladores crear páginas web interactivas.
* La sintaxis de Java requiere que se declaren los tipos de datos, mientras que la sintaxis de JavaScript no necesita esto. Además, Java es un lenguaje estático y JavaScript es dinámico.
* JavaScript se depura en una fase y Java en dos. JavaScript hace que el código trabaje informando de los errores que se producen a medida que se está ejecutando. Java primero realiza la fase de compilación, y el compilador indica los posibles errores de sintaxis presentes en nuestro código. Después, se ejecuta el programa, y pueden surgir errores para ser depurados.
* Java posee variables definidas que no se pueden cambiar y es más complejo, JavaScript puede ser cambiante, dándole flexibilidad, y es más sencillo.

### Diferencias más marcadas entre JavaScript y Python.

&#x20;¿Cuáles son realmente las diferencias más relevantes entre ambos lenguajes de programación? A continuación presentamos algunas de las que más se resaltan.

* Python se concibió como idea a finales de los 80’s y su primera versión fue lanzada en 1991, JavaScript por otra parte vino un poco después, su primera versión llegó por allá en 1995. Por tanto, Python es un poco más antiguo.
* En Python, existen diferentes tipos numéricos como int, float, etc. Mientras que en JavaScript solo hay números de punto flotante.
* En los últimos años, Python ha superado en popularidad a JavaScript.
* **Sintaxis:** JavaScript utiliza llaves `{}` y puntos y comas `;` para separar declaraciones y bloques de código. Python utiliza indentación (espacios en blanco) para definir bloques de código, lo que lo hace más fácil de leer y mantener.
* **Ambiente de ejecución:** JavaScript es ejecutado principalmente en navegadores web y también puede ser utilizado en el lado del servidor a través de Node.js. Python se puede utilizar en una amplia variedad de entornos, incluidos servidores web, scripts, aplicaciones de escritorio, análisis de datos y más.
* **Tipado:** JavaScript es un lenguaje de tipado débil y dinámico, lo que significa que las variables pueden cambiar de tipo durante la ejecución y no requieren una declaración de tipo explícita. Python es un lenguaje de tipado fuerte y dinámico, lo que significa que las variables están asociadas con un tipo específico y se requiere una declaración de tipo explícita.
* JavaScript es un lenguaje de programación interpretado y orientado a eventos, diseñado para su uso principalmente en navegadores web. Python es un lenguaje de programación interpretado, multipropósito y general, utilizado en diversas aplicaciones, desde desarrollo web hasta ciencia de datos.


> In summary, JavaScript’s interpreted nature, client-side execution, object-oriented paradigm, dynamic typing, and widespread adoption differentiate it from other programming languages. Understanding these distinctions helps developers choose the right language for their specific needs. 
>
> En resumen, la naturaleza interpretada de JavaScript, la ejecución del lado del cliente, el paradigma orientado a objetos, la tipificación dinámica y la adopción generalizada lo diferencian de otros lenguajes de programación. Comprender estas distinciones ayuda a los desarrolladores a elegir el lenguaje adecuado para sus necesidades específicas


## ¿Cuáles son algunos tipos de datos JS?
## What are some JS data types?

Certainly! JavaScript has eight fundamental data types. Let’s explore each of them:

* **String:**
* A string represents a sequence of characters, such as "Hello, World!". Strings can be enclosed in either single quotes (') or double quotes (").

* **String:** representa datos textuales (cadenas de caracteres).

```javascript
console.log(typeof 'MZ');

// string
```

* **Number:**
* Numbers in JavaScript are stored as decimal numbers (floating point). They can be written with or without decimals. For example:
With decimals: let x1 = 34.00;
Without decimals: let x2 = 34;

**Number:** permite representar y manipular valores numéricos como «37» o «-9.25».

```javascript
console.log(typeof 42);

// number
```

* **Bigint:**
* Introduced in ES11 (ECMAScript 2020), BigInt allows you to represent large integers beyond the limits of the Number type. For example: const bigNumber = 1234567890123456789012345678901234567890n;
* **BigInt:** representa valores numéricos que son demasiado grandes para ser representados por el tipo de dato **number**.

```javascript
console.log(typeof 1234567890123456789n);

// bigint
```

* **Boolean:**
* A boolean represents either true or false. It’s commonly used for conditional statements and logical operations.

**Boolean:** representa un valor lógico y puede tener dos valores, ya sean **true** o **false**.&#x20;

```javascript
console.log(typeof true);

// boolean
```

* **Undefined:**
* When a variable is declared but not assigned a value, it is undefined. For example: let myVar; // undefined
* * **Undefined:** representa una variable que no ha sido declarada o a la cual no se le ha asignado un valor.

```javascript
console.log(typeof undefined);

// undefined
```
* **Null:**
* Represents the intentional absence of any value. It’s often used to indicate that a variable has no value or an empty object reference.

* **Null:** representa la ausencia intencional de cualquier valor, un valor nulo o «vacío».
***
* **Symbol:**
* Introduced in ES6, symbols are unique and immutable values. They are often used as property keys in objects to prevent accidental name clashes.
* **Symbol:** es un valor primitivo único e inmutable.

```javascript
console.log(typeof Symbol(1));

// symbol
```

* **Object:**
* The most versatile data type. Objects can contain key-value pairs, arrays, functions, and other objects. For example:

Existen seis tipos de datos primitivos, es decir, que no son un objeto. Hay que tener cuidado con este concepto porque JavaScript en muchas situaciones convierte automáticamente los datos primitivos en objetos equivalentes a excepción de **null** y **undefined**.

* **Object:** representa una colección de datos definidos y entidades más complejas.

```javascript
console.log(typeof {});

//object
```

* **Function:** es una forma abreviada para funciones, aunque cada constructor de funciones se deriva del constructor **Object**. Son objetos con la capacidad de ser ejecutables.

```javascript
console.log(typeof function() {});

// function
```

## ¿Cuáles son las tres funciones de String en JS?
### What are the three String functions in JS?

#### 1. String.split()

Divide una cadena en un arreglo de subcadenas de la cadena original a partir de un carácter separado.
> Divide a chain into an arrangement of subcadens of the original chain from a separate character.
```javascript
let cadena = "Hola,mundo,JavaScript";
console.log(cadena.split(","));

// (3) ['Hola', 'mundo', 'JavaScript']
```

#### 2. String.substring()

Extrae caracteres desde un índice A hasta un índice B sin incluirlo
> Extracts characters from an index A to a B index without including it

```javascript
let cadena = "Hola";
console.log(cadena.substring(0,3));

// Hol
```

#### 3. String.trim()

Elimina espacios en blanco al inicio y al final de una cadena:
> Eliminate blank spaces at the beginning and at the end of a chain:

```javascript
let cadena = "   Hola   ";
console.log(cadena.trim());

// Hola
```

## ¿Qué es un condicional?
## What is a conditional?
> A conditional is a sentence structure that expresses a particular situation and its result or consequence. It consists of two main parts: the if clause (which sets out a condition) and the main clause (which describes what happens when that condition is fulfilled).
>
> Un condicional es una estructura de oración que expresa una situación particular y su resultado o consecuencia. Consta de dos partes principales: la cláusula if (que establece una condición) y la cláusula principal (que describe lo que sucede cuando se cumple esa condición).

En el mundo de la programación, a menudo necesitamos que nuestro código tome decisiones basadas en ciertas condiciones. Aquí es donde entra en juego el condicional _if_ en JavaScript.

### Condicional if.

El condicional _if_ evalúa una expresión y, si esa expresión es verdadera, ejecuta un bloque de código. La estructura básica del condicional _if_ es simple y directa.

```
// Sintaxis
```

```javascript
/if (condición) {
    // Código a ejecutar si la condición es verdadera
}
```

#### Ejemplos:

#### Verificar si un número es mayor que 10.

```javascript
let numero = 15;
if (numero > 10) {
    console.log("El número es mayor que 10.");
}

// El número es mayor que 10.
```

#### Verificar si un número es positivo

```javascript
let numero = 5;
if (numero > 0) {
    console.log("El número es positivo.");
}

// El número es positivo.
```

#### Comprobar si una palabra es "hola"

```javascript
let palabra = "hola";
if (palabra === "hola") {
    console.log("La palabra es hola.");
}

// La palabre es hola.
```



#### Verificar si un estudiante pasó el examen

```javascript
let nota = 85;
if (nota >= 60) {
    console.log("El estudiante pasó el examen.");
}

// El estudiante pasó el examen.
```

#### Verificar si un número es par o impar

<pre class="language-javascript"><code class="lang-javascript"><strong>let numero = 7;
</strong>if (numero % 2 === 0) {
    console.log("El número es par.");
}

if (numero % 2 !== 0){
    console.log("El número es impar.");
}

// El número es impar.
</code></pre>

### Condicional if - else.

Imagina que está en una encrucijada y debe tomar una decisión basada en una condición. Si se cumple una condición, tomas el camino de la izquierda; de lo contrario, tomas el camino de la derecha. Esa es precisamente la esencia del condicional _if-else_.

```
// Sintaxis
```

```javascript
 if (condición) {
    // Código a ejecutar si la condición es verdadera
    } else {
    // Código a ejecutar si la condición original es falsa
    }
```

#### Ejemplos:

#### Determinar el tipo de suscripción en una plataforma.

<pre class="language-javascript"><code class="lang-javascript">let horasVistas = 50;
<strong>if (horasVistas > 40) {
</strong>     console.log("Recomendamos la suscripción Premium.");
}
else {
     console.log("Una suscripción Estándar es suficiente para ti.");
}

// Recomendamos la suscripción Premium.
</code></pre>

#### Verificar si un usuario puede acceder a un contenido exclusivo.

```javascript
let esMiembro = true;
let tieneCupon = false;

if (esMiembro || tieneCupon) {
   console.log("¡Puedes acceder al contenido exclusivo!");
} else {
   console.log("Lo sentimos, necesitas ser miembro o tener un cupón.");
}

// ¡Puedes acceder al contenido exclusivo!
```

#### Determinar el descuento aplicado en una tienda en línea

```javascript
let esEstudiante = true;
let esPrimerCompra = false;

if (esEstudiante || esPrimerCompra) {
    console.log("Tienes un 10% de descuento.");
} else {
    console.log("No tienes descuentos disponibles.");
}
    
// Tienes un 10% de descuento.
```

## ¿Qué es un operador ternario?

> The ternary operator is a conditional operator that takes three operands. It’s commonly used in programming languages to provide a concise way of expressing simple conditional logic. 
>
>El operador ternario es un operador condicional que toma tres operandos. Se usa comúnmente en lenguajes de programación para proporcionar una forma concisa de expresar lógica condicional simple.

El operador condicional (ternario) es el único **operador en JavaScript** que tiene tres operandos. Este operador se usa con frecuencia como atajo para la instrucción if. Siendo un condicional simple que ejecuta una de dos instrucciones posibles dependiendo de la evaluación previa de una condición.

### **Sintaxis**

```javascript
condición ? expresión1 : expresión2;
```
* It can be visualized as an if-else statement:
* Se puede visualizar como una if-else declaración:
```
if (Expression1) {
    variable = Expression2;
} else {
    variable = Expression3;
}
```
### **Parámetros**

* **Condición**.- Expresión que se puede evaluar como verdadera o falsa.
* **Expresión 1 y 2**.- Expresiones con valores definidos que pueden ejecutarse dependiendo de la condición.

### **Forma de uso**

```javascript
variable = expresion ? true_value : false_value;
```

Esto permite básicamente una asignación condicional a una variable en función de la evaluación de la expresión. Si es cierto, entonces true\_value se asigna a la variable, caso contrario, entonces false\_value se asigna a la variable.

### **Ejemplos**

```javascript
var num1 = 5;
var num2 = 7;
var max = ( num1 > num2 ) ? num1 : num2 ;

console.log(max);

// 7
```

En este ejemplo , `max` es usado para ser asignado al número con el valor más alto . La expresión indica que si `num1` es mayor que `num2`, entonces `num1` se asigna a `max` .  Sin embargo, si la expresión es falsa ( lo que significa que `num2` es mayor o igual a `num1` ), a continuación, `num2` se asigna a `máx` .

```javascript
var miEdad = 24;
var mayorEdad = (miEdad > 18) ? "Sí, eres mayor de edad" : "No, sigue intentando";

console.log(mayorEdad);

// Sí, eres mayor de edad
```



En este segundo ejemplo vemos cómo reconocer un dato si es mayor a 18, y asignar a la variable un string, con dos posibilidades.

```javascript
var diaFeriado = false;
var pagar = "Hoy debo pagar " + ( diaFeriado ? "19 euros" : "15 euros");

console.log(pagar);

// Hoy debo pagar 15 euros
```

En este otro caso evaluamos una expresión booleana, y se obtiene un string el cual posteriormente es concatenado a otro.

Podemos usar también el operador ternario con una estructura más larga.

```javascript
var a = 15;
var numeroObtenido = a == 5 ? "Cinco":
                    a == 7 ? "Siete":
                    a == 11 ? "Once":
                    a == 15 ? "Quince":
                    "Otro Número";

console.log( numeroObtenido );

// Quince
```

En este caso, ampliamos el uso del condicional ternario. Cuando la primera condición evaluada no es verdadera, optamos por establecer una nueva condición y seguir el ciclo anterior.

## ¿Cuál es la diferencia entre una declaración de función y una expresión de función?
### What is the difference between a declaration of function and an expression of function?

> Certainly! In JavaScript, there are two ways to define functions: function declarations and function expressions. 
>
> ¡Ciertamente! En JavaScript, hay dos formas de definir funciones: declaraciones de funciones y expresiones de funciones.

Veremos las diferencias de sintaxis y prácticas de ambas a través de un pequeño ejemplo.

Let’s explore the differences between them:

Un ejemplo de **declaración de función** es el siguiente:

```javascript
function sum(a,b) {
   return a + b;
}
```

Se caracteriza por el hecho de que la **declaración de una función la hace disponible para todo el programa**, incluyendo el código que está antes de la declaración de la función.&#x20;

```javascript
var add = sum(3,2);
 
function sum(a,b) {
   return a + b;
}

console.log(add);

// 5
```

Una **expresión con una función** es:

```javascript
var sum = function(a,b) {
   return a + b;
};
```

En este caso, estamos declarando un función y asignándosela a una variable. Es similar a declarar una expresión lambda en Pyhton. No es posible referenciarla antes de la expresión, porque realmente no se trata de una función declarada, sino del valor asignado a una variable y, por tanto, **hasta que no se defina la variable no se puede utilizar**.

```javascript
var sum = function(a,b) {
    return a + b;
 };

 console.log(sum(4,2));
 
 // 6
```

Una diferencia más. En el segundo caso (usar una función en una expresión) es necesario terminar la expresión con un punto y coma (`;`), igual que cualquier otra expresión.

## ¿Qué es la palabra clave "this" en JS?
### What is the keyword "This" in JS?


### ¿Qué es el `this`? <a href="#que-es-el-this" id="que-es-el-this"></a>

> It is a word reserved in JavaScript that we can use to refer to the context in which it is invoked, so its implicit value can vary during the execution of the code.

Es una palabra reservada en JavaScript que podemos utilizar para referirnos al contexto en el que se invoca, por lo que su valor implícito puede variar durante la ejecución del código.

### `this` en el contexto global <a href="#this-en-el-contexto-global" id="this-en-el-contexto-global"></a>

Decimos que el contexto global es todo lo que se encuentra fuera de cualquier bloque de código.

En este caso, `this` siempre hace referencia al objeto global:

```javascript
console.log(this === window);

// true
```

```javascript
this.awesomeNumber = 37
console.log(awesomeNumber)

// 37
```

### `this` en el contexto de una función <a href="#this-en-el-contexto-de-una-funcion" id="this-en-el-contexto-de-una-funcion"></a>

Si invocamos `this` dentro de una función, su valor cambia dependiendo de cómo ejecutamos la función.

#### Llamada simple <a href="#llamada-simple" id="llamada-simple"></a>

Si es una llamada simple y no está en modo estricto, `this` devuelve el objeto global.

```javascript
function whoIsThis() {
  return this
}

console.log(whoIsThis() === window)

// true
```

#### Llamada simple (modo estricto) <a href="#llamada-simple-modo-estricto" id="llamada-simple-modo-estricto"></a>

Si es una llamada simple y está en modo estricto, `this` conserva el valor que haya recibido antes de la ejecución de la función, y devuelve `undefined` si no ha recibido ninguno.

```javascript
function whoIsThis() {
  'use strict'
  return this
}

console.log(whoIsThis())

// undefined
```

#### Como método de objeto <a href="#como-metodo-de-objeto" id="como-metodo-de-objeto"></a>

Si la función es el método de un objeto y se invoca como tal, `this` es el objeto en sí mismo.

```javascript
const me = {
  name: 'Carlos Reyes',
  sayMyName() {
    return this.name
  },
}

console.log(me.sayMyName())

// 'Carlos Reyes'
```

#### Función asignada como método de un objeto <a href="#funcion-asignada-como-metodo-de-un-objeto" id="funcion-asignada-como-metodo-de-un-objeto"></a>

Cuando se define una función y luego se asigna como método de un objeto, `this` dentro de la función se refiere al objeto al que se ha asignado la función.

```javascript
function sayHello() {
  console.log(`Hola, soy ${this.name}.`)
}

const person = {
  name: 'Juan',
  greet: sayHello, // asignamos 'sayHello' a la propiedad 'greet'
}

person.greet()

// Hola, soy Juan.
```

#### Función asignada como método de un objeto anidado <a href="#funcion-asignada-como-metodo-de-un-objeto-anidado" id="funcion-asignada-como-metodo-de-un-objeto-anidado"></a>

Cuando se define una función y se asigna como propiedad de un objeto más anidado, `this` dentro de la función se refiere al objeto más inmediato que contiene la función como propiedad.

```javascript
const myObj = {
  myMethod: function () {
    console.log(this)
  },
  nestedObj: {
    nestedMethod: myObj.myMethod,
  },
}

myObj.myMethod() // Imprime el objeto myObj
myObj.nestedObj.nestedMethod()

// Imprime el objeto nestedObj
```

> Remember that this is not a variable; it is a keyword, and you cannot change its value directly1. Understanding how this behaves in different contexts is crucial for writing effective JavaScript code! 
> 
> Recuerde que this no es una variable; Es una palabra clave y no puede cambiar su valor directamente 1 . ¡Comprender cómo this se comporta en diferentes contextos es crucial para escribir código JavaScript efectivo!