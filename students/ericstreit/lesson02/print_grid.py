
#print grid lesson

# #Part 2
def print_grid(gridsize):
    borderline = "+" + "-" *gridsize + "+" + "-" *gridsize + "+"
    innerline = "|" + " " *gridsize + "|" + " " *gridsize + "|"
    print(borderline)
    for i in range(gridsize):
        print(innerline)
    print(borderline)
    for i in range(gridsize):
        print(innerline)
    print(borderline)
print_grid(10)

#Part 1
# print("+" + "-" *gridsize + "+" + "-" *gridsize + "+")
# print("|" + " " *gridsize + "|" + " " *gridsize + "|")
# print("|" + " " *gridsize + "|" + " " *gridsize + "|")
# print("|" + " " *gridsize + "|" + " " *gridsize + "|")
# print("|" + " " *gridsize + "|" + " " *gridsize + "|")
# print("+" + "-" *gridsize + "+" + "-" *gridsize + "+")
# print("|" + " " *gridsize + "|" + " " *gridsize + "|")
# print("|" + " " *gridsize + "|" + " " *gridsize + "|")
# print("|" + " " *gridsize + "|" + " " *gridsize + "|")
# print("|" + " " *gridsize + "|" + " " *gridsize + "|")
# print("+" + "-" *gridsize + "+" + "-" *gridsize + "+")
input("press any key to continue")
