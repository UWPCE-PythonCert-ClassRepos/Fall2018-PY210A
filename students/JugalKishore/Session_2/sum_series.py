#!/usr/bin/env python3

"""
1. Fibonacci Series Formula
F(n) = F(n-1) + F(n-2)
where:
      F(0) = 0
      F(1) = 1
      
2. Lucas series Formula
F(n) = F(n-1) + F(n-2)
where:
      F(0) = 2
      F(1) = 1
      
3. We will compute nth value of series using recrusive function startegy 
"""

# fibonacci function defination
def fibonacci(n):
    
    """
    required argument: integer n
    return: nth value of fibonacci series
    """
	
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# lucas function defination
def lucas(n):
    
    """
    required argument: integer n
    return: nth value of lucas series
    """
    
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

# generlize sum_series function defination        
def sum_series(n, x = 0, y = 1):
    
    """
    required argument: integer n
    optional argument x and y
    
    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    If x and y are different from above seed value then nth value of other series will be printed. 
    For this homework, other series = fibonacci(n) + lucas(n) + fibonacci(x) + lucas(x) + fibonacci(y) + lucas(y)
    """
    if x == 0 and y == 1:
        return fibonacci(n)
    elif x == 2 and y == 1:
        return lucas(n)
    else:
        return fibonacci(n) + lucas(n) + fibonacci(x) + lucas(x) + fibonacci(y) + lucas(y)
        
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