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

# Part 2 Write a function that prints the grid size according to an integer


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
print("Scalable Grid")
print_grid(3)
print_grid(15)
