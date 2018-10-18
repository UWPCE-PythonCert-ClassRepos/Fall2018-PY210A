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
        if index % 2 == 0:
            square_width += " "
        else:
            square_width += "-"
    divide =  "+" + square_width + "+" + square_width + "+"
    length = "|" + (" " * n) + "|" + (" " * n) + "|"
    print(divide)
    for __ in range(3):
        for __ in range(n):
            print(length)
        print(divide)