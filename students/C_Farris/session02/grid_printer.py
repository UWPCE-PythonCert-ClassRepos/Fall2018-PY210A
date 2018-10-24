#!/usr/bin/env Python3


#Date: October 16, 2018
#Created by: Carol Farris
#Purpose: Practice printing a grid


#printGridpart1 prints a 2x2 grid with user specified size
def printGridpart1(n,m=2): 
    m = m
    num_dashes = int((n-1)//2)
    space = " "
    plus = "+"
    spaceminus= " -"
    tallline = "|"
    oneLine = (plus + spaceminus*num_dashes + space)*m + plus 
    middleLine = (tallline + space*n)*m + tallline
    for y in range(m):
        print(oneLine) 
        for x in range(num_dashes): 
    	    print((middleLine))
    print(oneLine)    


#printGridpart2 prints an mxm grid with user specified size
def printGridpart2(m,n):
    m = m 
    n = n
    space = " "
    plus = "+"
    spaceminus= " -"
    tallline = "|"
    oneLine = (plus + spaceminus*n + space)*m + plus 
    middleLine = (tallline + space*(n*2) + space)*m + tallline
    for y in range(m):
        print(oneLine) 
        for x in range(n): 
    	    print((middleLine))
    print(oneLine)



if __name__ == "__main__" :
    printGridpart1(3)
    printGridpart1(11)
    printGridpart1(15) 
    printGridpart2(3,4)
    printGridpart2(5,3)  

