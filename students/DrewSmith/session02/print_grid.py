def print_simple_grid():
    divide = "+ " + ("- " * 4) + "+ " + ("- " * 4) + "+"
    length = "| " + ("  " * 4) + "| " + ("  " * 4) + "|"
    print(divide)
    for __ in range(3):
        for __ in range(4):
            print(length)
        print(divide)

def print_grid(n):
    square_width = ""
    for index in range(n):
        square_width += " " if index % 2 == 0 else "-"

    divide =  "+" + square_width + "+" + square_width + "+"
    length = "|" + (" " * n) + "|" + (" " * n) + "|"
    print(divide)
    for __ in range(3):
        for __ in range(n):
            print(length)
        print(divide)

def print_grid2(grid, size):
    divide = "+"
    length = "|"
    for __ in range(grid):
        divide += (" -" * size) + " +"
        length += ("  " * size) + " |"        
    
    print(divide)
    for __ in range(grid):
        for __ in range(size):
            print(length)
        print(divide)