#!/usr/bin/env python3

#Tim Pauley
#Python 201a HW 3
#List Lab 3


#Create a list that contains the names of 5 students of this class. (Do not ask for input to do that, simply create the list.) Print the list. 
 

#Print the name that has that number as index. 
#Add "John Smith" and "Mary Miller" at the beginning of the list (by using "+"). Print the list.

# Task 1

fruits = ["Apples", "Pears", "Oranges", "Peaches"]

print(fruits)

#Ask the user to input one more name and append it to the list.

new = input("type a fruit to add> ")

fruits.append(new)

print(fruits)

#Print the list. Ask a user to input a number. 

ind = int(input("give me an index> "))

print("you selected fruit number: {}, which is {}".format(ind, fruits[ind - 1]))
print()
print("All the fruit:\n", fruits)
print()

fruits.insert(0, 'Kiwi')

print("Added a kiwi at the beginning:\n", fruits)

print()
print("All the P fruits:")
for fruit in fruits:
    if fruit[0].lower() == 'p':
        print(fruit)
print()

# make a new list with duplicated entries - to test removal
d_fruits = fruits * 2

print("All the fruits are:", fruits)
ans = input("Which fruit would you like to delete? >")
while ans in d_fruits:
    d_fruits.remove(ans)

print("\nWith fruit deleted:\n", d_fruits)


# Series 3

orig_fruits = fruits[:]

for fruit in fruits[:]:  
    ans = input("Do you like: %s? " % fruit)
    if ans[0].lower() == 'n':  
        while fruit in fruits: 
            fruits.remove(fruit)
    elif ans[0].lower() == 'y':
        pass
    else:
        print("please answer yes / no ")
        
print("\nHere they are with only the ones you like")
print(fruits)
print()

# Series 4

fruits = orig_fruits[:]  

r_fruits = []
for fruit in fruits:
    r_fruits.append(fruit[::-1])

print("Here they are reversed")
print(r_fruits)




