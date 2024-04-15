

print("------------------------------EXERCISE1--------------------------------------------")

"""
exercise 1 -- ejercicio 1
Cree un bucle For de Python. Create a for loop in Python

"""
# Example of a simple for loop in Python
for i in range(5):
    print(f"Loop iteration {i + 1}")

# Output:
# Loop iteration 1
# Loop iteration 2
# Loop iteration 3
# Loop iteration 4
# Loop iteration 5

print("--------------------------------EXERCISE2------------------------------------------")
"""
exercise 2 -- ejercicio 2
Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
 Create a Python function called Sum that takes 3 arguments and returns the sum of 3.
"""


def Sum(a, b, c):
    return a + b + c


"""
   Returns the sum of three numbers.

   Args:
       a (float or int): First number.
       b (float or int): Second number.
       c (float or int): Third number.

   Returns:
       float or int: Sum of the three numbers.
"""
# Example usage
result = Sum(1, 2, 3)
print(f"The sum of 1, 2, and 3 is: {result}")

print("--------------------------------EXERCISE3------------------------------------------")

"""
exercise 3 -- ejercicio 3
Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
Create a Lambda function with the same functionality as the sum function that has just created.
"""
Sum = lambda a, b, c: a + b + c

# Example usage
result = Sum(1, 2, 3)
print(f"The sum of 1, 2, and 3 is {result}")

print("--------------------------------EXERCISE14------------------------------------------")

"""
exercise 4 -- ejercicio 4
  -Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

Esta es toda la asignación, ¡mucha suerte!
"""
# Given variables
Name = 'Mustafa'
List_name = ('Jessica', 'Paul', 'George', 'Henry', 'Adam')

# Initialize a flag to track if the value of Name is found in the list
found_name = False

# Check if Name is in the list
for name in List_name:
    if name == Name:
        found_name = True
        break

# Print the result
if found_name:
    print(f"'{Name}' is found in the list.")
else:
    print(f"'{Name}' is not found in the list.")

