"""
Project Requirements: Build FizzBuzz in Python

So we're going to write a program that prints the numbers from 1 to 100 but for multiples of 3 it prints Fizz.
So it prints a string of fizz instead of the number and for the multiples of five it prints Buzz for the numbers
which are multiples of both 5 and 3 then you're going to print out fizz buzz.
And so just to give an idea of what this is going to look like you're going to print out something that
is 1, 2, 3, 4, and 5. But instead of where we have a number 3 right here,
this instead is going to be the string Fizz and instead of the number 5 this is going to be Buzz.

1
2
Fizz
4
Buzz


"""
def fizz_buzz(num1, num2):
    for num in range(num1, num2):
        output = ""
        if num % 3 == 0:
            output = output + "Fizz"
        if num % 5 == 0:
            output += "Buzz"
        print(output or num)

# call funtion
fizz_buzz(1, 101)