def fibonacci(n):
    """Returns as an integer the nth value in the fibanacci sequence"""
    return sum_series(n)

    # if n == 1:
    #     return 0
    # elif n == 2:
    #     return 1
    # else:
    #     return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
    """Returns as an integer the nth value in the lucas sequence"""

    return sum_series(n, n0=2, n1=1)
    # if n == 0:
    #     return 2
    # elif n == 1:
    #     return 1
    # else:
    #     return lucas(n - 2) + lucas (n - 1)

def sum_series(n, n0=0, n1=1):
    """ Returns as an integer the nth value of a summation series
    using n0 and n1 as the seed values for the summation.
    Defaults to fibonacci sequence if n0 and n1 are not passed.
    """

    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-2, n0=n0, n1=n1) + sum_series(n-1, n0=n0, n1=n1)

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
    assert lucas(8) == 47

    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
