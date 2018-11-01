# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    if a == b:
        c = (a + b) * 2
        return c
    else:
        c = a + b
        return c