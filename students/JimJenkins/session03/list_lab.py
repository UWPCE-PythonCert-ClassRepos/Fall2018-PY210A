#!/usr/bin/env python3

"""
Author: Jim Jenkins (dvlupr)
Date: 10/30/2018

"""
# SERIES 1


# create the initial list
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit_original = fruit_list
for fruit in enumerate(fruit_list):
    print(fruit)
print('-----')

# user input to add a new fruit
new_fruit = str(input("please add a new fruit: "))
fruit_list.append(new_fruit)
for fruit in enumerate(fruit_list):
    print('updated list: ', fruit)
print('-----')

# user input to select a number for fruit
fruit_num = int(input('please provide a number of fruit: '))
print('You selected: ', fruit_list[fruit_num])
print('-----')

# user input to add a new fruit to the front with +
new_fruit = str(input("please add another new fruit: "))
fruit_list = [new_fruit] + fruit_list
for fruit in enumerate(fruit_list):
    print('updated list: ', fruit)
print('-----')

# user input to add a new fruit to the front with +
new_fruit = str(input("please add another new fruit: "))
fruit_list.insert(0, new_fruit)
for fruit in enumerate(fruit_list):
    print('updated list: ', fruit)
print('-----')

# display all the fruits that begin with P, using a for loop
new_fruit_list = []
for fruit in fruit_list:
    if fruit.startswith('P'):
        new_fruit_list.append(fruit)
print('fruits that start with P: ', new_fruit_list)
print('-----')

# SERIES 2


# display the list
print('current list: ')
for fruit in enumerate(fruit_list):
    print(fruit)
print('-----')

# remove the last fruit from the list
print('removing the last item.')
fruit_list.pop(-1)
print('current list: ')
for fruit in enumerate(fruit_list):
    print(fruit)
print('-----')

# asking user for which item to delete
del_num = int(input('which item number would you like to delete?: '))
fruit_list.pop(del_num)
print('deleting: ', del_num)
print('updated list: ')
for fruit in enumerate(fruit_list):
    print(fruit)
print('-----')


#SERIES 3

#todo issues with my looping
#request user for input for do you like <fruit>? and add while loop for answers other than yes and no delete each
# no from the fruit list
max_count = len(fruit_list)
print('max count: ', max_count)
count = 0
while count <= max_count:
    count = count + 1
    for fruit in fruit_list:
        fruit_ask = fruit
        user_answer = input('do you like {}? '.format(fruit_ask))
        if user_answer.lower() == 'yes':
            print('ok, thanks.')
        elif user_answer.lower() == 'no':
            fruit_list.remove(fruit_ask)
            print('removed item')
        else:
            print('wrong answer')



# SERIES 4


# reverse list and display
fruit2_list = fruit_list
fruit2_list.reverse()
print('reverse: ')
for fruit2 in enumerate(fruit2_list):
    print(fruit2)
print('-----')

# delete the list item from the original list and display both
fruit_original.pop(-1)
print('original list: ')
for fruit_org in enumerate(fruit_original):
    print(fruit_org)
print('reverse (again): ')
for fruit2 in enumerate(fruit2_list):
    print(fruit2)
print('-----')
