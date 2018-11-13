#!/usr/bin/env python3
"""
Cheng Liu
PY210A
Session04
"""

# create a dictionary
dict_1 = {'name': 'Chris', 'City': 'Seattle', 'Cake': 'Chocolate'}
print(dict_1)


# delete an item in dictionary
del dict_1['Cake']
print(dict_1)


# add an item to dictionary
dict_1['Fruit'] = 'Mango'
print(dict_1)

# display all dictionary keys
print(dict_1.keys())

# display all dictionary values
print(dict_1.values())

# display if 'cake' is in key, and if 'Mango' is in values
print('cake' in dict_1.keys())
print('Mango' in dict_1.values())


# create a new dictionary from dictionary 1
# use the same keys but with values to be # of 't' in each value
dict_2 = {}
for key, value in dict_1.items():
    dict_2[value] = value.count('t')
print(dict_2)


# create new sets with numbers from 0 to 20 that divisible by 2,3,and 4
s2 = set()
s3 = set()
s4 = set()

for i in range(21):
    if not i % 2:
        s2.add(i)
    if not i % 3:
        s3.add(i)
    if not i % 4:
        s4.add(i)

print(s2)
print(s3)
print(s4)

# if s3 is a subset of s2
print(s3.issubset(s2))

# if s4 is a subset of s2
print(s4.issubset(s2))

# a new set with letters in 'python' and add 'i' to the set
s = set('python')
s.add('i')
print(s)

# create a new frozen set
s_frozen = frozenset('marathon')
print(s_frozen)

# print the union and intersection
print(s.union(s_frozen))
print(s.intersection(s_frozen))
