"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
assignment objective: "Fizz-Buzz"
Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.

"""
for number in range(1, 101):

#if number is divisible by 3 and 5 print FizzBuzz
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

#if number is divisible by 3 print Fizz
    elif number % 3 == 0:
        print("Fizz")

#if number is divisible by 5 print Buzz
    elif number % 5 == 0:
        print("Buzz")

#if number was not divisible by 3 or 5 print the number
    else:
        print(number)
