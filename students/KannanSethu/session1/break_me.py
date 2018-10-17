#!/usr/bin/python


###########################################################################################
###  FUNCTION DEFINITIONS 
###########################################################################################


#def exception_SyntaxError():
#    '''Function to demonstrate SyntaxError exception raised by Python interpreter'''
#	print "Hello world"

#def execption_TypeError():
#    '''Function to demonstrate inbuilt TypeError exception raised by Python interpreter'''
#	x = 5 + "five"
#
#execption_TypeError()

#def exception_NameError():
#	'''Function to demonstrate inbuilt NameError exception raised by Python interpreter''' 
#	x = []
#	y = x + z 
#
#exception_NameError()

def exception_AttributeError():
	'''Function to demonstrate inbuilt AttributeError exception raised by Python interpreter'''
	x = ["Kannappan Sethunarayanan"]
	first_name = x.split()[0]
	print (first_name)

exception_AttributeError()