#!/usr/bin/env python3

# Dictionaries 1

# Create a dictionary 
dic = {
        "name" : "Chris",
        "city" : "Seattle",
        "cake" : "Chocolate"
}

# Display the dictionary
print(dic)

# Delete the entry for “cake”
dic.pop('cake')

# Display the dictionary
print(dic)

# Add an entry for “fruit” with “Mango” and display the dictionary
dic["fruit"] = "Mango"

# Display the dictionary keys.
print(dic.keys())

# Display the dictionary values
print(dic.values())

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print('cake' in dic)

# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print('Mango' in dic.values())

# Dictionaries 2

dic = {
        "name" : "Chris",
        "city" : "Seattle",
        "cake" : "Chocolate"
}

# Make a dictionary using the same keys but with the number of ‘t’s in each value as the value
for i in dic.keys():
    val = len([x for x in dic[i] if x == 't' or x == 'T'])
    dic[i] = val

print(dic)

# Sets

# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.

s2 = set([x for x in range(0,21) if x % 2 == 0])

s3 = set([x for x in range(0,21) if x % 3 == 0])

s4 = set([x for x in range(0,21) if x % 4 == 0])

# Display the sets.
print(s2)
print(s3)
print(s4)

# Display if s3 is a subset of s2 (False)
print(s3.issubset(s2))

# and if s4 is a subset of s2 (True).
print(s4.issubset(s2))

# Sets 2
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
a_set = set([x for x in 'Python'])
a_set.add('i')
print(a_set)

# Create a frozenset with the letters in ‘marathon’.
a_frozenset = frozenset([x for x in 'marathon'])
print(a_frozenset)

# display the union and intersection of the two sets.
print(a_set.union(a_frozenset))
print(a_set.intersection(a_frozenset))










