#!/usr/bin/env python3


#Series 1

my_list = ["Apples", "Pears", "Oranges", "Peaches"]

print(my_list)

response = input("Please enter a new fruit > ")
my_list.append(str(response).title())

print(my_list)

response = input("Please enter a number, 1 -5 > ")
print(int(response))
print(my_list[int(response)-1])

my_list = ["Strawberry"] + my_list
print(my_list)

my_list.insert(0, "Bananas")
print(my_list)


l = []
for i in my_list:
	if i.startswith("P"):
		l.append(i)

print(l)



#Series 2

print(my_list)

my_list = my_list.pop(-1)

print(my_list)

response = input("Please select fruit to remove > ")
response = str(response).title()
if response in my_list:
	my_list.remove(response)

print(my_list)


#Series 3

for fruit in my_list:
	while True:
		response = input("Do you like {}: ".format(fruit.lower()))

		if response.lower() == 'Yes' or response.lower() == 'no':
			break
		else:
			print("Please enter either 'Yes' or 'no' ")
	if response.lower() == 'no':
		my_list.remove(fruit)
print("Fruits are: {}".format(my_list))
print()



#Series 4

my_list = ["Apples", "Pears", "Oranges", "Peaches"]

my_list_copy = my_list[:]
print(my_list_copy)

my_list.pop()
print(my_list)
