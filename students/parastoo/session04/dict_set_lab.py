#!/usr/bin/env python3

print('Dictionaries 1')
#Create a dictionary

my_dict = {'name' : 'Chris',
           'city' : 'Seattle',
           'cake' : 'Chocolate'}

#Display the dictionary.

print('{name} is from {city}, and likes {cake}'.format(**my_dict))

# Delete the entry for 'cake'
# Display the dictionary

print(my_dict.popitem())

#Add an entry for “fruit” with “Mango” and display the dictionary.
my_dict['fruit'] = 'Mango'
print(my_dict.keys())
print(my_dict.values())
print('cake' in my_dict)
print('Mango' in my_dict.values())

#############

print('Dictionaries 2')
'''
Using the dictionary from item 1: Make a dictionary
using the same keys but with the number of ‘t’s in
each value as the value (consider upper and lower case?)
'''

my_dict2 = {}
for k, v in my_dict.items():
    my_dict2[k] = v.count('t')
print(my_dict2)

###############

print('Sets')

'''Create sets s2, s3 and s4 that contain numbers from
zero through twenty, divisible by 2, 3 and 4.
'''

s2= set([i for i in range(21) if i%2 == 0])
print(s2)
s3= set([i for i in range(21) if i%3 == 0])
print(s3)
s4= set([i for i in range(21) if i%4 == 0])
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

####################

print('Sets 2')

#Create a set with the letters in ‘Python’ and add ‘i’ to the set.

ps= set([l for l in 'Python'])
ps.add('i')
print(ps)

#Create a frozenset with the letters in 'marathon'.

fs= frozenset(([l for l in 'marathon']))
print(fs)
print(ps.union(fs))
print(ps.intersection(fs))