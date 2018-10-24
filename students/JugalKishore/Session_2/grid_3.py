#!/usr/bin/env python3

def grid_3(row, width):
	for i in range (row):
		print (("+" + ("-")*width) * row + "+")
		for j in range (width):
			print(("|" + (" ")*width) * row + "|")
		if (i == row - 1):
			print (("+" + ("-")*width) * row + "+")
            

grid_3(4, 3)

#Output
'''
+---+---+---+---+
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
+---+---+---+---+
'''