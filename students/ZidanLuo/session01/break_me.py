def NameError ():
    print(x)

# Passing arguments of the wrong type should result in a TypeError
def TypeError(x):
    x = x + 1

def SyntaxError():
    print("error" + 1 + ' ')

def AttributeError(x,y):
    x = x + 1
    y = y + 1

NameError();
TypeError("str");
SyntaxError();
AttributeError(2);
