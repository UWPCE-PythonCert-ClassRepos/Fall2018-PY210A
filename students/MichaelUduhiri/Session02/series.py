"""
a template for the series assignment
"""


def fibonacci(n):
    """ compute the nth Fibonacci number """
    x = 0
    y = 1
    for num in range(0, n):
        x,y = y,x+y
    return x
print (fibonacci(3))

def lucas(n):
    """ compute the nth Lucas number """
    x = 2
    y = 1
    if n == 0:
        return x
    for num in range(2, n + 1):
        z = x + y
        x = y
        y = z
    return y
print (lucas(7))


def sum_series(n,n0=0,n1=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    """
    return fibonacci(2)
    return lucas(3)
print (sum_series(2, 3, 4))

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

    assert sum_series(5) == fibonacci(4)

    assert sum_series(3,0,1) == fibonacci(3)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
