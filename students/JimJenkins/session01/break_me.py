#!/usr/bin/env python

'''
Author: Jim Jenkins (dvlupr)
Date: 10/13/2018

<<<<<<< HEAD
'''

# functions returns a name error because hello is not defined.
def nameerror():
    print (hello)
    return nameerror


# function returns a type error because the equation expects an int and has a str
def typeerror():
    x = 4 / "Hello World"
    return typeerror


# function returns a syntax error because the equation has a spelling error for while
def syntaxerror():
    whille x % 2 == 0
    return syntaxerror


# function returns an attribute error because the int attribute doesn't have append
def attributeError():
    int.append (5)
    return attributeerror


# calling the functions
nameerror()
typeerror()
syntaxerror()
attributeError()


