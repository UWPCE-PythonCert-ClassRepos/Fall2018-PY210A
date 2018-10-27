#Lesson03
#Slicing Exercises ##
#

def numberswap(n):
    """Prints the list with the last item first and first item last"""
    l=len(n)
    print("{}, {} and {}".format(n[-1], n[1:(l-1)], n[0]))

def every_other(n):
    """Prints every other item in list starting with the very first"""
    print(n[::2])

def every_other_in_middle(n):
    """Prints every other item in list omitting the first and last 4 in the series"""
    l=len(n)
    print(n[4:(l-4):2])

def reverse_list(n):
    """Prints the reverse of the list"""
    print(n[::-1])

def swap_thirds(n):
    """Prints the last third of the list first, then the first third, then the last"""
    l = len(n)
    third = (l // 3)
    print("{}, {} and {}".format(n[(third * 2)::], n[0:third], n[third:(third*2)]))

#Function testing
if __name__=="__main__":
    mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    mystring = "This is my string test"
    print("The list contains: ",mylist)
    print("The string contains: ",mystring)
    numberswap(mylist)
    numberswap(mystring)
    every_other(mylist)
    every_other(mystring)
    every_other_in_middle(mylist)
    every_other_in_middle(mystring)
    reverse_list(mylist)
    reverse_list(mystring)
    swap_thirds(mylist)
    swap_thirds(mystring)
