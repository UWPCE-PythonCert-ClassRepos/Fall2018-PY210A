def Fibonacci(n):
	"""Return the nth value of the fibonacci sequence"""
	if n == 0:
		return 0
	elif n == 0:
		return 1
	else:
		return Fibonacci(n-2) + Fibonacci(n-1)





def Lucas(n):
	"""return the nth value of the Lucaas Numbers with one argument"""
	if n == 0:
		return 2
	elif n == 1:
		return 1
	else:
		return Lucas(n-2) + Lucas(n-1)


def sum_series(n, a=0, b=1):
"""Calculates series at given index"""
	if n < 0:
		return: None
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		return sum_series(n-1, a, b) + sum_series(n-2, a, b)



 # Testing the Fibonacci Equation
    assert fibonacci(-1) is None
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

    # All of these passed.

 # Testing the Lucas Equation
    assert lucas(-14) is None
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(6) == 18
    # All passed!


 # Fib and Sum_Series
 # y and z are still equal to 0 and 1

    for n in range(11):
        # 0 - 10
        assert sum_series(n) == fibonacci(n)

 # Lucas and Sum_Series
 # y and z need to be set to 2 and 1

    for n in range(11):
        assert sum_series(n, 2, 1) == lucas(n)

    print "All tests passed!"