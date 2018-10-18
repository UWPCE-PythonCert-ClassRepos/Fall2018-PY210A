#Function that produces a name error
def Name ():
    print(x)

#Passing arguments of the wrong type should result in a TypeError
def Type(x):
    x = x + 1

#define a function without colon will cause Syntax error
def Syntax()
    print("error")

#integer type object has no attribute "sort"
def Attribute():
    i = 10
    i.sort()

Name();
Type("str");
Syntax();
Attribute();
