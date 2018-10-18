"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
assignment objective:
"Fizz-Buzz"
takes a random number and prints fizz if the number is divisible by 3
takes a random number and prints buzz if the number is divisible by 5
takes a random number and prints fizzbuzz if the number is divisible by 3 and 5
"""

import random

test_num = random.randint(1,101)

#print the number being evaluated for the sake of clarity
print(test_num)

#if test_num is divisible by 3 and 5 print fizzbuzz
if test_num % 3 == 0 and test_num % 5 == 0:
    print("fizzbuzz")

#if test_num is divisible by 3
elif test_num % 3 == 0:
    print("fizz")

#if test_num is divisible by 5
elif test_num % 5 == 0:
    print("buzz")

#if test_num was not divisible by 3 or 5
else:
    print("the number is not divisible by 3 or 5")
