#!/usr/bin/env python3

# Series 1
print("####Series 1####")
print()

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”
list = ['Apples', 'Pears', 'Oranges', 'Peaches']

# Display the list (plain old print() is fine…).
print(list)
print()

#Ask the user for another fruit and add it to the end of the list.
response = str(input("Please enter a new fruite name: "))

# Display the list
list.append(response)
print(list)
print()

# Ask the user for a number and display the number back to the user and the fruit corresponding 
number = int(input("Please enter a number between 1 and {}: ".format(len(list))))
print(number, list[number-1])
print()

# Add another fruit to the beginning of the list using “+” and display the list.
response = str(input("Please enter a new fruite name: "))
list = [response] + list
print(list)
print()

# Add another fruit to the beginning of the list using insert() and display the list.
response = str(input("Please enter a new fruite name: "))
list.insert(0, response)
print(list)
print()

#Display all the fruits that begin with “P”, using a for loop.
list_start_with_P = []
for fruit in list:
    if fruit.startswith('P') or fruit.startswith('p'):
        list_start_with_P.append(fruit)
print("The fruites start with P are", list_start_with_P)
print()

#########################################################################################

# Series 2
print("####Series 2####")
print()

# Display the list
print(list)
print()

# Remove the last fruit from the list
list2 = list[:-1]
print(list2)
print()

# Ask the user for a fruit to delete, find it and delete it
response = str(input("Please enter the fruite name which you want to delete: "))
list2.remove(response)
print(list2)
print()

# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
list2_2 = list * 2

response = str(input("Please enter the fruite name which you want to delete: "))
while response in list2_2:
	list2_2.remove(response)

print("New list after deletion is: ", list2_2)
print()

#########################################################################################

# Series 3
print("####Series 3####")
print()


# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
# Display the list.

list3 = list[:]
for fruit in list3:
	while True:
		response = input("Do you like {}: ".format(fruit.lower()))

		if response.lower() == 'yes' or response.lower() == 'no':
			break
		else:
			print("Please enter either 'yes' or 'no' ")
	if response.lower() == 'no':
		list3.remove(fruit)
print("Fruites are: {}".format(list3))
print()


#########################################################################################

# Series 4
print("####Series 4####")
print()

# Make a copy of the list
list4 = list[:]

for letter, fruit in enumerate(list4):
	#reverse the letters in each fruit in the copy
	list4[letter] = fruit[::-1]

# Delete the last item of the original list
list.pop()

# Display the original list and the copy
print(list)
print(list4)



