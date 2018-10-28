#!/usr/bin/env python3

#Author: Carol Farris
#File Name: break_me.py
#Content: Write four simple python functions that throw errors


#The function below will throw a name error if supplied an undefined value
def cause_name_error(val):
    try:
        print(val)
    except NameError:
        print("Name Error. Did you define your variable?")


#the function below will throw a type error if the supplied variable
#is not valid for the action
def cause_type_error(val):
	try: 
		print(val//2)
	except TypeError:
		print("TypeError! The variable passed is invalid for the desired action.")	

#The function below will throw a syntax error because the print statement
#was incorrectly written. A perenthesis needs to surround ("hello")
#It needs to be commented out or the script wont run.
"""def cause_syntax_error():
    try:
        print "hello"
    except SyntaxError:
        print("Syntax Error! ")	"""

##This function will append to lists and other objects that carry the append
#attribute. parameters passed that lack the append attribute will cause
#attribute error to be thrown.
def cause_attribute_error(attr):
    mylist = [1,2,3]
    try:
        attr.append(mylist)
        print(attr)
    except AttributeError:
        print("Attribute Error! You attempted to append to something that lacks the append attribute.")





#Main:
too = "this is text!"
turkey= [1,2,3]
#cause_name_error(val)
#cause_type_error(too)
#cause_syntax_error()
cause_attribute_error(turkey)#This does not throw an exception
cause_attribute_error(too) #this will


