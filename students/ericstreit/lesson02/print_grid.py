
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
#for testing
if __name__=="__main__":
    print_grid(5)

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
