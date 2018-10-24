#!/usr/bin/env Python3


#Date: October 16, 2018
#Created by: Carol Farris
#Purpose: Practice printing a grid


#Below successfully prints a grid, but isn't complete.
#It will print a total of n boxes, in a grid width of 2
#I need to make it more flexible. 
def printGrid(n):
    n = n #width
    space = " "
    plus = "+"
    minus = "-"
    spaceminus= " -"
    tallline = "|"
    oneLine = (plus + spaceminus*n + space)*2 +  plus
    middleLine = tallline + space*((n*2)+1)
    for y in range(n//2):
        print(oneLine)
        for x in range(n):
    	    print((middleLine*2 +  tallline))
    print(oneLine)    



printGrid(6)
