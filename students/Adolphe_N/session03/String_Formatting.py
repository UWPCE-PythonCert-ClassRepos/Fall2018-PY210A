#! python3

#Task 1: format string that takes a 4 element tuple and produces: 
#'file_002 :   123.46, 1.00e+04, 1.23e+04'
The_tuple = ( 2, 123.4567, 10000, 12345.67)

def format_tuple(t):
    '''
    :param t: four element tuple returns string with filename, floating point number, integer, and long floating point number
    '''
    #filename with leading zeros
    str_name = 'file_{:03d}'.format(t[0])
    
    #Floating point number with 2 decimals
    str_float = '{:.2f}'.format(t[1])
    
    #Scientific notation 
    str_int = '{:.2e}'.format(t[2])
    
    #long floating point number
    str_long_float = '{:3.2e}'.format(t[3])
    
    return '{}, {}, {}, {}'.format(str_name, str_float, str_int, str_long_float)

print (format_tuple(The_tuple))

# Task 2
print('\nTask Two')

def format_tuple2():
    
    pass

#Task 3
print('\nTask Three')

def formatter(in_tuple):
    '''
    Dynamically Building up format strings
    '''
    str_form = 'the {} numbers are: '
    numbers = []
    
    for item in in_tuple:
        numbers.append('{:d}')
    str_form += ', '.join(numbers)
    
    return str_form.format(len(in_tuple), *in_tuple)
# Tests
tuple_1 = (2, 3, 5)
print(formatter(tuple_1))

tuple_2 = (2, 3, 5, 7, 9)
print(formatter(tuple_2))

#Task 4
print('\nTask Four')

tuple_5 = (4, 30, 2017, 2, 27)

#use string formatting to print '02 27 2017 04 30'

def format_numbers(t):
    
    return'{:02d} {} {} {:02d} {}'.format(t[3], t[4], t[2], t[0], t[1])
print(tuple_5)
print(format_numbers(tuple_5))

# Task Five
print("\nTask Five")

# Use this four element list
element_list = ["oranges", 1.3, "lemons", 1.1]

# Print sentence
print(f'The weight of an {element_list[0][:-1]} is {element_list[1]} and the weight of a {element_list[2][:-1]} is {element_list[3]}.')

# Change fruit names to upper case and make the weight 20% higher (1.2 x)
print(f'The weight of an {element_list[0][:-1].upper()} is {element_list[1]*1.2} and the weight of a {element_list[2][:-1].upper()} is {element_list[3]*1.2}.')

# Task Six
print("\nTask Six")

headers = ("Students", "ID", "Grade")

students = [("Hema", 1324, 3.5), ("Mark", 4253, 3.6), ("Parker", 1983, 4.0), ("Kam", 1002, 3.9)]

# Print a table of several rows, but make sure things are aligned


def print_table(l):
    print("{:10}{:>10}{:>15}".format(*headers))

    for x in l:
        print("{:10}{:>10}{:>15}".format(x[0], x[1], ("{0:,.2f}".format(x[2]))))


# Test
#print_table(animals)

print("\nBonus")
tuple_10 = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

