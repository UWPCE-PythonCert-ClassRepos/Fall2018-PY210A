#!/usr/bin/env Python3

#Date: October 23, 2018
#Created by: Carol Farris
#Purpose: Practice Fibonacci sequence
#Note: I wanted to try to include negative fibonacci numbers but couldn't quite get it to work!

import math

#returns the fibonacci number of the nth sequence for positive integers
def fibonacci(n):
    if n < 0 :
    	return "Please specify a positive integer"
    #    return math.pow(-1, (n+1))* ((n))
    elif n == 0 :
        return 0	
    elif n == 1 :
        return 1
    else : 	
        return (fibonacci(n-2) + fibonacci(n - 1)) 

#returns the lucas number of the nth sequence for positive integers
def lucas(n):
    if n < 0 :
        return "Please specify a positive integer"
    elif n == 0 :
        return 2
    elif n == 1 :
        return 1
    else :
        return (lucas(n-2) + lucas(n - 1))


#Function that returns fibonacci/lucas like algorithm with user specified n0 and n1
# fib n0=0 n1=1  lucas n0=2 n1=1
def sum_series(n, n0=0, n1=1):
    count = 0
    n0 = n0
    n1 = n1
    if n < 0:
        return "Please specify a positive integer"
    elif n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        for i in range (0, n+1):
            if i == 0:
                count = n0
            if i == 1:
            	count = n1
            if i > 1:
                count = n0 + n1
                n0 = n1
                n1 = count
    return (count)
            



#This is a brief check to ensure I am testing my assertion errors
#by running with name == __main__
print("name is: ", __name__)

if __name__ == "__main__":

    assert fibonacci(0)  == 0
    assert fibonacci(1)  == 1
    assert fibonacci(2)  == 1
    assert fibonacci(3)  == 2
    assert fibonacci(4)  == 3
    assert fibonacci(5)  == 5
    assert fibonacci(6)  == 8
    assert fibonacci(7)  == 13

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    #test sum_series to ensure it returns accurate values for Fib and lucas numbers
    assert sum_series(0,2,1) == 2
    assert sum_series(1,2,1) == 1
    assert sum_series(2,2,1) == 3
    assert sum_series(3,2,1) == 4
    assert sum_series(4,2,1) == 7
    assert sum_series(5,0,1) == 5
    assert sum_series(6,0,1) == 8









    

