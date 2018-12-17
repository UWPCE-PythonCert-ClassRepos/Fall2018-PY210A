#!/usr/bin/env python

print('\nTask1\nFormat String')

X = ( 2, 123.4567, 10000, 12345.67)

print('{:003d} : {:.2f}, {:.2e}, {:.3g}'.format(X[0], X[1], X[2], X[3]))

###################

print('\nTask2\nAlternative Format String')

print('%03d : %.2f, %.2e, %.3g' % (X[0], X[1], X[2], X[3]))

##################

print('\nTask3\nDynamically build up')

# Rewrite: 'The 3 numbers are: {:d}, {:d}, {:d} .format(1,2,3)'

t = (1, 2, 3)

def formatter(t):
    format_string = 'The {:d} numbers are:'.format(len(t))
    format_string += ", ".join(['{:d}'] * len(t))
    return format_string.format(*t)

#################

print('\nTask4')

# Use string formating to print: '02 27 2017 04 30'

t = ( 4, 30, 2017, 2, 27)
print('{:0d} {:d} {:d} {:0d} {:d}'.format(t[3], t[4], t[2], t[0], t[1]))


#################

print('\nTask5')

['oranges', 1.3, 'lemons', 1.1]

#Write an f-string that will display:
#The weight of an orange is 1.3 and the weight of a lemon is 1.1

F = ['orange', 'lemon']
W = [1.3, 1.1]

print(f'The weight of an {F[0]} is {W[0]} and the weight of a {F[1]} is {W[1]}')
print(f'The weight of an {F[0].upper()} is {W[0]*1.2} and the weight of a {F[1].upper()} is {W[1]*1.2}')

#################

print('\nTask6\nPositions')

'''Write some Python code to print a table of several rows,
each with a name, an age and a cost. Make sure some of the costs
are in the hundreds and thousands to test your alignment specifiers.'''

data = [{'Age': 2, 'Type': 'Condo', 'Cost': 100000 },
        {'Age': 3, 'Type': 'Town House', 'Cost': 200000},
        {'Age': 10, 'Type': 'House', 'Cost': 300000}]

def print_table():

    '''make a string that prints the header'''

    header = '{:^10}|{:^10}|{:^10}'.format('Type', 'Age', 'Cost')
    rows = [row.values()]
    str_format=[]
    for row in rows:
        str_format += ['{:<10}|{:^10}|{:^10}'.format(row[2], row[1],row[0])]

    return header + '\n'.join(str_format)



