'''
Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

'''


def gridprinter1():
	print("+ " + "- - - - " + "+ " + "- - - - " + "+")
	for i in range(4):
		print("|         |         |")
	print("+ " + "- - - - " + "+ " + "- - - - " + "+")
	for i in range(4):
		print("|         |         |")
	print("+ " + "- - - - " + "+ " + "- - - - " + "+")

gridprinter1()

#prints a grid specified by n
def gridprinter2(n):
	print("+ " + "- " * n + "+ " + "- " * n + "+")
	for i in range(n):
		print("| " + "  " * n + "| " + "  " * n + "|")
	print("+ " + "- " * n + "+ " + "- " * n + "+")
	for i in range(n):
		print("| " + "  " * n + "| " + "  " * n + "|")
	print("+ " + "- " * n + "+ " + "- " * n + "+")

gridprinter2(3)


#prints a grid with n characters in x cells
def gridprinter3(x,y):
	for i in range(y):
		print(("+ " + "- " * x) * y , "+")
		for i in range(x):
			print(("| " + "  " * x) * y, "|")
	print(("+ " + "- " * x) * y , "+")

gridprinter3(7,3)





