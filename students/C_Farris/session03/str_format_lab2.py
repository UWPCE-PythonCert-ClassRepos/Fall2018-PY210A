#!/usr/bin/env Python3

"""
Date: November 23rd, 2018
Created by: Carol Farris
Purpose: String Formatting Lab
Goal: Gain familiarity with string formatting
"""


def buildUpStringsOne(practiceTuple):
    print((f"File_{practiceTuple[0]:03}: "
           f"{practiceTuple[1]:.2f}, {practiceTuple[2]:.2e},"
           f" {practiceTuple[3]:.2e}"))


def buildUpStrings2(practiceTuple):
    print(("File_{:03}: {:.2f}, {:.2e}, {:.2e}").format(*practiceTuple))


def buildUpStringsThree(test):
    starter_String = "'The {} values are"
    for i in test:
        starter_String += " {:d},"
    final_String = starter_String.strip(',') + "'"
    print(final_String.format(len(test), *test))


def buildUpStringsFour():
    mytuple = (4, 30, 2017, 2, 27)
    myString = "{:0>2d} {} {} {:0>2d} {}".format(mytuple[3],
             mytuple[4], mytuple[2], mytuple[0], mytuple[1])
    print(myString)


def beefUpFruitString():
    fruityList = ['oranges', 1.3, 'lemons', 1.1]
    print(f"The weight of an {fruityList[0][:-1]} "
          f"is {fruityList[1]} and the weight of a "
          f"{fruityList[2][:-1]} is {fruityList[3]}")
    print(f"The weight of an {fruityList[0][:-1].title()}"
          f" is {fruityList[1]*1.2} and the weight of a "
          f"{fruityList[2][:-1].title()} is {fruityList[3]*1.2}")


def practicePrintingColumns():
    practiceList = [['Gary', 5, 2], ['Tom', 15, 30],
                    ['Richard', 80, 100], ['Jerry', 25, 1000],
                    ['Mary', 30, 20000]]
    print('\n')
    print('{:<20}'.format('Name'), '{:<15}'.format('Age'),
          '{:>5}'.format('Cost'))
    print('\n')
    for x in practiceList:
        print('{:<20}'.format(x[0]),
              '{:<15}'.format(x[1]),
              '${:<5,}'.format(x[2]))


def five_Space_Columns(ten_cons):
    print("{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}"
          "{:>5}{:>5}{:>5}{:>5}".format(*ten_cons))


if __name__ == '__main__':
    practiceTuple = (2, 123.4567, 10000, 12345.67)
    test = (1, 2, 3, 4, 5)
    ten_cons = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    """Task 1"""
    buildUpStringsOne(practiceTuple)
    """Task 2"""
    buildUpStrings2(practiceTuple)
    """Task 3"""
    buildUpStringsThree(test)
    """Task 4"""
    buildUpStringsFour()
    """Task 5"""
    beefUpFruitString()
    """Task 6"""
    practicePrintingColumns()
    """Task 6.5"""
    five_Space_Columns(ten_cons)
