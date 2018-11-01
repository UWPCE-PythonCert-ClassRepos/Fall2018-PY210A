#!/usr/bin/env python3

# Series 1
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)

new_fruit = input("Enter a new fruit: ")
fruit.append(new_fruit)
print(fruit)

ind = int(input(f"Enter number between 1 and {len(fruit)}: "))
print(f"You selected: {ind} " + fruit[ind - 1])

fruit = ["Grapes"] + fruit
print(fruit)

fruit.insert(0, "Strawberries")
print(fruit)

for item in fruit:
    if item[0] == "P":
        print(item)

# Series 2
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)

del fruit[-1]
print(fruit)

fruit = fruit * 2
print(fruit)
keep_going = True
while keep_going:
    delete_fruit = input("Enter a fruit to delete: ")
    for item in fruit:
        if item == delete_fruit:
            fruit.remove(item)
            keep_going = False
print(fruit)

# Series 3
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
for item in fruit[:]:
    question = input(f"Do you like {item.lower()}?")
    while question not in ['yes', 'no']:
        question = input("Please respond yes or no?")
    if question == "no":
        fruit.remove(item)
print(fruit)

# Series 4
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit_copy = fruit[:]
for item in range(len(fruit_copy)):
    fruit_copy[item] = fruit_copy[item][::-1]
del fruit[-1:]
print(fruit_copy)
print(fruit)
