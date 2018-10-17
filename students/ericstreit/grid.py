
#grid homework
#updated version
borderline = "+" + "-" *gridsize + "+" + "-" *gridsize + "+"
innerline = "|" + " " *gridsize + "|" + " " *gridsize + "|"
gridsize = int(input("How big of a grid would you like?"))
print(borderline)
for i in range(gridsize):
    print(innerline)
print(borderline)
for i in range(gridsize):
    print(innerline)
print(borderline)
#first attempt
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
