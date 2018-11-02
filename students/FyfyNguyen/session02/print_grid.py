# Part 1: print 2x2 grid 
PLUS = '+'
MINUS = '-'
SPACE = ' '
PIPE = '|'
DASH = (SPACE + MINUS) * 4 + SPACE

def print_grid1():
    row_one = PLUS + DASH + PLUS + DASH + PLUS + '\n'
    row_two = PIPE + (SPACE * 9) + PIPE + (SPACE * 9) + PIPE + '\n'
    print(row_one + row_two * 3 + row_one + row_two * 3 + row_one)
print_grid1()


# Part 2: write a function print_grid(n) that takes integer argument
PLUS = '+'
MINUS = '-'
SPACE = ' '
PIPE = '| '

def print_grid2(n):
    DASH = (SPACE + MINUS) * n + SPACE
    row_one = PLUS + DASH + PLUS + DASH + PLUS + '\n'
    row_two = PIPE + "  " * n + PIPE + "  " * n + PIPE + '\n'
    print(row_one + row_two * n + row_one + row_two * n + row_one)
print_grid2(12)


# Part 3: write function with two parameters for row and columns, and cell size
PLUS = '+'
MINUS = '-'
SPACE = ' '
PIPE = '| '

def print_grid3(grid_size, units):
    DASH = (SPACE + MINUS) * units + SPACE
    row_one = PLUS + DASH
    row_two = PIPE + "  " * units

    grid_one = row_one * grid_size + PLUS + '\n'
    grid_two = row_two * grid_size + PIPE + '\n'

    full_grid = grid_one + grid_two * units

    print(full_grid * grid_size + grid_one)
print_grid3(10,5)
