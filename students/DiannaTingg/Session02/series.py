# Lesson 02 Exercise: Fibonacci Series

# Step 1 - Fibonacci Series

def fibonacci(n):
    """Return the nth value based on the Fibonacci series (0, 1, 1, 2...)"""

    # Define base cases (n is 0 or 1)
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # If n is higher than 1, use recursion to find answer
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


# Fibonacci function using sum_series function
def fibonacci2(n):
    return sum_series(n)


# Step 2 - Lucas Numbers (2, 1, 3, 4, 7, 11, 18, 29, ...)


def lucas(n):
    """Return the nth value based on the Lucas series (2, 1, 3, 4...)"""

    # Define base cases (n is 0 or 1)
    if n == 0:
        return 2
    elif n == 1:
        return 1

    # If n is higher than 1, use recursion to find answer
    else:
        return lucas(n - 2) + lucas(n - 1)


# Lucas function using sum_series function
def lucas2(n):
    return sum_series(n, 2, 1)


# Step 3 - Sum Series (specify first two numbers or use default values)
def sum_series(n, n0=0, n1=1):
    """
    Return the nth value of a summation series.

    :param n0=0: Value of element at index 0 in the series. Default is 0.
    :param n1=1: Value of element at index 1 in the series. Default is 1.

    This function works for the first two numbers of a sum series.
    sum_series(n, 0, 1) is equivalent to fibonacci series
    sum_series(n, 2, 1) is equivalent to lucas numbers
    """

    # Define base cases
    if n == 0:
        return n0
    elif n == 1:
        return n1

    # If n is higher than 1, use recursion to find answer
    else:
        return sum_series(n - 2, n0, n1) + sum_series(n - 1, n0, n1)


# Tests
if __name__ == "__main__":
    # Check fibonacci function
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # Check fibonacci2 function
    assert fibonacci2(0) == 0
    assert fibonacci2(1) == 1
    assert fibonacci2(2) == 1
    assert fibonacci2(3) == 2
    assert fibonacci2(4) == 3
    assert fibonacci2(5) == 5
    assert fibonacci2(6) == 8
    assert fibonacci2(7) == 13

    # Check lucas function
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    # Check lucas2 function
    assert lucas2(0) == 2
    assert lucas2(1) == 1
    assert lucas2(4) == 7

    # Check sum_series function
    assert sum_series(5) == fibonacci(5)
    assert sum_series(5, 2, 1) == lucas(5)

print("Hooray!  Tests passed!")
