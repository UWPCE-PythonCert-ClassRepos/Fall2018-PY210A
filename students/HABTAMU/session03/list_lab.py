#!/usr/bin/env python3

a_list = ["Apples","Pears","Oranges","Peaches"]
print(a_list)

new_fruit = input("Which fruit would you like to add? \>").strip().title()
a_list.append(new_fruit)

print ("There are", len(a_list), "fruits:", a_list)

new_num = int(input("Enter any number? \>").strip())
z_fruit = a_list[new_num]
output = "You added a number {} and fruit that corspond to is {}".format(new_num,z_fruit)
print(output)

