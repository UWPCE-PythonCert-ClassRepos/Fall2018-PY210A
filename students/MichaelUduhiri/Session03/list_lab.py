#!/usr/bin/env python3
$ ./list_lab.py

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

new_fruit = input("Please enter another fruit ")
fruits.append(new_fruit)
print(fruits)

fruit_number = int(input("Please enter a number "))
print(fruit_number, fruits[fruit_number - 1])

another_fruit1 = ["Grapefruit"]
print(another_fruit1 + fruits)

fruits.insert(6, "Pineapple")
print(fruits)

for i in fruits:
    if i[0] == "P":
        print(i)


'''Series 2'''
print(fruits)
fruits.remove("Pineapple")
print(fruits)
delete_fruit = input("Which fruit would you like to delete? ")
if delete_fruit in fruits:
    fruits.remove(delete_fruit)
print(fruits)

'''Series 3'''
like_fruit = input("Do you ")


'''Series 4'''
