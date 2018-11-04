#! python3

#Task 1: format string that takes a 4 element tuple and produces: 
#'file_002 :   123.46, 1.00e+04, 1.23e+04'
The_tuple = ( 2, 123.4567, 10000, 12345.67)

def format_tuple(t):
    '''
    :param t: four element tuple returns string with filename, floating point number, integer, and long floating point number
    '''
    #filename with leading zeros
    file_name = 'file_{:03d}'.format(t[0])
    
    #Floating point number with 2 decimals
    
    
    return '{} :'.format(file_name)

print (format_tuple(The_tuple))