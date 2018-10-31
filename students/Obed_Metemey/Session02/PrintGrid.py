
"""
/usr/bin/env -- Python3
Printing a Grid
Author : OM
"""

# Part 1
# This code prints a simple grid


# Part 2
# This code prints a function print_grid(n) that takes one integer argument and prints a grid with the size of the grid given by the argument.


def print_grid(n):

    print("+" + "-" * n + "+" + "-" * n + "+")
    print("|" + " " * n + "|" + " " * n + "|")
    print("+" + "-" * n + "+" + "-" * n + "+")
    print("|" + " " * n + "|" + " " * n + "|")
    print("+" + "-" * n + "+" + "-" * n + "+")


# example
print_grid(4)


# Part 3
# This code draws a similar grid function twith a specified number of rows and columns, and with each cell a given size.


def vertical(symbol, spaces):
    for i in range(symbol):
        print("| " + " " * spaces, end="")
    print("|")


def horizontal(symbol, spaces):
    for i in range(symbol):
        print("+ " + "- " * spaces, end="")
    print("+")


def print_grid(symbol, spaces):
    for x in range(symbol):
        horizontal(symbol, spaces)

        for y in range(spaces):
            vertical(symbol, spaces)
    horizontal(symbol, spaces)


# example
print_grid(2, 3)
