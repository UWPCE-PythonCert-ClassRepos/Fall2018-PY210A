#!/usr/bin/env Python3


#dict_lab.py
#Date: November 4th, 2018
#Created by: Carol Farris
#Purpose: dictionary Lab

"""
Remaining work:
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/dict_lab.html

Dict overview:
https://uwpce-pythoncert.github.io/PythonCertDevel/modules/DictsAndSets.html
"""

import math

"""Dictionary 1 lab"""

#create dictionary for Chris who lives in seattle and likes chocolate cake
personDict = {'name': 'Chris', 'city': 'Seattle', 'cake' : 'chocolate'}

#print the dictionary
print(personDict)

#delete the entry for cake
personDict.popitem()

#print the new dictionary
print(personDict)

#add key fruit with value mango to dictionary
personDict['fruit'] = 'Mango'

#print the new dictionary
print(personDict)

#display the dictionary keys in personDict (first for loop, then pythonic below that.)
for key in personDict:
    print(key)

personDict.keys()    

#display the dictionary keys in personDict (first for loop, then pythonic below that.)
for key in personDict:    
    print(personDict[ key ])

personDict.values()    


#Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print('cake'in personDict)

#Display whether or not “Mango” is a value in the dictionary (i.e. True).
print('Mango' in personDict.values())


"""Dictionary 2 lab"""


#Create new dictionary that has same values as dictionary above, but with values
#that show the number of t/T's in the previously assigned values.
alphabetDictionaryT = {}

for key in personDict:
	previousValue = personDict[ key ]
	numberTs = previousValue.lower().count('t')
	alphabetDictionaryT[ key ] = numberTs

print(alphabetDictionaryT)	

"""Sets"""
s2 = set([0,2,4,6,8,10,12,14,16,18,20])
print("numbers divisible by 2: ", s2)

s3 = set([0,3,6,9,12,15,18])
print("numbers divisible by 3: ", s3)

s4 = set([0,4,8,12,16,20])
print("numbers divisible by 4", s4)

print(s3.issubset(s2))
print(s4.issubset(s2))



"""Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
display the union and intersection of the two sets."""


    