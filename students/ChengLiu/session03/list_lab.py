#!/usr/bin/env python3

"""
PY210A-Session03
Cheng Liu
list
"""

# Series 1
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

new_fruit = input("Enter a new fruit name: ")
fruits.append(new_fruit)
print(fruits)

display_index = int(input("Enter a number: "))
print(fruits[display_index - 1])


new_fruit_2 = input("Enter another fruit: ")
fruits = [new_fruit_2] + fruits
print(fruits)


new_fruit_3 = input("Enter another fruit: ")
fruits.insert(0, new_fruit_3)
print(fruits)


for fruit in fruits:
    if fruit[0].upper() == 'P':
        print(fruit)
    else:
        pass


# Series 2
print(fruits)
del fruits[-1:-2]
print(fruits)

to_delete = input("Enter a fruit to delete: ")
for fruit in fruits:
    if fruit.upper() == to_delete.upper():
        print(fruits.index(fruit))
        del fruits[fruits.index(fruit)]
    else:
        pass
    print(fruits)


# Series 3
for fruit in fruits:
    user_answer = ""
    while user_answer.lower() not in ('yes', 'no'):
        user_answer = input("Do you like " + fruit.lower() + " ? ")
        if user_answer.lower() == 'no':
            del fruits[fruits.index(fruit)]
        else:
            pass
    print(fruits)


# Series 4
fruits_copy = fruits[:]
fruits_copy.reverse()
print(fruits)
print(fruits_copy)
del fruits[-1:-2]
print(fruits)
print(fruits_copy)
