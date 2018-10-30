"""List manipulation"""

"""Series 1"""
"""Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”"""
fruit_list = ['Apples','Pears','Oranges','Peaches']

"""Display the list"""
print (fruit_list)

"""Ask the user for another fruit and add it to the end of the list"""
user_fruit = input("User please enter a fruit you like > ")
fruit_list.append(user_fruit)

"""Display the list"""
print (fruit_list)

"""Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis)"""
user_number = input("User please enter any number between 1 to {} > ".format(len(fruit_list)))
print ("User chose {}".format(int(user_number)) + " and the fruit is "  + fruit_list[int(user_number) - 1])

"""Add another fruit to the beginning of the list using “+” and display the list"""
fruit_list = ['Pineapple'] + fruit_list
print('\nList of Fruits:\n', fruit_list)

"""Add another fruit to the beginning of the list using insert() and display the list"""
fruit_list.insert(0, 'Banana')
print('\nList of Fruits:\n', fruit_list)

"""Display all the fruits that begin with “P”, using a for loop"""
for fruit in fruit_list:
    if fruit[0] == "P":
        print (fruit)


"""Series 2"""

"""Display the list"""
print (fruit_list)

"""Remove the last fruit from the list"""
fruit_list.pop()
print (fruit_list)

"""Ask the user for a fruit to delete, find it and delete it"""

user_delete_fruit = input("User please enter the fruit you want to remove from the list ")

if user_delete_fruit in fruit_list:
    fruit_list.remove(user_delete_fruit)

print (fruit_list)

"""Series 3"""
"""Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
   For each “no”, delete that fruit from the list.
   For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
   Display the list 
"""
for fruit in fruit_list:
    response = ''
    while response not in ['yes', 'no']:
        print(f'Do you like {fruit}?\n Please select yes or no')
        response = input()
    if response == 'no':
        fruit_list.remove(fruit)

print(fruit_list)

"""Series 4"""

"""Make a copy of the list and reverse the letters in each fruit in the copy"""
new_fruit_list = [fruit[::-1] for fruit in fruit_list[:]]
print(new_fruit_list)


