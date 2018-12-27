# Part 1
# One of the most basic scripts to draw the grid pattern
print (("+ " + "- " * 4 + "+ " + "- " * 4 + "+") + "\n" +
        ("| " + "  " * 4 + "| " + "  " * 4 + "|") + "\n" +
        ("| " + "  " * 4 + "| " + "  " * 4 + "|") + "\n" +
        ("| " + "  " * 4 + "| " + "  " * 4 + "|") + "\n" +
        ("| " + "  " * 4 + "| " + "  " * 4 + "|") + "\n" +
        ("+ " + "- " * 4 + "+ " + "- " * 4 + "+") + "\n" +
        ("| " + "  " * 4 + "| " + "  " * 4 + "|") + "\n" +
        ("| " + "  " * 4 + "| " + "  " * 4 + "|") + "\n" +
        ("| " + "  " * 4 + "| " + "  " * 4 + "|") + "\n" +
        ("|" + " " * 9 + "|" + " " * 9 + "|") + "\n" +
        ("+ " + "- " * 4 + "+ " + "- " * 4 + "+"))



# Part 2
# (a) A function to print a grid with 1 input parameter.
def print_grid_2a(n):
    if n > 0 and n % 2 == 1:
        line = ("+ " + "- " * (n//2))* 2 + "+"
        stik = ("|" + " " * n) * 2 + "|"
        print((line + "\n" + (stik + "\n") * (n//2)) * 2 + line)


print_grid_2a(15)

# (b) An example of a function to print a different grid with 1 input parameter.
def print_grid_2b(n):
    if n > 0:
        line = (("+ " + "- "*n)*n + "+")
        stik = ("| " + "  "*n)*n + "|"
        print((line + "\n" + (stik + "\n")* n)*n + line)


print_grid_2b(5)



# Part 3
# A more general function to print a grid with 2 input parameters.
# Param m specifies the number of rows and columns and param n, the cell size.
def print_grid_2_param(m,n):
    line = ("+ " + "- " * n) * m + "+"
    stik = ("| " + "  " * n) * m + "|"
    print((line + "\n" + (stik + "\n") * n) * m + line)


print_grid_2_param(3,4)


