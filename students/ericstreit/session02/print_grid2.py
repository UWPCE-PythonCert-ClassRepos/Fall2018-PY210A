
#print grid lesson

# #Part 2
def print_grid2(size, units):
    borderline = ("+" + "-" *units) *size
    innerline = ("|" + " " *units) * size
    print(borderline, end ="+")
    print()
    for x in range(size):
        for i in range(units):
            print(innerline, end = "|")
            print()
        print(borderline, end ="+")
        print()
#for testing
if __name__=="__main__":
    print_grid2(4,4)
