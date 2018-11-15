#!/usr/bin/env Python3


#Date: October 30, , 2018
#Created by: Carol Farris
#Purpose: Slicing Lab


"""Write some functions that take a sequence as an argument, and return a copy of that sequence:
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order.
NOTE: These should work with ANY sequence – but you can use strings to test, if you like."""


myList = [1,2,3,4,5,6,7,8,9,10,11,12]
myString = "The Quick Brown Fox Jumped Over The Lazy Dog"


def swapfirstlast(n):
    print("value before swapping:")
    print(n)
    newList = [n[-1], n[1:-1], n[0]]
    print(*newList)

def everyotheritem(n):
    print(n[1::2])
    pass


"""#remove every other item in the list
 def everyotherremoved(n):
     altList = n #remove every other item

     return 


#first four and last four items removed
def first4last4removed(n):
    alist= n


def elementsReversed(n): """
if __name__ == '__main__':
    swapfirstlast(myList)
    swapfirstlast(myString)
    everyotheritem(myList)
    everyotheritem(myString)



