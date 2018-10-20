# Lesson 02 Exercise: Grid Printer

# Part 1: Write a function that prints a grid like the example.


def standard_grid():
    # Top row
    print("+ " + "- " * 4 + "+ " + "- " * 4 + "+")

    print("| " + " " * 8 + "| " + " " * 8 + "|")
    print("| " + " " * 8 + "| " + " " * 8 + "|")
    print("| " + " " * 8 + "| " + " " * 8 + "|")
    print("| " + " " * 8 + "| " + " " * 8 + "|")

    # Middle row
    print("+ " + "- " * 4 + "+ " + "- " * 4 + "+")

    print("| " + " " * 8 + "| " + " " * 8 + "|")
    print("| " + " " * 8 + "| " + " " * 8 + "|")
    print("| " + " " * 8 + "| " + " " * 8 + "|")
    print("| " + " " * 8 + "| " + " " * 8 + "|")

    # Bottom row
    print("+ " + "- " * 4 + "+ " + "- " * 4 + "+")


# Test
print("Standard Grid")
standard_grid()
print()

# Part 2: Write a function that prints the grid size based on an integer.


def print_grid(n):
    # Figure out what half of the grid should be
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
print()

# Part 3: Write a function that prints the grid using a specific table size and cell size.


# Function to make a single header row
def make_row(table_size, cell_size):
    for i in range(table_size):
        print("+ " + "- " * cell_size, end="")
    print("+")


# Function to make a single column row
def make_column(table_size, cell_size):
    for i in range(table_size):
        print("| " + " " * (cell_size * 2), end="")
    print("|")


# Function to make a scalable grid
def print_grid2(table_size, cell_size):
    for i in range(table_size):
        make_row(table_size, cell_size)

        for i in range(cell_size):
            make_column(table_size, cell_size)
    make_row(table_size, cell_size)


# Tests
print("Customizable Grids")
print_grid2(3, 4)
print_grid2(5, 3)
