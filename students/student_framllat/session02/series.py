a = int(input("How many nums shall I calculate for you? "))

def fibonacci(n):
    
    """This function calculates the nth value of a Fibonacci number
     starting at the zero index
    """
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def lucas(n):

    """This function calculates the nth value of a Lucas Number
     starting at the zero index
    """
    if n < 0:
        return None
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)

def sum_series(n, n0=0, n1=1):

    """This function attempts to calculate the nth value of a Series 
     starting at the zero index
    """
    if n < 0:
        return None
    elif n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)


fib_res = fibonacci(a)
luc_res = lucas(a)
#sum_res = sum_series(a, 0, 1)
sum_res = sum_series(a, 2, 1)

print("The Fibonacci -> ",fib_res)
print("The Lucas -> ",luc_res)
print("The Series -> ",sum_res)

if __name__ == "__main__":

## Tests to validate 

    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert lucas(4) == 7
    assert lucas(5) == 11

## Tests for the sum_series--With LUCAS params
    assert sum_series(5,2,1) == lucas(5)
    assert sum_series(1,2,1) == lucas(1)

## Tests for the sum_series--With FIBONACCI params
    assert sum_series(0,0,1) == 0
    assert sum_series(7,0,1) == fibonacci(7)

print("SUCCESS")
