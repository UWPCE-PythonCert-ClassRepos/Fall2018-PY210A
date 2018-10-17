
# import random

# This is the NameError


def error_name():
    while True:

        try:
            print("..running the NameError...")
            num = random.random()
            print(num)
            print("Apparently no errors")
            break
        except NameError:
            print("This be a NameError")
            break

# This is the TypeError


def error_type():
    while True:

        try:
            print("...running the TypeError...")
            blank = "Hello"
            var = blank / 3
            break
        except:
            print("This be TypeError")
            break

# This is the SyntaxError

#def error_syntax():
#    while True:

#        try:
#            print("...running the SyntaxError...")
#            if 2 > 1
#                print("A")
#            break
#        except:
#           print("This be the SyntaxError...")
#            break

# This is the AttributeError

def error_attribute():
    while True:

        try:
            hello = "Howdy folks!"
            print("...running the Attribute Error...")
            print(hello.sum())
            break
        except:
            print("This be an Attribute Error...")
            break


error_name()
error_type()
error_attribute()

#error_syntax()


