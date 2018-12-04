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
    newFruit.strip()  # strip any whitespace
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


if __name__ == '__main__':
    myFruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(myFruit)
    askforAFruit()
    askForANumber()
    addToBeginningOfList(myFruit)
    displayPfruits(addToBeginningOfList(myFruit))
