# PY210A - session02
# Cheng Liu
# A function that draws a grid with specified number of number of rows
# and columns, and with each cell a given size


def print_grid(sizes, units):
    """
    sizes: the # of rows/columns in the cell
    units: the # of repeated cells
    """

    row1 = '+' + ' -' * sizes + ' '
    row2 = '|' + '  ' * sizes + ' '
    cell = row1 * units + '+ \n' + (row2 * units + '| \n') * sizes
    grid = (cell * units)
    print(grid + row1 * units + '+ ')


print_grid(5, 3)
