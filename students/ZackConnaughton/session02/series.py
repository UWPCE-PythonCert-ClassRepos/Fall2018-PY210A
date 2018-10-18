def fibonacci(n):
    """Returns as an integer the nth value in the fibanacci sequence"""

    i = 0
    j = 1
    for x in range(n-1):
        #print(str(i) + " " + str(j))
        j, i = add_values(i, j), j
    return i

def add_values(i, j):
    return i + j

def fibo(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas (n - 1)

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
