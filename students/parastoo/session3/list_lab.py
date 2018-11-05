#!/usr/bin/env python3
#Series 1

print('Series 1')
'''Create a list that contains “Apples”, “Pears”,
“Oranges” and “Peaches” and isplay the list.'''
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

'''Ask the user for another fruit and add it to the end of the list.'''
fruits.append(input('\nAdd a fruit:\n>>>'))
print (fruits)

'''Ask the user for a number and display the number
back to the user and the fruit corresponding to that number.'''
x = int(input('\nEnter a number:\n>>>'))
print(x , ":", fruits[x-1])

'''Add another fruit to the beginning of the list using “+” and
display the list.'''
fruits = [input('\nAdd another fruit:\n>>>')] + fruits
print('\n',fruits)

'''Add another fruit to the beginning of the list using
insert() and display the list.'''
fruits.insert(0, input('\nAdd another fruit to the begining of the list:\n>>>'))
print(fruits)

'''Display all the fruits that begin with “P”, using a for loop.'''
print('\nFruits that begin with "P"', '\n',[fruit for fruit in fruits if fruit[0].lower() == 'p'])

#Series 2
print('\nSereis 2')

# remove the last fruit from the list

last_fruit = fruits[-1]
del fruits[-1]
print(fruits)

#Ask the user for a fruit to delete, find it and delete it.

del_a_fruit = input('\nPick a fruit to delete:\n>>>')
while del_a_fruit in fruits:
    fruits.remove(del_a_fruit)

print(fruits)



# Multiply the list times two. Keep asking until a match is found.

fruits_times_two = fruits * 2
print('\nDoubled fruit list:\n',fruits_times_two)

del_a_fruit = input('\nPick a fruit to delete:\n>>>')
while del_a_fruit in fruits_times_two:
    fruits_times_two.remove(del_a_fruit)

print(fruits_times_two)

#Series 3
print('\nSeries 3')

for fruit in fruits:

    choice = (input('Do you like {} ? (yes/no)'.format(fruit.lower())))[0].lower()

#For each “no”, delete that fruit from the list.

    if choice == 'n':
        while fruit in fruits:
            fruits.remove(fruit)
        print (fruits)

    elif choice == 'y':
        print(fruits)

#For any answer that is not “yes” or “no”, reprompt

    else:
        choice = input('Please enter yes or no')

#Series 4
print('\nSeries 4')

#Make a copy of the list and reverse the letters in each fruit in the copy.

new_fruits = fruits[:]

for fruit in new_fruits:
    fruit = fruit[::-1]

new_fruits = [fruit[::-1] for fruit in fruits]
print(new_fruits)

#Delete the last item of the original list. Display the original list and the copy.

del fruits[-1]
print(fruits)
print(new_fruits)











