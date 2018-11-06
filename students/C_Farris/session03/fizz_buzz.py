#!/usr/bin/env Python3


#Date: October 23, 2018
#Created by: Carol Farris
#Purpose: Practice Fizz Buzz challenge



#Method that prints Fizz if number x is divisible 3 and Buzz if number x is divisible by 5
#This method tests 1-100 inclusive. 
def fizzbuzz():
    for x in range (1, 101):
        if x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

fizzbuzz()            



