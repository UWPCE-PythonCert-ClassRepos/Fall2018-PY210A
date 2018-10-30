#!usr/bin/env python

#Series 1

#Create and print list
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)
#User input ask for new fruit
new_fruit = input("Please tell me another type of fruit that is not in the list")
#Append list with user fruit
fruit.append(new_fruit)
print(fruit)
#Ask the user for a number of listed fruit indexes
num_question = int(input("Please give me a number from 0-4:"))
#Return the number back and fruit name at that index
print(fruit[num_question])
#Add another fruit to the list using "+"
print(fruit + ['Melons'])
#Add another fruit to list using insert(), then display
fruit.insert(0, 'Strawberries')
print(fruit)
#Display fruits that begin with "P", using a for loop
for x in fruit:
	if x == 'P':
		print(x)
"""I think you have to use enumerate??"""

#Series 2
#Display list
print(fruit)
#Remove the last fruit from list
del fruit[5]
new_fruit = fruit[:5]
print(new_fruit)
print(fruit)
#User input to ask for fruit to delete, find it the delete it
del_fruit = input("What fruit in the list do you want to delete?")
fruit.remove(del_fruit)
print(fruit)
#Bonus: Multiply list times two. Keep asking until a match is found. Once found, delete all occurances


#Series 3
#Display original fruit list
print(fruit)
#`Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list
#(making the fruit all lowercase). For each “no”, delete that fruit from the list.
#For any answer that is not “yes” or “no”, prompt the user to answer with
#one of those two values (a while loop is good here)

question = ("Do you like {}?".format(fruit[0]))
"""***how do i get list manipulation to where I can filter the listed indexes into the question
Can I use NESTED if statements to continue to ask questions***"""


def ask_yes_no(question):
	"""Ask a yes or no question about the fruit"""
	response = None
	while response not in ("yes", "no"):
		response = input(question.lower())
	if response == "no":
		del(fruit[0])
		return fruit
	else:
		return response

if __name__ == "__main__":
	ask_yes_no(question)
	print(fruit)
	ask_yes_no(question)


#Display the list.
print(fruit)


