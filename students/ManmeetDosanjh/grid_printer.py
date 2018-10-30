# Part 1

print('+' + '----' + '+' + '----' + '+')
print('|    |    |')
print('|    |    |')
print('|    |    |')
print('|    |    |')
print('+' + '----' + '+' + '----' + '+')
print('|    |    |')
print('|    |    |')
print('|    |    |')
print('|    |    |')
print('+' + '----' + '+' + '----' + '+')









# Part 2

#?? I couldn't figure this one out.

























# Part 3
def row(a):
    print("+", end=" ")
    for i in range(a-1):
        print("- - - - +", end=" ")
    print("- - - - +")
    
def column(a):
    print("|", end=" ")
    for i in range(a-1):
        print("        |", end=" ")
    print("        |")

def func(a,b):
    first(a)
    for i in range(b):
        for i in range(4):
            second(a)
        first(a)
a=int(input("Col: "))
b=int(input("Row: "))

func(a,b)