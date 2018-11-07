#!/usr/bin/env python3


#initialize list of fruits
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']



def list_series_1(fruits):
    #Display the initial list of fruits
    print(fruits)

    #prompt user for fruit then append to list
    more_fruit = input("What fruit should I add to the list? ")
    fruits.append(more_fruit)
    print(fruits)

    #Prompt user for fruit number they would like to display, then display that fruit
    fruit_num = int(input("What fruit number do you want? "))
    print(fruit_num, fruits[fruit_num - 1])

    #Add Banana to beginnning of list
    first_fruit = ["Banana"] 
    new_list = first_fruit + fruits
    print(new_list)

    #Insert a new fruit somewhere in the list using insert()
    new_list.insert(3, "Guava")
    print(new_list)

    #Print every fruit in the list that starts with 'P'
    count = 0
    for fruit in new_list: 
        if fruit[0] == 'P':
            print(fruit)
        count = count + 1    


list_series_1(fruits)



def list_series_2(fruits):
    #Display the list
    print(fruits)

    #Remove the last fruit from the list
    del fruits[-1]
    print(fruits)

    #Ask user which fruit they would like to delete; delete that fruit
    response = input("Which fruit would you like to delete from the list? ")
    for fruit in fruits[:]:
        if fruit == response:
            fruits.remove(fruit)
    print(fruits)

list_series_2(fruits)



def list_series_3(fruits):

    #Ask user if they like each item in the list - this is a missed opportunity to say "How do you like them apples?" to the user :P
    for fruit in fruits[:]:
        response = input("Do you like {}? ".format(fruit).lower())
        if response == "yes":
            continue
        elif response == "no":
            fruits.remove(fruit) #will take "no" but will not remove item
            continue
        else:
            prompt = input("Please answer 'yes' or 'no'. Do you like {}? ".format(fruit).lower())
            continue
    print(fruits)


list_series_3(fruits)



def list_series_4(fruits):
    #Make a copy of the list and reverse the letters in each fruit in the copy.
    fruit_copy = fruits[:]
    for fruit in fruit_copy:
        print(fruit[::-1]) #doesn't return a list
    print(fruits)


list_series_4(fruits)

