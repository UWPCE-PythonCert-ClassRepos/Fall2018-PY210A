#problem 1: print a grid that is equal height and width

def print_grid1():
    #print top row + inbetween rows
    print("+" + "-" * 2 + "+" + "-" * 2 + '+')
    print("|" + " " * 2 + "|" + " " * 2 + '|')
    print("|" + " " * 2 + "|" + " " * 2 + '|')
    #print middle row
    print("+" + "-" * 2 + "+" + "-" * 2 + '+')
    print("|" + " " * 2 + "|" + " " * 2 + '|')
    print("|" + " " * 2 + "|" + " " * 2 + '|')
    #print bottom row
    print("+" + "-" * 2 + "+" + "-" * 2 + '+')


#problem 2: print a grid that changes depending on input integer
def print_grid2(n):
    #determine half of n - account for rounding
    half_n = n // 2

    #top line of grid
    print('+' + '-' * n + '+' + '-' * n + '+')
    for i in range(half_n):
        print("|" + " " * n + "|" + " " * n + '|')

    #center line of grid
    print('+' + '-' * n + '+' + '-' * n + '+')

    for i in range(half_n):
        print("|" + " " * n + "|" + " " * n + '|')

    #bottom line of grid
    print('+' + '-' * n + '+' + '-' * m + '+')


#problem 3: Write a function that draws a similar grid with a specified number of rows and columns, and with each cell a given size.
def print_grid3(rows, columns):
    plus = '+'
    width = '|'
    for i in range(rows):
        plus += (' -' * columns) + ' +'
        width += ('  ' * columns) + ' |'

    print(plus)
    for i in range(rows):
        for i in range(columns):
            print(width)
        print(plus)