"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
assignment objective: write a program that returns:
-Fibonacci Series
-Lucas Series
    programs return 10th value as written; to change desired return value, adjust the
    range(value) in each for loop.
-Sum_Series
"""


#Fibonacci series of numbers, function returns: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def Fibonacci(n):
    # returning 0 or 1 are the base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)

for i in range(10):
    print(Fibonacci(i))


#Lucas series of numbers, function returns: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76
def Lucas(l):
    #returning 2 or 1 are the base cases
     if l == 0:
         return 2
     if l == 1:
         return 1
     return Lucas(l-1) + Lucas(l-2)

for i in range(10):
    print(Lucas(i))


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
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)

for i in range(10):
    print(sum_series(i))
    

if __name__ == "__main__":
    #assertion tests
    assert Fibonacci(0) == 0
    assert Fibonacci(1) == 1
    assert Fibonacci(7) == 13

    assert Lucas(0) == 2
    assert Lucas(1) == 1
    assert Lucas(4) == 7

    assert sum_series(5) == Fibonacci(5)
    assert sum_series(5, 2, 1) == Lucas(5)

    print("tests passed")
