#!/usr/bin/env python3
#
############### Series 3 #######################
#
#
# re-Create list of fruits from Series 1 and lowercase
#
#
fruits = ["Apples", "Pears", "Oranges", "Peaches"]	
fruits = [fruit.lower() for fruit in fruits]
#
for i in range(len(fruits)):

    user_inp = input("Do you like {}? (Type 'Y' for Yes or 'N' for No)".format(fruits[i]))

    while user_inp not in ("Y", "N"):
        user_inp = input("Response not recognized. Type 'Y' for Yes or 'N' for No.")

    if user_inp == "Y":
        print("I think you will like our {}".format(fruits[i]))
    elif user_inp == "N":
        print("Too bad")
        item = fruits[i]
        #fruits.remove(item)
        fruits = [fruits.remove(item) for fruit in fruits]
#
#
#
print("Here is what's left...", fruits)

