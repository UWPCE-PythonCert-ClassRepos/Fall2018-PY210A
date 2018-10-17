#part 1 and part 2
def print_grid(number):
    if number < 5:
        number = 5
    num = ((number - 3)//2)
    for y in range(2):
        print(horizontal(num))
        for x in range(num):
            print(vertical(num))
    print(horizontal(num))

#part 3
def print_grid_multi(number, squares):
    for y in range(squares):
        print(horizontal(number, count=squares))
        for x in range(number):
            print(vertical(number, count=squares))
    print(horizontal(number, count=squares))

def horizontal(num, count=2):
    str_plus = "+"
    str_minus = "-"
    str = ""
    for x in range(count):
        str = str + str_plus + str_minus * (num)
    str = str + str_plus
    return str

def vertical(num, count=2):
    str_vert = "|"
    str = ""
    for x in range(count):
        str = str + str_vert + " " * (num)
    str = str + str_vert
    return str
