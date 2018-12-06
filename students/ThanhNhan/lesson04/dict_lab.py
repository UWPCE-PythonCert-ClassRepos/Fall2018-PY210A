#!/usr/bin/env pythone3
import math

#Dictionaries 1

#Create a dictionary containing “name”, “city”, and “cake” 
d_cake = {'name': 'Chris', 'city':'Seattle',  'cake': 'Chocolate'}
keys = d_cake.keys() #view objects keys
values = d_cake.values() #view objects value
item = d_cake.items() # view object items
print(d_cake)
print(item)

del d_cake['cake'] #delete the entry of the cake
print(d_cake) #display cake using dictionary

d_cake['fruit'] = 'Mango' #add entry Mango to fruit
print(keys) #display keys 
print(values) #display values
print('cake' in d_cake.keys()) #display wether or not cake in keys
print('Mango' in d_cake.values())  #display wether or not Mango in value


#Dictionaries 2
#Using the same keys but with the number of ‘t’s 
#in each value as the value (consider upper and lower case?).
# a_key = {}

# for key, val in d_cake.items():
# 	a_key[key] = val.count('t')
# print (a_key)

#change go upper
for key, val in d_cake.items():
	d_cake[key] = val.count('t' or 'T')
print (d_cake)

# Create sets s2, s3 and s4 that contain numbers from zero through 
#twenty, divisible by 2, 3 and 4.
# Display the sets.

s2 = set()
s3 = set()
s4 = set()

for x in range(21):
	if (x % 2 == 0):
		s2.update([x])
	if (x % 3 == 0):
		s3.update([x])
	if (x % 4 == 0):
		s4.update([x])

print(s2)
print(s3)
print(s4)

# Display if s3 is a subset of s2 (False)
print (s3.issubset(s2))


# and if s4 is a subset of s2 (True).
print (s4.issubset(s2))


# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
s = set()
s.update('Python')
s.add('i')
print ("set:", s)

# Create a frozenset with the letters in ‘marathon’.
fs = frozenset('marathon')
print(fs)

# display the union and intersection of the two sets.
print("union:", s.union(fs))
print("intersection: ", s.intersection(fs))
