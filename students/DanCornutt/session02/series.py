def fibonacci(n):
    """
    Computes fibonacci number, starting with integers 0 and 1.
    Args:
        param1 (int): nth fibonacci number

    Returns:
        int: Returns calculated fibonacci number value
    """
    return sum_series(n)


def lucas(n):
    """
    Computes lucas number, starting with integers 2 and 1.
    Args:
        param1 (int): nth lucas number

    Returns:
        int: Returns calculated lucas number value
    """
    return sum_series(n, 2, 1)


def sum_series(n, n0=0, n1=1):
    """
    Calculates value based on the prior numbers in a series.
    Starting with integers n0 and n1.
    Default values for n0, n1 calculate fibonacci series.

    Args:
        param1 (int): nth series number
        param2 (int): Optional, default value 0
        param2 (int): Optional, default value 1

    Returns:
        int: Returns calculated series number value
    """
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n - 2, n0, n1) + sum_series(n - 1, n0, n1)


if __name__ == "__main__":
    # run some tests
    print(__name__)
    assert fibonacci(0) == 0 "Initial calculation failed!"
    assert fibonacci(1) == 1 "Second calculation failed!"
    assert fibonacci(2) == 1 "Recursion calculation failed!"
    assert fibonacci(3) == 2 "Recursion calculation failed!"
    assert fibonacci(4) == 3 "Recursion calculation failed!"
    assert fibonacci(5) == 5 "Recursion calculation failed!"
    assert fibonacci(6) == 8 "Recursion calculation failed!"
    assert fibonacci(7) == 13 "Recursion calculation failed!"

    assert lucas(0) == 2 "Initial calculation failed!"
    assert lucas(1) == 1 "Second calculation failed!"

    assert lucas(4) == 7 "Recursion calculation failed!"

    assert sum_series(5) == fibonacci(5) "fibonacci function != sum_series"

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5) "lucas function != sum_series"

    print("tests passed")
