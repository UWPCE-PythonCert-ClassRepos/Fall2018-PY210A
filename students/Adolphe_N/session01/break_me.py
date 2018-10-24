#Python assignment 1

#most common exceptions

'''
this function returns an NameError exception because 'name' is not defined
'''
def my_name():
    
    return name

'''
this function returns an typeError exception because 'hello' is string and cant be divided by integer
'''
def type():
    
    x = 5/ "hello"
    print (x)

'''
this function returns a syntaxError exception because of unrecognized user of math operator sign
'''
def syntaxError():
#    y ===5
    pass
'''
this function returns an Attribute_Error exception because 'limit' is not a property of 'set'
'''
def Attribute_Error():
    set.limit()


#my_name()
#type()
#syntaxError
Attribute_Error()
