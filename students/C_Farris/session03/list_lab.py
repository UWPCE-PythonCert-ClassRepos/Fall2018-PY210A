#!/usr/bin/env Python3

"""
Date: November 11, 2018
Created by: Carol Farris
Title: list Lab
Goal: learn list functions
"""


def displayPfruits(myFruit):
    for x in myFruit:
        if x.lower().startswith('p'):
            print(x)
        else:
            print(x + "  doesn't start with p")


def addUsingInsert(myFruit):
    myFruit.insert(0, 'Pineapple')
    print(myFruit)


def addToBeginningOfList(myFruit):
    singleList = ['Mango']
    myFruit = singleList + myFruit
    print(myFruit)
    addUsingInsert(myFruit)
    print(myFruit)
    return myFruit


def askforAFruit():
    newFruit = input("Please enter a different fruit ==>")
    newFruit = newFruit.strip().capitalize()  # strip any whitespace
    myFruit.append(newFruit)
    print(myFruit)


def askForANumber():
    fruitNumb = 100
    fruitLength = len(myFruit) - 1
    textInput = "Please select an integer from 0-{} ==>".format(fruitLength)
    while not fruitNumb <= fruitLength:
        fruitNumb = int(input(textInput))
    gotThatFruit = myFruit[fruitNumb]
    print(fruitNumb, gotThatFruit)


def rm_A_fruit():
    print("rm_A_fruit")
    print(myFruit)
    lastItem = len(myFruit) - 1
    myFruit.pop(lastItem)
    print(myFruit)


def get_fruit_to_rm():
    findFruit = input('Please select a fruit to remove from list above ==>')
    findFruit = findFruit.strip().capitalize()
    myFruit.remove(findFruit)
    print(myFruit)


def rm_disliked_fruit():
    print(myFruit)
    fruitToDelete = []
    for x in myFruit:
        question = ""
        verdict = ''
        while verdict != 'yes' and verdict != 'no':
            question = "Do you like {}? Yes or No? ==>  ".format(x.lower())
            verdict = input(question)
            verdict = verdict.strip().lower()
            if verdict == 'no':
                fruitToDelete.append(x)
    findAndDeleteFruit(fruitToDelete)
    print(myFruit)


def findAndDeleteFruit(fruitToDelete):
    for x in fruitToDelete:
        myFruit.remove(x)


def make_new_reversed_list():
    newFruity = []
    for x in myFruit:
        newFruity.append(x[::-1])
    print("The new list with words reversed: {}".format(newFruity))
    print("below is the beginning list: {}".format(myFruit))


if __name__ == '__main__':
    myFruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
    """series 1"""
    print(myFruit)
    askforAFruit()
    askForANumber()
    addToBeginningOfList(myFruit)
    displayPfruits(addToBeginningOfList(myFruit))
    """series 2"""
    rm_A_fruit()
    get_fruit_to_rm()
    """series 3"""
    rm_disliked_fruit()
    """series 4"""
    make_new_reversed_list()
