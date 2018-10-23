# Fibonacci Series

def fibonacci(n):
"""
make sure the input n is an integer and larger or equal to 0
"""
    if n != int(n):
        if not isinstance(n,int):
 	    print("Hey, there's an error, n must be integer.")
    elif n < 0:
	print("Hey, there's an error, n must be larger or equal to 0.")
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
	    print(L[n]) #print the output
        if n == 0:
	    print(0)	    
        if n == 1:
	    print(1)	    
   
print("START TEST")
fibonacci(0)
fibonacci(1)
fibonacci(5)
fibonacci(8)
fibonacci(4.5)
fibonacci(-1)
fibonacci(7.0)

# Lucas Numbers


def lucas(n):
#make sure the input n is an integer and larger or equal to 0
    if n != int(n):
        if not isinstance(n,int):
 	    print("Hey, there's an error, n must be integer.")
    elif n < 0:
	print("Hey, there's an error, n must be larger or equal to 0.")
    else:
	n = int(n)
	if n >= 2:
	    L = [None]*(n+1) #make an empty list has length n+1, n start from 0 
            L[0] = 2 #the first two values are 0 and 1 for the Fibonacci series
	    L[1] = 1
            for i in range(2,n+1):
	        L[i] = L[i-2]+L[i-1] #this equation is based on the Fibonacci definition
	    print(L[n]) #print the output
        if n == 0:
	    print(2)	    
        if n == 1:
	    print(1)	    
   
print("START TEST")
lucas(0)
lucas(1)
lucas(5)
lucas(8)
lucas(4.5)
lucas(-1)
lucas(7.0)



