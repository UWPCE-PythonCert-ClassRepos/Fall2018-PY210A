#!/usr/bin/env python3
# Function to explore error

# NameError: indicates that you have tried to use a symbol that is not bound to a value.
def nameErr(a):
    a *= 5
    return b

# TypeError: indicates that you have tried to use the wrong kind of object for an operation.
def typeErr(c, d):
    c += 5
    d = c + "wow"
    return d

# SyntaxError: indicates that you have mis-typed something.
def syntaxErr(f, g):
    h = f + g
#    retur h

# AttributeError: indicates that you have tried to access an attribute or method that an object does not have
# (this often means you have a different type of object than you expect)
def attributeErr(g):
    h = "still dk"
    return h
