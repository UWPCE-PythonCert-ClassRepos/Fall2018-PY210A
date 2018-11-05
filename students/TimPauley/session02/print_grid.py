#Tim Pauley
#Python Homework 2
#Date due: Oct 23 2018



def print_grid(size):

    number = 2
    box_size = int((size - 1) // 2)  # size of one grid box
    print("box_size:", box_size)
    # top row
    top = ('+ ' + '- ' * box_size) * number + '+' + '\n'
    middle = ('| ' + ' ' * 2 * box_size) * number + '|' + '\n'

    row = top + middle * box_size

    grid = row * number + top

    print(grid)





print_grid(7)

