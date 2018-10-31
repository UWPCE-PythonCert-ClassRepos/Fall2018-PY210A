# Jae Kim
# python_list_lab.py

fruits = ["Apples", "Pears", "Oranges", "Peaches"]

###### Series 1
print(fruits)

another_fruit = input("Add another fruit: \n => ")
fruits.append(another_fruit)
print(fruits)

show_fruit = input("Which nth fruit do you want to see? \n => ")
print(fruits[int(show_fruit)])

first_fruit = input("Add a fruit to the beginning of the list \n => ")
fruits = [first_fruit] + fruits
print(fruits)

another_first_fruit = input("Add another fruit to the beginning of the list \n => ")
fruits.insert(0, another_first_fruit)
print(fruits)

for fruit in fruits:
    if fruit[0].lower() == 'p':
        print(fruit)


# End of Series 1
# Series 2
fruits_2 = fruits

print(fruits_2)
del fruits_2[-1]

fruits_twice = fruits_2 * 2
print("Doubled fruits \n {}".format(fruits_twice))

remove_fruit = input("Which fruit do you want to remove? \n => ")
fruits_twice[:] = (value for value in fruits_twice if value != remove_fruit)

print(fruits_twice)

# End of Series 2
# Series 3
fruits_3 = fruits

for fruit in fruits:
    input_like = input('Do you like {}?'.format(fruit.lower()))

    while input_like != 'yes' or input_like != 'no':
        if input_like == 'yes':
            break
        if input_like == 'no':
            fruits_3.remove(fruit)
            print('Removing {}'.format(fruit))
            break
        else:
            print('I only accept yes or no inputs.\n')

            input_like = input('Do you like {}?'.format(fruit.lower()))

print(fruits_3)

# End of Series 3
# Series 4
fruits_4 = fruits
new_fruits_4 = list()

for fruit in fruits_4:
    reversed_fruit = fruit[::-1]
    new_fruits_4.append(reversed_fruit)

print(new_fruits_4)

del fruits_4[-1]
print(fruits_4)