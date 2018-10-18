#! usr/bin/env python

#Create function for line one of the grid
def grid_lineOne():
	print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')

#Create function for line two of the grid
def grid_lineTwo():
	print('|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|')


#Called each line by the line function to create grid
if __name__ == "__main__":
	grid_lineOne()
	grid_lineTwo()
	grid_lineTwo()
	grid_lineTwo()
	grid_lineTwo()
	grid_lineOne()
	grid_lineTwo()
	grid_lineTwo()
	grid_lineTwo()
	grid_lineTwo()
	grid_lineOne()

#Part 2 """add a variable for each line so I do not have to repeat each code of line more tha once"""
def print_grid(n):
	print('+', ('-'' ' * n), '+', ('-'' ' * n), '+')
	for i in range(n):
		print('|', (' '' ' * n), '|', (' '' ' * n), '|')
	print('+', ('-'' ' * n), '+', ('-'' ' * n), '+')
	for i in range(n):
		print('|', (' '' ' * n), '|', (' '' ' * n), '|')
	print('+', ('-'' ' * n), '+', ('-'' ' * n), '+')
print_grid(3)

#Part 3
def grid(row, col):
	sep = '\n' + '+---'*col + '+\n'
	return sep + ('|   '*col + '|' + sep)*row


print(grid(3,7))