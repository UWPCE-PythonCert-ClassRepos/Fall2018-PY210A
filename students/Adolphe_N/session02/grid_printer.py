#!/usr/bin/env python3

def print_grid():
     
    print("+ " + "- " * 4 + "+ " + "- " * 4 + "+") # Top row

    print("| " + " " * 8 + "| " + " " * 8 + "|")
    print("| " + " " * 8 + "| " + " " * 8 + "|")
    print("| " + " " * 8 + "| " + " " * 8 + "|")
    print("| " + " " * 8 + "| " + " " * 8 + "|")


    print("+ " + "- " * 4 + "+ " + "- " * 4 + "+")

    print("| " + " " * 8 + "| " + " " * 8 + "|")
    print("| " + " " * 8 + "| " + " " * 8 + "|")
    print("| " + " " * 8 + "| " + " " * 8 + "|")
    print("| " + " " * 8 + "| " + " " * 8 + "|")

    
    print("+ " + "- " * 4 + "+ " + "- " * 4 + "+")

    
print_grid()


'''
this function will print grid based on the parameters passed into it
'''
def print_adjustedGrid(n):
    
    print("+ " + n * "-" + "+ " + n * "-" + "+")

    print("| " + " " * n + "| " + " " * n +  "|")
    print("| " + " " * n + "| " + " " * n +  "|")
    print("| " + " " * n + "| " + " " * n +  "|")
    print("| " + " " * n + "| " + " " * n +  "|")

    print("+ " + n * "-" + "+ " + n * "-" + "+")

    print("| " + " " * n + "| " + " " * n +  "|")
    print("| " + " " * n + "| " + " " * n +  "|")
    print("| " + " " * n + "| " + " " * n +  "|")
    print("| " + " " * n + "| " + " " * n +  "|")

    print("+ " + n * "-" + "+ " + n * "-" + "+")

#print_adjustedGrid(15)

'''
this function will print the grid based on 2 input parameters
'''
def row(grid_size, cell_size):
    for i in range (grid_size):
        print("+ " + "- " * cell_size, end= '')
    print('+') 
    
def column (grid_size, cell_size):
    
    for i in range (grid_size):
        print ('| ' + ' '* (cell_size * 2), end = '')
    print ('|')
    
    
def grid(grid_size, cell_size):
    for i in range (grid_size):
        row(grid_size, cell_size)
        
        for j in range (cell_size):
            column(grid_size, cell_size)
    row(grid_size, cell_size)
    
#grid(3,5)



    