#!/usr/bin/env python3
'''
some comprehension exercises
count even numbers
dict and set comprehensions
'''

# count even numbers

def count_evens(nums):
    c = [x for x in nums if x % 2 == 0]
    return len(c)

assert count_evens([2, 1, 2, 3, 4]) == 3
assert count_evens([2, 2, 0]) == 3
assert count_evens([1, 3, 5]) == 0

# dict and set comprehensions

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

# Print the dict by passing it to a string format method
string_dic = "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, \
{salad} salad, and {pasta} pasta".format(**food_prefs)
print(string_dic)

# Using a list comprehension, build a dictionary of numbers from zero to
# fifteen and the hexadecimal equivalent
val = [hex(i) for i in range(16)]
d = dict(zip(range(16), val))
print(d)

# Do the previous entirely with a dict comprehension
d = {i: hex(i) for i in range(16)}
print(d)

# Using the dictionary from item (1): Make a dictionary using the same keys but
# with the number of ‘a’s in each value.
d = {i: food_prefs[i].count('a') for i in food_prefs}
print(d)

# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4
# a.x Do this with one set comprehension for each set
s2 = {s for s in range(21) if s % 2 == 0}
s3 = {s for s in range(21) if s % 3 == 0}
s4 = {s for s in range(21) if s % 4 == 0}

# create a sequence that holds all the divisors you might want
divisors = range(2,10)
# loop through that sequence to build the sets up
l = []
for i in divisors:
    set_n = {s for s in range(21) if s % i == 0}
    l.append(set_n)
print(l)

# do it all as a one-liner
l = [{s for s in range(21) if s % i == 0} for i in divisors]
print(l)




