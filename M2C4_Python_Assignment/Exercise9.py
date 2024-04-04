"""
Exercise 9: Use reassignment to add an element to your tuple.

"""
my_tuple = (10, 20, 30, "banana", 40.5)
print(my_tuple)
print('--------------------------------')

my_tuple = (10, 20, 30, "banana", 40.5)
new_element = 500  # Replace this with the value you want to add
my_tuple += (new_element,)
#my_tuple = my_tuple + (new_element,)
print(my_tuple)