#!/usr/bin/env python

'''
Author: Jim Jenkins (dvlupr)
Date: 10/18/2018

'''

import sys


# create list and prepend first two values
num_list = list()
num_list.extend([0, 1])


#iterate through and create the sequence
def fn_fibonacci(b):
    # check to ensure the number of sequence runs is reasonable
    if b > 50:
        sys.exit('Number is too high for the system, please select a lower number')
    # set the sentinel value at zero for the iteration sequence
    a = 0
    while a != b:
        a = a + 1
        # grab the last two values from the list
        x = num_list[-1]
        y = num_list[-2]
        # calculate the next number in the list
        z = x + y
        # add the item to the list
        num_list.append(z)
        print(num_list)

# ask the user for how many times they want to run the sequence
b = int(input('How many times would you like to run the sequence?: '))

# run the sequence per the users instructions
fn_fibonacci(b)