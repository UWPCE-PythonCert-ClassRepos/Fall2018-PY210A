def fibonacci(n):
    '''Add a function called fibonacci.
    The function should have one parameter n.
    The function should return the nth value in the fibonacci series
    (starting with zero index).'''
    list = [0, 1]
    while len(list) < n+1:
        newlist = [list[len(list)-2] + list[len(list)-1]]
        newlist = list + newlist
        list = newlist
    return list[n]

def lucas(n):
    '''The Lucas Numbers are a related series of integers that start
    with the values 2 and 1 rather than 0 and 1.
    The function should return the nth value in the lucas series
    (starting with zero index).'''
    list = [2, 1]
    while len(list) < n+1:
        newlist = [list[len(list)-2] + list[len(list)-1]]
        newlist = list + newlist
        list = newlist
    return list[n]

def sum_series(n, a = 0, b = 1):
    '''Add a third function called sum_series with one required parameter
    and two optional parameters.
    The required parameter will determine which element in the series to print.
    The two optional parameters will have default values of 0 and 1 and will
    determine the first two values for the series to be produced.'''
    list = [a , b]
    while len(list) < n+1:
        newlist = [list[len(list)-2] + list[len(list)-1]]
        newlist = list + newlist
        list = newlist
    return list[n]

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