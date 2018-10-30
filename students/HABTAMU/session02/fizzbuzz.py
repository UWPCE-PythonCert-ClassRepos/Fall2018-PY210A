#!/usr/bin/env python3

for i in range(101):
    if (i%3 == 0) :
        if (i%5 == 0):
            print(i, "FizzBuzz")
        else:
            print(i, "Fizz")
    elif (i%5 == 0):
        print(i,"Buzz")
    else:
        print(i)
