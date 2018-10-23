
#fibonacci series exercise
def fibonacci(n):
    """This is the Fibonacci function that will return the nth value. This series starts with 0 and 1"""
    a=0
    b=1
    #comment out all but the last of the print statements if you don't want to see the count increase
    #print(a)
    #print(b)
    for i in range(n-2):
        c=a+b
        #print(c)
        a=b
        b=c
    #print(f'the {i+3}th number in the fibonacci sequence is {c}')
    return(c)

#lucas numbers series exercise
def lucas(n):
    """This is the Lucas Numbers function that will return the nth value. This series starts with 2 and 1"""
    a=2
    b=1
    #comment out all but the last of the print statements if you don't want to see the count increase
    #print(a)
    #print(b)
    for i in range(n-2):
        c=a+b
        #print(c)
        a=b
        b=c
    #print(f'the {i+3}th number in the lucas number sequence is {c}')
    return(c)
#the sum series function that
def sum_series(n,n2 = 0,n3 = 1):
    """This is the sum seires function that will return the nth value in a series of numbers. 1st option returns the nth number and the 2nd and 3rd option sets the beginning of the series. Default is 0 and 1 for fibonacci"""
    a=n2
    b=n3
    #comment out all but the last of the print statements if you don't want to see the count increase
    #print(a)
    #print(b)
    for i in range(n-2):
        c=a+b
        #print(c)
        a=b
        b=c
    return(c)

#validating functions
if __name__=="__main__":
    assert fibonacci(12) == 89
    assert lucas(12) == 199
    assert sum_series(8,2,1) == 29
    assert sum_series(8) == 13
    print("assertions are valid")
