#!/usr/bin/env python3

# Series 1
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list)
add_fruit = input("What fruit would you like to add? ")
fruit_list.append(add_fruit)
print(fruit_list)
user_choice = input("Pick a number between 1 and {}. ".format(len(fruit_list)))
print(fruit_list[int(user_choice) - 1])
other_fruit = []
new_choice = input("Pick a new fruit. ")
other_fruit.append(new_choice)
fruit_list = other_fruit + fruit_list
print(fruit_list)
new_choice = input("Now pick another fruit. ")
fruit_list.insert(0,new_choice)
print(fruit_list)
print("Now here's all the fruits that begin with the letter 'P'")
for i in fruit_list:
	if i[0] == "P":
		print(i)
series1_fruit_list = fruit_list

# Series 2
fruit_list = series1_fruit_list
print(fruit_list)
fruit_list.pop(-1)
print(fruit_list)
to_delete = input("Choose a fruit to to delete. ")
if to_delete in fruit_list:
	fruit_list.remove(to_delete)
else:
	print('i don\'t see that fruit in the list.')

# Series 3
fruit_list = series1_fruit_list

print(fruit_list)
for i in fruit_list:
	user_likes = input("Do you like {}? yes / no ".format(i.lower()))
	while user_likes != "yes" or "no":
		print("invalid response / try again")
		user_likes = input("Do you like {}? yes / no ".format(i.lower()))
	if user_likes == "no":
		fruit_list.remove(i)


print(fruit_list)

# Series 4
fruit_list = series1_fruit_list
reversed_list = []
for i in fruit_list:
	reversed_list.append(i[::-1])
fruit_list.pop()
print(fruit_list, reversed_list)


