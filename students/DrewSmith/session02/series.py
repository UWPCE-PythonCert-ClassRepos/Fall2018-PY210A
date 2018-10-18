def fibonacci(n):
    """
    Returns the nth value in the fibonacci sequence
    
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
    Returns the nth value in the lucas sequence
    
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

def sum_series(n, first=0, second=1):
    """
    Returns the nth value in a sequence with a given start
    
    :param n: the zero based index in sequence to return
    :param first: the first value of the sequence
    :param second: the second value of the sequence
    """
    if n == 1:
        return second
    elif n <= 0:
        return first
    return sum_series(n -1, second, first + second)