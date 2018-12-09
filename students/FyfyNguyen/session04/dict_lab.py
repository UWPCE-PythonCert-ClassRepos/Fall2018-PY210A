#!/usr/bin/env python3

"""
Dictionary and Set Lab
"""

# Dictionaries 1
# Create a dict containing "name", "city", and "cake" for
# "Chris" from "Seattle" who likes "Chocolate" and display dict
dict_1 = dict(name='Chris', city='Seattle', cake='Chocolate')
print(dict_1)

# Delete entry for "cake" and display dict
dict.popitem(dict_1)
print(dict_1)

# Add entry for "fruit" with "Mango" and display dict
dict_1['fruit'] = 'Mango'
print(dict_1)

# Display dictionary keys
print(dict_1.keys())

# Display dictionary values
print(dict_1.values())

# Display whether "cake" is key in dictionary (i.e. False)(now)
print('cake' in dict_1)

# Display whether "Mango" is a value in the dictionary (i.e. True)
print('Mango' in dict_1.values())


# Dictionaries 2
# Using dict from above: Make a dictionary using the same keys
# but with the number of 't's in each value (consider upper and lower case)
dict_2 = dict_1.copy()
for item in dict_2:
    dict_2[item] = dict_1[item].lower().count('t')
print(dict_2)


# Sets
# Create sets s2, s3, s4 that contain numbers from 0-20
# divisible by 2, 3, 4 and display sets
s2 = set(range(0, 21, 2))
s3 = set(range(0, 21, 3))
s4 = set(range(0, 21, 4))
print(s2)
print(s3)
print(s4)

# Display if s3 is a subset of s2 (False)
print(s3.issubset(s2))

# Display if s4 is a subset of s2 (True)
print(s4.issubset(s2))

# Sets 2
# Create a set with letters in 'Python' and add 'i' to set
python = set('Python')
python.add('i')
print(python)

# Create a frozenset with the letters in 'marathon'
marathon = frozenset('marathon')
print(marathon)

# Display the union and intersection of the two sets
print(python.union(marathon))
print(python.intersection(marathon))
print(marathon.union(python))
print(marathon.intersection(python))
