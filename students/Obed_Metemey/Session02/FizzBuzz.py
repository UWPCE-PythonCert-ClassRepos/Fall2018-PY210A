
"""
/usr/bin/env -- Python3
Fizz Buzz Exercise
Author : OM
"""

# Goal:

#     Write a program that prints the numbers from 1 to 100 inclusive.
#     But for multiples of three print “Fizz” instead of the number.
#     For the multiples of five print “Buzz” instead of the number.
#     For numbers which are multiples of both three and five print “FizzBuzz” instead.

# print(10 % 7)


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


# Example
fizzbuzz()
