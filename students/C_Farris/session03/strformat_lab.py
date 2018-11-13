#!/usr/bin/env Python3

"""
Date: October 30, 2018
Created by: Carol Farris
Purpose: String Formatting Lab
Goal: Gain familiarity with string formatting
"""

from decimal import Decimal


def makeStringFromTuples():
    myString = "file_"
    count = 0
    for x in practiceTuple:
        if count == 0:
            myNumber = str(2).zfill(3)
            myString += myNumber + ": "
        elif count == 1:
            x = str(round(x, 2))
            myString += "  " + x
        else:
            x = str('%.2E' % Decimal(x))
            myString += ", " + x
        count += 1
    print(myString)


def buildUpStringsTwo():
    stringPieces = []
    count = 0
    for x in practiceTuple:
        if count == 0:
            myNumber = str(2).zfill(3)
            myString = "file_{}: ".format(myNumber)
            stringPieces.append(myString)
        elif count == 1:
            x = str(round(x, 2))
            myString = "  {}".format(x)
            stringPieces.append(myString)
        else:
            x = str('%.2E' % Decimal(x))
            myString = ", {}".format(x)
            stringPieces.append(myString)
        count += 1
    finalString = '{}{}{}{}'.format(stringPieces[0],
                  stringPieces[1], stringPieces[2],
                  stringPieces[3])
    print(finalString)


def buildUpStringsThree():
    stringPieces = []
    count = 0
    form_string = ''
    for x in practiceTuple:
        form_string += '{}'
        if count == 0:
            myNumber = str(2).zfill(3)
            myString = "file_{}: ".format(myNumber)
            stringPieces.append(myString)
        elif count == 1:
            x = str(round(x, 2))
            myString = "  {}".format(x)
            stringPieces.append(myString)
        else:
            x = str('%.2E' % Decimal(x))
            myString = ", {}".format(x)
            stringPieces.append(myString)
        count += 1
    print(form_string.format(*stringPieces))


def buildUpStringsFour():
    mytuple = (4, 30, 2017, 2, 27)
    myString = "{:0>2d} {} {} {:0>2d} {}".format(mytuple[3],
               mytuple[4], mytuple[2], mytuple[0], mytuple[1])
    print(myString)


def beefUpFruitString():
    fruityList = ['oranges', 1.3, 'lemons', 1.1]
    print(f"The weight of an {fruityList[0][:-1]} is {fruityList[1]} and the weight of a {fruityList[2][:-1]} is {fruityList[3]}")
    ##here you need to add the 20% and reprint
    print(f"The weight of an {fruityList[0][:-1]} is {fruityList[1]*1.2} and the weight of a {fruityList[2][:-1]} is {fruityList[3]*1.2}")


def practicePrintingColumns():
    practiceList = [['Gary', 5, 2], ['Tom', 15, 30],
                    ['Richard', 80, 100], ['Jerry', 25, 1000],
                    ['Mary', 30, 20000]]
    print('\n')
    print('{:<20}'.format('Name'), '{:<15}'.format('Age'),
          '{:>5}'.format('Cost'))
    print('\n')
    for x in practiceList:
        print('{:<20}'.format(x[0]), '{:<15}'.format(x[1]),
             '{:>5,}'.format(x[2]))


if __name__ == '__main__':
    practiceTuple = (2, 123.4567, 10000, 12345.67)
    """Task 1"""
    makeStringFromTuples()
    """Task 2"""
    buildUpStringsTwo()
    """Task 3"""
    buildUpStringsThree()
    """Task 4"""
    buildUpStringsFour()
    """Task 5"""
    beefUpFruitString()
    """Task 6"""
    practicePrintingColumns()
