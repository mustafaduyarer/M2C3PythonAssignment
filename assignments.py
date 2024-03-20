
# M2C3 Python Assignment
print('-------------------------------------------------------')

# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
my_string = "Hello World!"
my_integer = 42
my_float = 3.14
my_list = [1, 2, 3, 4, 5]
is_true = True
is_false = False

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
first_three_letters = my_string[:3]
print('First three letters are:' + first_three_letters)

print('-------------------------------------------------------')

# Exercise 3: Use an index to grab the first element from your list.
first_element = my_list[0]
print(f"The first element of the list is: {first_element}")

print('-------------------------------------------------------')

# Exercise 4: Create a new number variable that adds 10 to your original number.
original_number = 22  # Replace with your actual original number
new_number = original_number + 10
print(f"The new number after adding 10 is: {new_number}")

print('-------------------------------------------------------')

# Exercise 5: Use an index to get the last element in your list.
my_new_list = [1, 2, 3, 4, 5,6,7,8,9]
last_element = my_new_list[-1]
print(f"The last element of the list is: {last_element}")

print('-------------------------------------------------------')

# Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
list_names = names.split()
print(list_names)

print('-------------------------------------------------------')

# Exercise 7: Get the first word from your string using indexes.
# Use the upper function to transform the letters into uppercase.
# Create a new string that takes the uppercase word and the rest of the original string.
first_word = my_string.split()[0]
print(first_word)
uppercase_word = first_word.upper()
print(uppercase_word)

rest_of_string = my_string[len(first_word):]
print(rest_of_string)
new_my_string = uppercase_word + rest_of_string
print(new_my_string)

print('-------------------------------------------------------')


# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
new_number = 52
# String interpolation
sentence = f"The new number is {new_number}."

print(sentence)

print('-------------------------------------------------------')

# Exercise 9: Print “hello world”.
print("\"hello world\"")

