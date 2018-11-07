#!/usr/bin/env python3

#
############### Series 1 #######################
#
fruits = ["Apples", "Pears", "Oranges", "Peaches"]

print("Here is a selection of delicious fruits: ", fruits)
user_inp = input("Please add your suggestion to this delectable smorgasbord: " )
#
#
### -> Insert User Input and then display back results
#
fruits.append(user_inp)
print("Updated fruit selection is now: ", fruits, "\n")
#
#
### -> Prompt user to select from list and display back results
#
num = int(input("Pick a number, any number... "))
print("You have chosen: ",num,"which corresponds to the magical fruit of: ", fruits[num - 1],"\n")
#
#
### -> Use the + method to prepend additional fruit and display results
#
fruits = ["Cantalopes"] + fruits
print("The list has grown to:  ", fruits),"\n"
#
### -> Use the insert method to prepend and display results
#
fruits.insert(0,"Honey Dew")
print("...and now the list has grown to:  ", fruits,"\n")
#
#
### -> iterate over list and display back items starting with capital P
#
for i in range(len(fruits)):
    tmp = fruits[i]
    if tmp[0] is "P":
        print(tmp)
    else:
        pass
#
############### Series 2 #######################
#
print("Here is a list of yummy fruits we built: ", fruits,"\n")
#
#
### -> Remove the last item in list and display back
fruits.pop()
print("Hey, someone ate one. Our list is smaller: ", fruits,"\n")
#
#
user_inp = str(input("Which one do you want to take? "))
#print("You said ", user_inp, "\n")
if user_inp in fruits:
    fruits.remove(user_inp)
    print("Now all that is left is: ", fruits, "\n")
else:
    print("No such animal...er...fruit")
    pass
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
while True:

    #for i in fruits[:]:
    for i in range(len(fruits)):
        tmp = fruits
        #user_inp = input("Do you like {}? (Type 'Y' for Yes or 'N' for No)".format(i))
        user_inp = input("Do you like {}? (Type 'Y' for Yes or 'N' for No)".format(tmp[i]))

        if user_inp == "Y":
            #print("I think you'll like our {}.".format(i))
            print("I think you'll like our {}.".format(tmp[i]))
            continue
        elif user_inp == "N":
            #fruits = [fruit.remove() for fruit in fruits]
            fruits.remove(i)
            #tmp.remove(i)
        else:
            print("Please enter 'Y' for Yes or 'N' for No.")
#
#
#
print("Here is what's left...", tmp)







