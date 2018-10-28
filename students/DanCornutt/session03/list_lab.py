#!/usr/bin/env python3

"""
This is the list lab from Session 3 of Python Cert class.

"""
def series1():
    l = ["Apples", "Pears", "Oranges", "Peaches"]
    print(l)
    l.append(input("Which fruit would you like to add? > "))
    print(l)
    item = int(input("Which fruit would you like to return? (1 to {})? > ".format(len(l)))) -1
    print("The {}th item is {}".format(item+1, l[item]))
    l = ["Papaya"] + l
    print (l)
    l.insert(0, 'Limes')
    print (l)

    for f in l:
        if f[0] == "P":
            print(f)
    return l

def series2(l):
    print(l)
    l.pop()
    print(l)
    del l[int(input("Which fruit would you like to remove? (1 to {})? > ".format(len(l)))) -1]
#TODO add bonus question if I have time

if __name__ == "__main__":
    series2(series1())
