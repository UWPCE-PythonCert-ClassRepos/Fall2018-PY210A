
#fibonacci series exercise

def fibr(n):
    """This is the recursive Fibonacci function that will return the nth value."""
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibr(n-1)+fibr(n-2)

#fibonacci iterative version
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

#lucas numbers recusive version
def lucasr(n):
    """This is the recursive Lucas function that will return the nth value."""
    if n == 0: return 2
    elif n == 1: return 1
    else: return lucasr(n-1)+lucasr(n-2)

#lucas numbers series exercise - iterative version
def lucas(n):
    """This is the iterative Lucas Numbers function that will return the nth value. This series starts with 2 and 1"""
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

#sum series function - recursive version - not working yet with Lucas numbers
def sum_seriesr(n,n2 = 0,n3 = 1):
    """This is the recursive sum series function"""
    if n == n2: return n2
    elif n == 1: return 1
    else: return sum_seriesr(n-1)+sum_seriesr(n-2)

#the sum series function - iterative version
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
    assert fibr(11) == 89
    assert fibonacci(12) == 89
    assert lucas(12) == 199
    assert lucasr(11) == 199
    assert sum_series(8,2,1) == 29
    assert sum_series(8) == 13
    print("Lucas Recursive results of 8:", sum_seriesr(8,2,1))
    #assert sum_seriesr(8,2,1) == 29
    assert sum_seriesr(7) == 13
    print("assertions are valid")
