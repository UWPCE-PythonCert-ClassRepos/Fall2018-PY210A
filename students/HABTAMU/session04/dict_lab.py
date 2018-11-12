#!/usr/bin/env python3
"""Dictionaries 1"""
my_dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(my_dict)

# Delete the entry for “cake”.
# my_dict.popitem()
# print(my_dict)

# Add an entry for “fruit” with “Mango” and display the dictionary.
dict = my_dict
my_dict['fruit'] = 'Mango'
print(dict)

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
if 'Cake' in my_dict.keys():
    print("Actually 'cake' is a key in the dictionary")
else:
    print("i guess not!")

# Display whether or not “Mango” is a value in the dictionary (i.e. True).
if 'Mango' in my_dict.values():
    print("Actually 'Mango' is a values in the dictionary")
else:
    print("i guess not!")
