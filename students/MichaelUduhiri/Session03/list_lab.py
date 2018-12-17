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
print(fruits)
like_fruit = input("Do you like " + str.lower(fruits[0]) + "? ")
if like_fruit == "no":
    fruits.remove(fruits[0])
while like_fruit != "yes" or "no":
    print(like_fruit)
print(fruits)


'''Series 4'''
new_fruit_list = fruits[::-1]
new_fruit_list.reverse
reverse_new_fruit_list = [i[::-1] for i in new_fruit_list]
print(reverse_new_fruit_list)
