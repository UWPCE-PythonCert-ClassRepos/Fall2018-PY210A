# Lesson 02 Exercise: Grid Printer

# Part 1: Write a function that draws a grid like the example


def standard_grid():
    # Top row
    print("+ " + "- " * 4 + "+ " + "- " * 4 + "+")

    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|")

    # Middle row
    print("+ " + "- " * 4 + "+ " + "- " * 4 + "+")

    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|")

    # Bottom row
    print("+ " + "- " * 4 + "+ " + "- " * 4 + "+")


# Test
print("Standard Grid")
standard_grid()

# Part 2: Write a function that prints the grid size according to an integer


def print_grid(n):
    half = n // 2

    # Top row
    print("+ " + "- " * half + "+ " + "- " * half + "+")

    for i in range(half):
        print("| " + " " * (half * 2) + "| " + " " * (half * 2) + "|")

    # Middle row
    print("+ " + "- " * half + "+ " + "- " * half + "+")

    for i in range(half):
        print("| " + " " * (half * 2) + "| " + " " * (half * 2) + "|")

    # Bottom row
    print("+ " + "- " * half + "+ " + "- " * half + "+")


# Tests
print("Scalable Grids")
print_grid(3)
print_grid(15)

# Part 3: Write a function that takes in a specified table size and cell size


# Function to make a single header row
def make_row(table_size, cell_size):
    for i in range(table_size):
        print("+ " + "- " * cell_size, end="")
    print("+")


# Function to make a single column row
def make_column(table_size, cell_size):
    for i in range(table_size + 1):
        print("| " + " " * (cell_size * 2), end="")
    print()


# Function to make a scalable grid
def print_grid2(table_size, cell_size):
    for i in range(table_size):
        make_row(table_size, cell_size)

        for k in range(cell_size):
            make_column(table_size, cell_size)
    make_row(table_size, cell_size)


# Tests
print("Customizable Grids")
print_grid2(3, 4)
print_grid2(5, 3)
