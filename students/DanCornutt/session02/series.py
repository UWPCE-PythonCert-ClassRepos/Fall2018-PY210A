def fibonacci(n):
    """
    Computes fibonacci number, starting with integers 0 and 1.
    Args:
        param1 (int): nth fibonacci number

    Returns:
        int: Returns calculated fibonacci number value
    """
    print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

def lucas(n):
    """
    Computes lucas number, starting with integers 2 and 1.
    Args:
        param1 (int): nth lucas number

    Returns:
        int: Returns calculated lucas number value
    """
    print(n)
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)

def sum_series(n, n0=0, n1=1):
    """
    Calculates value based on the prior numbers in a series.
    Starting with integers n0 and n1.
    Default values for n0, n1 calculate fibonacci series.

    Args:
        n (int): nth series number
        n0 (int): Optional, default value 0
        n1 (int): Optional, default value 1

    Returns:
        int: Returns calculated series number value
    """
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n - 2, n0, n1) + sum_series(n - 1, n0, n1)
