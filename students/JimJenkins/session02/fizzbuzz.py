#!/usr/bin/env python

'''
Author: Jim Jenkins (dvlupr)
Date: 10/18/2018

'''
import sys

# request how many times the user wants to run FizzBuzz
y = int(input('How many numbers do you want to FizzBuzz test?: '))

# set the sentinel value
x = 0
# create a while loop looking for the factors of 3 and 5
while x != y:
    # check to ensure the number of sequence runs is reasonable
    if y > 500:
        sys.exit('Number is too high for the system, please select a lower number')
    x = x + 1
    if x % 3 == 0:
        print (x, 'Fizz')
    elif x % 5 == 0:
        print(x, 'Buzz')
    else:
        print(x, 'FizzBuzz')