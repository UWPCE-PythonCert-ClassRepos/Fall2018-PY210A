import sys


def fibonacci(n):
	#list the simple cases for n
	if n == 0 or n == 1:
		return n
	#recursion function
	else:
		return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
	#just like the fibonacci function, list the simple cases and 
	#uses recursion
	if n == 0:
		return 2
	elif n == 1:
		return 1
	else:
		return lucas(n-1) + lucas(n-2)

#n if the required parameter to determine which element in the series to print
#y and z are optional parameters to determine the default values
def sum_series(n, y = 0, z = 1):
	if n == 0:
		return y
	elif n == 1:
		return z
	else: 
		return sum_series(n-1, y, z) + sum_series(n-2, y, z)



#print(fibonacci(int(sys.argv[1])))
#print(lucas(int(sys.argv[1])))
if len(sys.argv) < 3:
    print(sum_series(int(sys.argv[1])))
else:    
    print(sum_series(int(sys.argv[1]), int(sys.argv[2]) , int(sys.argv[3])))