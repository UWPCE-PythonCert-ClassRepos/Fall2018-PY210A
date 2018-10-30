
def fibonacci(n):
    """return the nth value index n in the fibonacci sequence"""
    x = 0
    y = 1

    fib = [x,y]
    for i in range(n):
        x,y = y, x+y
        fib.append(y)
    return fib[n]


def lucas(n):
    """return the nth value index n in the Lucas sequence, which starts with 2, 1 instead of 0,1 like fibonacci"""
    x = 2
    y = 1

    lucas = [x,y]
    for i in range(n):
        x,y = y, x+y
        lucas.append(y)
    return lucas[n]


def sum_series(n, x = 0, y = 1):
    series = [x, y]
    for i in range(n):
        x,y = y, x + y
        series.append(y)
    return series[n]



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