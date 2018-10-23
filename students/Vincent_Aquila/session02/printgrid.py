"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
assignment objective: grid
"""

#Part 1
#Function for top, middle, and bottom of grid
def grid_one():
	print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')

#Function for intermediate lines of grid
def grid_two():
	print('|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|')

#Call each line by the grid function to create grid of 4 dashes by 4 posts
if __name__ == "__main__":
	grid_one()
	grid_two()
	grid_two()
	grid_two()
	grid_two()
	grid_one()
	grid_two()
	grid_two()
	grid_two()
	grid_two()
	grid_one()


#Part 2 variable height/width is determined by n
def print_grid(n):
	print('+', ('-'' ' * n), '+', ('-'' ' * n), '+')
	for i in range(n):
		print('|', (' '' ' * n), '|', (' '' ' * n), '|')
	print('+', ('-'' ' * n), '+', ('-'' ' * n), '+')
	for i in range(n):
		print('|', (' '' ' * n), '|', (' '' ' * n), '|')
	print('+', ('-'' ' * n), '+', ('-'' ' * n), '+')
print_grid(15)


#Part 3
"""
print a grid of any height by any width; change the number of dashes and number
of spaces in the grid function to alter the size of individual squares
"""
def grid(row, column):
	space = '\n' + '+----'*column + '+\n'
	return space + ('|    '*column + '|' + space)*row
print(grid(5,4))
