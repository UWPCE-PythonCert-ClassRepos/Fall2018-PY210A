!/usr/bin/python

def print_grid(n):
	'''function to print grid with one variable'''

    a = ("+" + "-"*n + "+" + "-"*n + "+")

    b = ("|" + " "*n + "|" + " "*n + "|")


    print (a)

    for i in range(n//2):
        print (b)

    print (a)

    for i in range(n//2):
        print (b)

    print (a)


print_grid(30)




def print_grind(size,unit):

	'''function to print grid with two variables'''

    a = ("+ " + "- "*unit)

    b = ("|" + " "*(unit*2 + 1))

    for i in range(size):
        print ((a*size + "+\n"), end='')
        print ((b*size  + "|\n") * unit, end='')
    print ((a*size + "+\n"), end='')

print_grind(5,3)

