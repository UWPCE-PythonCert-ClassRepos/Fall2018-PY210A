# Lesson 02 Exercise: Grid Printer

# Part 1: Write a function that draws a gird like the example


def print_grid():
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

print_grid()
