import time


def fibonacci(n):
    '''function to return the nth element in Fibonacci series'''
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
    '''function to return the nth element in Lucas series'''
    if n < 1:
        return 2
    elif n == 1:
        return 1
    else:
        return (lucas(n-1) + lucas(n-2))


def sum_series(n, first_element = 0, second_element = 1):
    '''Generalized function'''
    if first_element == 0 and second_element == 1:
        return fibonacci(n)
    elif first_element == 2 and second_element == 1:
        return lucas(n)
    else:
        return (sum_series(n-1) + sum_series(n-2))


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
