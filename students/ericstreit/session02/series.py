
#fibonacci series exercise
def fibonacci(n):
    """This is the Fibonacci function that will return the nth value"""
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
    """This is the Lucas Numbers function that will return the nth value"""
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
#validating functions
if __name__=="__main__":
    #fibonacci(14)
    assert fibonacci(12) == 89
    assert lucas(12) == 199
    print("assertions are valid")
