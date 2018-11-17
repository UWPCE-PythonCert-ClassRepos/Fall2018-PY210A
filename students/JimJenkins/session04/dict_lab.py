#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr)
Date: 11/05/2018

"""
#create a dictionary
cake_order = {}
cake_order['name'] = 'Chris'
cake_order['city'] = 'Seattle'
cake_order['cake'] = 'Chocolate'
print(cake_order)


#remove entry for cake
result = cake_order.pop('cake')
print(cake_order)


#add key for fruit with mango
cake_order['fruit'] = 'Mango'
print(cake_order)


#display the dict keys and then values
print(cake_order.keys())
print(cake_order.values())

#display whether or not “cake” is a key in the dictionary
result_cake = 'cake' in cake_order.keys()
if result_cake is True:
    print('cake - its in there')
else:
    print('cake - its not there')

#display whether or not “Mango” is a value in the dictionary (i.e. True).
result_mango = 'Mango' in cake_order.values()
if result_mango is True:
    print('mango - its in there')
else:
    print('mango - its not there')

#create dict with keys and values
cake_order = {}
cake_order['name'] = 'Chris'
cake_order['city'] = 'Seattle'
cake_order['cake'] = 'Chocolate'


#function to count a specific character in a word
def count_letters(word, char):
  letter_count = 0
  for letter in word:
      if letter == char:
        letter_count += 1
  return letter_count

words = list(cake_order.values())

letter_dict = {}
for word in words:
    letter_dict[word] = count_letters(word,'t')

print(letter_dict)

#create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4. Display the sets.
s2 = {0}
for i in range(0, 21):
    if i % 2 == 0:
        s2.add(i)
print(s2)

s3 = {0}
for i in range(0, 21):
    if i % 3 == 0:
        s3.add(i)
print(s3)

s4 = {0}
for i in range(0, 21):
    if i % 4 == 0:
        s4.add(i)
print(s4)

#if s3 is a subset of s2 (False)
print('s3 is a subset of s2: ', s3.issubset(s2))

#if s4 is a subset of s2 (True).
print('s4 is a subset of s2: ', s4.issubset(s2))

def word_sort(word):
    word_set = set()
    for letter in word:
        word_set.add(letter)
    return word_set

#create a set with the letters in ‘Python’ and add ‘i’ to the set.
python_set = word_sort('Python')
python_set.add('i')
print(python_set)

#create a frozenset with the letters in ‘marathon’.
marathon_set = word_sort('marathon')
frozenset(marathon_set)
print(marathon_set)

#display the union and intersection of the two sets.

# union
print("Union: ", python_set | marathon_set)

# intersection
print("Intersection: ", python_set & marathon_set)
