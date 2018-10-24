#!usr/bin/env python

#Fibonacci definition using recursion
def fibonacci(n):
    """Recursive Function to compute nth Fib number"""
    #If n is 0 or 1, return 0 or 1
    if n == 0:
    	return 0
    if n == 1:
        return 1

    # When n is >1, use recursion 
    else:
       return fibonacci(n-2) + fibonacci(n-1)

# Fibonacci using sum_series 
def fibonacci2(n):
    """Return the nth value based on the Fibonacci series"""
    return sum_series(n)
	

#Lucas numbers
#Lucas function that that start with 2 and 1
def lucas(n):
	#Return 2 and 1 if n is 0 and 1 respectively 
	if n == 0:
		return 2
	elif n == 1:
		return 1
	
	#If >1 use recursion
	elif n > 1:
		return lucas(n - 2) + lucas(n - 1)

# Lucas function sum_series function 
def lucas2(n):
    """Return the nth value based on the Lucas series"""
    return sum_series(n, 2, 1)

#Sum Series
def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series
    
    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n)."""

    # Base of series
    if n == 0:
        return n0
    elif n == 1:
        return n1

    # If n is > 1, use recursion 
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





