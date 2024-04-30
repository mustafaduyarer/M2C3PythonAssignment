/*
Create a JS function that accepts 4 arguments. Add the first two arguments, then the two seconds and multiply them.
If the created number is greater than 50, the console records "the number is greater than 50!" If it is smaller,
the console records "the number is less than 50!"
---------------------------------------------------------------------------------------------------------------------
Cree una función JS que acepte 4 argumentos. Suma los dos primeros argumentos, luego los dos segundos y multiplícalos.
Si el número creado es mayor que 50, la consola registra "¡el número es mayor que 50!"
Si es más pequeño, la consola registra "¡el número es inferior a 50!"
*/

function checkNumber(a, b, c, d) {
    const sum = a + b;
    const product = c * d;

    if (sum + product > 50) {
        console.log("The number is greater than 50!");
    } else {
        console.log("The number is less than 50!");
    }
}

// Example usage:
checkNumber(10, 20, 3, 4); // Output: "The number is greater than 50!"
checkNumber(5, 10, 2, 3); // Output: "The number is less than 50!"
