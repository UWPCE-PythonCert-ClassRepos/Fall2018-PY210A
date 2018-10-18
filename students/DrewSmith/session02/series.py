#!/usr/bin/env python3
"""
Module for generating adding sequence index values.
"""
def fibonacci(n):
    """
    Returns the nth value in the fibonacci sequence.
    
    :param n: the zero based index value in fibonacci sequence to return
    """
    first , second, val = 0, 1, 0
    if n <= 0:
        return first
    elif n == 1:
        return second

    for __ in range(2, n + 1):
        val = first + second
        first, second = second, val
    return val

def lucas(n):
    """
    Returns the nth value in the lucas sequence.
    
    :param n: the zero based index value in lucas sequence to return
    """
    first , second, val = 2, 1, 0
    if n <= 0:
        return first
    elif n == 1:
        return second

    for __ in range(2, n + 1):
        val = first + second
        first, second = second, val
    return val

def sum_series(n, first=0, second=1):
    """
    Returns the nth value in a sequence with a given start.
    
    :param n: the zero based index in sequence to return
    :param first: the first value of the sequence
    :param second: the second value of the sequence
    """
    if n == 1:
        return second
    elif n <= 0:
        return first
    return sum_series(n -1, second, first + second)

if __name__ == "__main__":
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29
    assert lucas(8) == 47
    assert lucas(9) == 76

    assert sum_series(0) == fibonacci(0)
    assert sum_series(1) == fibonacci(1)
    assert sum_series(2) == fibonacci(2)
    assert sum_series(9) == fibonacci(9)

    assert sum_series(0,2,1) == lucas(0)
    assert sum_series(1,2,1) == lucas(1)
    assert sum_series(2,2,1) == lucas(2)
    assert sum_series(9,2,1) == lucas(9)
    print("All tests passed")