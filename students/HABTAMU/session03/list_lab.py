#!/usr/bin/env python3
""" This is Section 1 List Lab """

a_list = ["Apples","Pears","Oranges","Peaches"]
print(a_list)

# Ask the user for another fruit and add it to the end of the list.
new_fruit = input("Which fruit would you like to add? \>").strip().title()
a_list.append(new_fruit)

print ("There are", len(a_list), "fruits:", a_list)

new_num = int(input("Enter any number? \>").strip())
z_fruit = a_list[new_num]
output = "You added a number {} and fruit that corspond to is {}".format(new_num,z_fruit)
print(output)
another_fruit = input("Let's add another fruit to the beginning of the list using and display the list:> ").strip()

# to add another fruit to the beginning of the list using “+” and display the list.
x = [another_fruit] + a_list

# Add another fruit to the beginning of the list using insert() and display the list.
a_list.insert(0,another_fruit)
print(x)
print(a_list)

# Display all the fruits that begin with “P”, using a for loop.
for i in range(len(a_list)):
    if a_list[i][0] == "P":
        print(a_list[i])
    else:
        print("")
