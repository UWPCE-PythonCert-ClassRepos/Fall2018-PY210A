#!/usr/bin/env python

'''
Author: Jim Jenkins (dvlupr)
Date: 10/16/2018
Write a function that draws a grid.
'''

# user input variables
x = int(input('Enter the box size: '))
a = int(input('Enter the number of boxes: '))


# create the function to create the grid
def fn_grid(x, a):
    for j in range(a):
        print(('+' + (' -' * x) + ' ') * a + '+')
        for i in range(x):
            print(('|' + ('  ' * x) + ' ') * a + '|')
    print(('+' + (' -' * x) + ' ') * a + '+')


# format the view
print('-----' * 7)


# run the fundtion based on user input
fn_grid(x,a)


# format the view
print('-----' * 7)