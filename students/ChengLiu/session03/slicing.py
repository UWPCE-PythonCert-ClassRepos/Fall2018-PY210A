#!/usr/bin/env python3

"""
PY210A-Session03
Cheng Liu
Slicing
"""

items = ['a','b','c','d','e']
items = items * 4
print(items)


items_copy = items[:]
items_copy[0] = items[-1]
items_copy[-1] = items[0]
print(items_copy)

del items_copy[::2]
print(items_copy)

del items_copy[:4]
print(items_copy)

del items_copy[-4:]
print(items_copy)

del items_copy[::2]
print(items_copy)

items_copy.reverse()
print(items_copy)



