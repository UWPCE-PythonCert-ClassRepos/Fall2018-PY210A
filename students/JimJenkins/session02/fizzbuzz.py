#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr)
Date: 10/18/2018

Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.
"""

# request how many times to run FizzBuzz
y = 100


# set the sentinel value
x = 0


# create a while loop looking for the factors of 3 and 5
while x != y:
    x = x + 1
    if x % 3 == 0 and x % 5 == 0:
        print(x, 'FizzBuzz')
    elif x % 3 == 0:
        print(x, 'Fizz')
    elif x % 5 == 0:
        print(x, 'Buzz')
    else:
        print(x)
