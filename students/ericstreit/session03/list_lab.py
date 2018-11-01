#Lesson03
#String Exercises ##
#
#!/usr/bin/env python3
#define variables
mylist = ["Apples", "Pears", "Oranges", "Peaches"]
#define function
def myfunc(n):
    """Update the DocString"""
    pass
#series 1
print("The list currently contains: ", mylist)
additem = input("Pleaes enter another item: ")
mylist.append(additem)
print("The list currently now contains: ", mylist)
l = len(mylist)
listitem = int(input("Enter a list item from 1 to {} and I will show it to you: ".format(l)))
print(mylist[(listitem-1)])
print()
pause = input("OK, let's add Kiwis to the list!")
newlist = ["Kiwis"]
mylist = newlist + mylist
print(mylist)
pause = input("Now adding Mangos to the beginning of the list!")
mylist.insert(0,"Mangos")
print(mylist)
pause = input("Now displaying all items that begin with the letter 'P'")
for i in mylist:
    if i[0] == "P":
        print(i)
pause = input("Press any key to continue to series 2 exercise")

#series 2
print()
print()
print("The list currently contains items: ",mylist)
print("Removing the last item, {}, from the list ".format(mylist[-1]))
mylist.pop()
print("The list now contains: ",mylist)
toremove = input("Please enter an item you would you like to remove : ")
mylist.remove(toremove)
print("The list now contains: ",mylist)

#series 3
#there is a bug in this section - if an item is removed then it skips the following item
#I suspect because it changes the index value
print("OK, let's move on to series 3!")
print()
copy_listXXXXXXXX = mylist
print(id(mylist))
print("here is the copied list")
print(copy_listXXXXXXXX)
print(id(copy_listXXXXXXXX))
for i in copy_listXXXXXXXX:
    choice = input("Do you like {}?: (y/n)".format(i))
    if choice == "y":
        continue
    elif choice == "n":
         mylist.remove(i)
         print("Removing {} from the list!".format(i))
         #bug if 'n' is selected it skips the next item in the list, even if I use a copy of the list..
    else:
        while choice != "y" or "n":
            choice = input("Hm, I don't understand '{}' please enter 'y' or 'n' ".format(choice))
            break
print(mylist)

#series 4
#start
print("Let's start series 4!")
print("The list currently contains: ", mylist)
l = len(mylist)
newlist = []
for i in mylist:
    newlist.append(i[::-1])
print("The original list is {} minus the last item.".format(mylist[0:l-1]))
print("The original list items spelled backwards is {}: ".format(newlist))

pause = input("Press any key to exit")



#for testing
if __name__=="__main__":
    pass
