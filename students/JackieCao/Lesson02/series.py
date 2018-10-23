# Fibonacci Series

def fibonacci(n):
    """
    make sure the input n is an integer and larger or equal to 0
    """
    if n != int(n):
        if not isinstance(n,int):
            print("n must be integer")
    elif n < 0:
        print("n must be larger or equal to 0")
    else:
        n = int(n)
        if n >= 2:
            """
            make an empty list has length n+1, n start from 0 
            the first two values are 0 and 1 for the Fibonacci series
            """
            L = [None]*(n+1)
            L[0] = 0 
            L[1] = 1
            for i in range(2,n+1):
                """
                this equation is based on the Fibonacci definition
                """
                L[i] = L[i-2]+L[i-1] 
            return(L[n]) #print the output
        if n == 0:
            return(0)	    
        if n == 1:
            return(1)	    

# Lucas Numbers


def lucas(n):
    # make sure the input n is an integer and larger or equal to 0
    if n != int(n):
        if not isinstance(n,int):
            print("n must be integer")
    elif n < 0:
        print("n must be larger or equal to 0")
    else:
        n = int(n)
        if n >= 2:
            L = [None]*(n+1) # make an empty list has length n+1, n start from 0 
            L[0] = 2 # the first two values are 2 and 1 for the Lucas series
            L[1] = 1
            for i in range(2,n+1):
                L[i] = L[i-2]+L[i-1] # this equation is based on the Lucas definition
            return(L[n]) # print the output
        if n == 0:
            return(2)	    
        if n == 1:
            return(1)	    


# sum_series

def sum_series(n, n0=0, n1=1):
    # make sure the input n is an integer and larger or equal to 0
    if n != int(n):
        if not isinstance(n,int):
            print("n must be integer.")
    elif n < 0:
        print("n must be larger or equal to 0.")
    else:
        n = int(n)
        if n >= 2:
            L = [None]*(n+1) # make an empty list has length n+1, n start from 0 
            L[0] = n0 # the first two values are n0 and n1
            L[1] = n1
            for i in range(2,n+1):
                L[i] = L[i-2]+L[i-1] # this equation is based on the Fibonacci definition
            return(L[n]) # print the output
        if n == 0:
            return(n0)	    
        if n == 1:
            return(n1)	    


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
    assert sum_series(5,2,1) == lucas(5)

    print("tests passed")


