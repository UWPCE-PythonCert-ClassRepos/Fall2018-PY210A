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
    if n == 1:
        return x
    elif n == 2:
        return y
    else:
        return sum_series(n - 1, x, y)+sum_series(n - 2, x, y)


if __name__ == "__main__":
    # run fibonacci tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # run lucas tests
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    # run either tests
    assert sum_series(5, 1, 1) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(6, 2, 1) == lucas(5)

    print("tests passed")