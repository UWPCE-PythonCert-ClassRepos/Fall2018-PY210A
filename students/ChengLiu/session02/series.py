# PY210A - session02
# Cheng Liu
"""
A function with one required parameter and two optional parameters
(1) The required parameter determines which elements in the series to print.
(2) The two optional parameters have default value of 0 and 1 which determines 
the first two values for the series to be produced.
(3) Calling the function with no optional prameters will produce numbers from 
the fibonacci series
(4) Calling it with the optional arguments 2 and 1 will produce values from 
the lucase numbers
(5) Other values for the optional parameters will produce other series
"""


def fibonacci(n):
    """ Compute the nth Fibonacci Number """
    if n == 0:
        return 0    # prints out the 1st element of fibonacci number (i.e. 0)
    elif n == 1:
        return 1    # prints out the 2nd element of fibonacci number (i.e. 1)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)    # fibonacci series


def lucas(n):
    """ Compute the nth Lucas number """
    if n == 0:
        return 2    # prints out the 1st element of lucas number (i.e. 2)
    elif n == 1:
        return 1    # prints out the 2nd element of lucas number (i.e. 1)
    else:
        return lucas(n - 1) + lucas(n - 2)    # lucas series



def sum_series(n, n0 = 0, n1 = 1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series
    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    """
    if n0 == 0 and n1 == 1:
        return fibonacci(n)
    elif n0 == 2 and n1 == 1:
        return lucas(n)
    else:
        return sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)



if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
