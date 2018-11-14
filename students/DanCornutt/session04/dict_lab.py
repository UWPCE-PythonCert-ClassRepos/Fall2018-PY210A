#!/usr/bin/env python3
"""
Dictionary Lab experiements with Dictionares, Sets an Frozensets
Functions are:
    dict1():
        no parameters
        creates dictionary, modifies, keys and values
        returns dictionary
    dict2(param1):
        param1: type Dictionary
        Copies passed dictionary, counts numbers of "t"s in each value
        returns: Dictionary
    set1():
        no parameters
        creates 3 sets and prints issubset tests
        returns: none
    set2():
        no parameters
        creates set of letters and frozenset of letters
        computes intersection and union sets for 2 created Sets
        returns: none
"""


def dict1():
    orders = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

    print(orders)
    del orders["cake"]
    print(orders)

    orders["fruit"] = "Mango"
    print(orders)
    print(orders.keys())
    print(orders.values())

    print(("cake" in orders.keys()))
    print(("Mango" in orders.values()))

    return orders


def dict2(orders):
    orders2 = orders.copy()
    for k, v in orders2.items():
        orders2[k] = v.lower().count("t")
    return orders2


def set1():
    s2 = set(range(2,21,2))
    s3 = set(range(3,21,3))
    s4 = set(range(4,21,4))
    print(s2, s3, s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))


def set2():
    s5 = set(list("Python"))
    s5.add("i")
    print(s5)
    fs1 = frozenset(list("marathon"))
    print(fs1)
    print(s5.union(fs1))
    print(s5.intersection(fs1))


if __name__ == "__main__":
    orders1 = dict1()
    print(orders1)
    orders2 = dict2(orders1)
    print(orders2)

    set1()
    set2()
