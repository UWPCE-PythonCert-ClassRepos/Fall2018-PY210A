#!/usr/bin/env python

"""

The number 6 is a truly great number.
Given two int values, a and b, return True if either one is 6.
Or if their sum or difference is 6.

Note: the function abs(num) computes the absolute value of a number.
"""


def love6(num1, num2):
    total = num1 + num2
    diff = num1 - num2
    if num1 == 6 or num2 == 6:
        return True
    elif abs(total) == 6 or abs(diff) == 6:
        return True
    else:
        return False
