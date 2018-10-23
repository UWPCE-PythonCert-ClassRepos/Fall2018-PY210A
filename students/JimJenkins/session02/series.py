#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr)
Date: 10/23/2018

"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)


def sum_series(n, x=0, y=1):
    if n == 0:
        return n == x
    elif n == 1:
        return n == y
    else:
        return sum_series(n-1)+sum_series(n-2)


print('fibonacci sequence.....')
for i in range(1, 10):
    print(fibonacci(i))


print(' ')


print('lucas sequence.....')
for i in range(0, 10):
    print(lucas(i))


print(' ')


print('sum series')
for i in range(0, 10):
    print('no parameters', sum_series(i))

for i in range(0, 10):
    print('with parameters', sum_series(i, 2))
