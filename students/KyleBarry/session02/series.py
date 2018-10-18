def fibonacci(n):
    """Return the nth value (the index of the list) in fibonacci sequence.
    fib[n-1] to return the value in the n position"""

    a = 0
    b = 1

    fib = [a, b]
    for i in range(n):
        a,b = b, a+b
        fib.append(b)
    return fib[n]

def lucas(n):
    """Return the nth value (the index of the list) in the lucas numbers series.
    fib[n-1] to return the value in the n position"""

    a = 2
    b = 1

    luc = [a, b]
    for i in range(n):
        a,b = b, a+b
        luc.append(b)
    return luc[n]


def sum_series(n, a=0, b=1):
    """Return the nth value in the series given values for a and b as the starting
    points. If no params are given for a and b, default to 0,1 (fibonacci sequence)."""

    ser = [a, b]
    for i in range(n):
        a,b = b, a+b
        ser.append(b)
    return ser[n]

if __name__ == '__main__':

    #test that fibonnaci sequencing is accurage
    assert fibonacci(9) == 34
    #test that lucas number sequencing is accurate
    assert lucas(5) == 11

    #test that sum_series with default params return fibonacci sequence
    assert sum_series(4289) == fibonacci(4289)

    #test that sum_series with lucas number starting params returns lucas
    #numbers sequence
    assert sum_series(5, 2, 1) == lucas(5)
    assert sum_series(45, 2, 1) == lucas(45)
    print('All assertions passed!')
