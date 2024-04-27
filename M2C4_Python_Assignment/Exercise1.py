"""
Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

"""

#List: A list is an ordered collection of elements. You can store different types of data in a list. Here’s an example of creating a list:

my_list = [1, 2, 3, "apple", 5.5]
print(my_list)
print('--------------------------------')

#Tuple: A tuple is similar to a list, but it is immutable (cannot be changed after creation). Use parentheses to define a tuple:

my_tuple = (10, 20, 30, "banana", 40.5)
print(my_tuple)
print('--------------------------------')

#Float: A float represents a decimal number. You can create a float directly:

my_float = 3.14
print(my_float)
print('--------------------------------')


#Integer: An integer represents a whole number. You can create an integer like this:

my_integer = 42
print(my_integer)
print('--------------------------------')

#Decimal: The decimal module provides precise decimal arithmetic. To create a decimal, you’ll need to import the module and use it:
from decimal import Decimal

product_cost = Decimal(88.40)
commision_rate = Decimal(0.08)
qty = 450

product_cost += (commision_rate * product_cost)
print(product_cost)

print(product_cost * qty)
print('--------------------------------')

#Dictionary: A dictionary stores key-value pairs. Keys must be unique. Here’s an example:

my_dict = {"name": "Alice", "age": 30, "city": "Wonderland"}
print(my_dict)

#Dictionary: A dictionary stores key-value pairs. Keys must be unique. Here’s an example:

my_dict = {"name": "Alice", "age": 30, "city": "Wonderland"}
print(my_dict)