#!/usr/bin/env python3
"""Dictionaries 1"""
 
# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” 
# (so the keys should be: “name”, etc, and values: “Chris”, etc.)
my_dict = {"name": "Chris","city": "Seattle","cake": "Chocolate"}

# Display the dictionary.
print("{name} is from {city}, and likes {cake} cake.".format(**my_dict))
                                                             
# Delete the entry for “cake”.
my_dict.popitem()
del my_dict["cake"]
print(my_dict)


# Add an entry for “fruit” with “Mango” and display the dictionary.
dict = my_dict
my_dict['fruit'] = 'Mango'

print(my_dict)

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print('cake' in my_dict)

# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print('Mango' in my_dict.values())

# Dictionaries 2
# Using the dictionary from item 1: 
# Make a dictionary using the same keys but with the number of ‘t’s in each value as the value(consider upper and lower case?).

d = {}
for k, v in my_dict.items():
    d[k] = v.count('t')
print(d)

# Sets
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.

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

# Display the sets.
# Display if s3 is a subset of s2(False)
print(s3.issubset(s2))

# and if s4 is a subset of s2 (True).
s4.issubset(s2)

# Sets 2
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.

s1 = set('Python')
s1.add('i')
s1
print(s1)

# Create a frozenset with the letters in ‘marathon’.
f = frozenset('marathon')

# display the union and intersection of the two sets.
x = s1.union(f)
y = f.union(s1)

print("union", x)
print("union with", y)

z = s1.intersection(f)
zz = f.intersection(s1)

print("intersection", z)
print("intersection with", zz)