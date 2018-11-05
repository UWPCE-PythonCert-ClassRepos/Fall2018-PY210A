def series_1():
    """
    Creates a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Displays the list
    Asks the user for another fruit and add it to the end of the list.
    Displays the list.
    Asks the user for a number and displays the number back to the user and the fruit corresponding to that number (on a 1-is-first basis)
    Adds another fruit to the beginning of the list using “+” and displays the list.
    Adds another fruit to the beginning of the list using insert() and displays the list.
    Displays all the fruits that begin with “P”, using a for loop.
    """
    fruits=["Apples","Pears","Oranges","Peaches"]
    print(fruits)
    response=input("Name another fruit==>")
    fruits.append(response)
    print(fruits)
    number=int(input("Please enter a number==>"))
    print(" {}. {}".format(number,fruits[number-1]))
    fruits=["Strawberry"]+fruits
    print(fruits)
    fruits.insert(0,"Blueberry")
    print(fruits)
    for fruit in fruits:
        if fruit[0]=="P":
            print(fruit)
    return fruits

def series_2(fruits):
    """
    Displays the list.
    Removes the last fruit from the list.
    Displays the list.
    Asks the user for a fruit to delete, finds it and deletes it.
    """
    print(fruits)
    fruits.pop()
    print(fruits)
    ask_them=input("Please choose a fruit to remove==>")
    for fruit in fruits:
        if fruit==ask_them:
            fruits.remove(ask_them)
    print(fruits)       
    
def series_3(fruits):
    """
    Asks the user for input displaying a line “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
    For each “no”, deletes that fruit from the list.
    For any answer that is not “yes” or “no”, prompts the user to answer with one of those two values
    Displays the list.
    """
    for fruit in fruits:
        like_fruit=""
        while not like_fruit=="yes" and not like_fruit=="no":
            like_fruit=input("Do you like {}?".format(fruit.lower()))
            if like_fruit=="no":
                fruits.remove(fruit)
            if like_fruit != "yes" and like_fruit != "no":
                print("Please enter yes or no")
    print(fruits)       

def series_4(fruits):
    """
    Makes a copy of the list and reverses the letters in each fruit in the copy.
    Deletes the last item of the original list. Displays the original list and the copy.
    Displays the original list and the copy
    """
    
    new_fruits=[]
    for fruit in fruits:
        new_fruits.append(fruit[::-1])
    fruits.pop()
    print(fruits)
    print(new_fruits)
 
    