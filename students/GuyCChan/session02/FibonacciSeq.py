# compute the Fibonacci, Lucas, and sum series sequences
def fibonacci(n):
   """ compute the nth Fibonacci number """
   """ set up seed values """
    if n == 0:
        return 0
    if n == 1:
        return 1
    """ define the procedure for the sequence """
    else:
        return (fibonacci(n - 2) + fibonacci(n - 1))

def lucas(n):
    """ compute the nth Lucas number """
    """ set up seed values """
    if n == 0:
        return 2
    if n == 1:
        return 1
    """ define the procedure for the series """
    else:
        return (lucas(n - 2) + lucas(n - 1))

def sum_series(n, n0, n1):   
    """ compute the nth value of a summation series. """
    """ :param n0=0: value of zeroth element in the series """
    """ :param n1=1: value of first element in the series """   
    if n == 0:
        return n0
    if n == 1:
        return n1
    """ define the procedure for the series """
    else:
        return (sum_series(n - 2) + sum_series(n - 1))

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

    assert sum_series(5, 0, 1) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
