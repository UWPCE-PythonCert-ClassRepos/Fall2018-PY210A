import math

def NameErrorTest():
    print("print this " % myVariable)

def TypeErrorTest():
    names = ["Bob", "Sue"]
    count = 2
    total = names + count

#def SyntaxErrorTest()
#    print("I won't make it here")

def AttributeErrorTest():
    return math.fakeMethod()