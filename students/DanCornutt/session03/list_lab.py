#!/usr/bin/env python3

"""
This is the list_lab from Session 3 of Python Cert class.
This is an executable module which can be run in the command line.
Lists are the primary examples demoed here.

"""

def series1():
    l = ["Apples", "Pears", "Oranges", "Peaches"]
    print(l)
    l.append(input("Which fruit would you like to add? > "))
    print(l)
    item = int(input("Which fruit would you like to return? (1 to {})? > ".format(len(l)))) -1
    print("Item number {} is {}".format(item+1, l[item]))
    l = ["Papaya"] + l
    print (l)
    l.insert(0, 'Limes')
    print (l)

    for f in l:
        if f[0] == "P":
            print(f)
    return l


def series2(l):
    l2 = l.copy()
    print(l2)
    l2.pop()
    print(l2)
    del l2[int(input("Which fruit would you like to remove? (1 to {})? > ".format(len(l2)))) -1]
#TODO add bonus question if I have time


def series3(l):
    l3 = l.copy()
    l3copy = []
    for f in l3:
        answer = ""
        while answer not in ('yes', 'no'):
            answer = input("Do you like {}? (yes or no)> ".format(f.lower()))
            answer = answer.strip()
        if answer == "yes":
            l3copy.append(f)
    print (l3copy)


def series4(l):
    l4 = []
    for f in l:
        rev = f[::-1]
        l4.append(rev)
    l4.pop()
    print(l, l4)


if __name__ == "__main__":
    l = series1()
    series2(l)
    series3(l)
    series4(l)
