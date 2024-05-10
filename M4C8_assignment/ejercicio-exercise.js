/*
-Cree un bucle for en JS que imprima cada nombre en esta lista. miLista = “velma”, “exploradora”, “jane”, “john”, “harry”
---------------------------------------------------------------------------------------------------------------------
Create a loop for in JS that prints each name on this list. Milista = "Velma", "Explorer", "Jane", "John", "Harry"
*/

const milista = ["Velma", "Explorer", "Jane", "John", "Harry"];

for (const name of milista) {
    console.log(name);
}

console.log('---------------------------------------------------------------------')

/*
-Cree un bucle while que recorra la misma lista y también imprima los nombres. Nota: Recuerda crear un contador para que el ciclo no sea infinito.
---------------------------------------------------------------------------------------------------------------------
-Create a While loop that travels the same list and also prints the names. Note: Remember to create a counter so that the cycle is not infinite.*/

const milista = ["Velma", "Explorer", "Jane", "John", "Harry"];
let counter = 0;

while (counter < milista.length) {
    console.log(milista[counter]);
    counter++;
}

console.log('---------------------------------------------------------------------')

/*
-Cree una función de flecha que devuelva "Hola mundo".
---------------------------------------------------------------------------------------------------------------------
-Create an arrow function that returns "Hi Mundo".
*/

const greetMundo = () => "Hola Mundo";

console.log(greetMundo()); // Output: Hola Mundo


console.log('---------------------------------------------------------------------')

