#!usr/bin/env python3

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

#1 Print the dict by passing it to a string format method

print("{name} is from {city}, and he likes {cake}, {fruit} fruit, {salad} salads, and {pasta}".format(**food_prefs))

#2 Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine). 
# (the hex() function gives you the hexidecimal representation of a number as a string)
# Here is the LONG version:
nums_range = range(16)
hexes = []
for num in nums_range:
    hexes.append(hex(num))

hex_dict = dict(zip(nums_range, hexes))

print(hex_dict)

# Here is the list comprehension version:
val = (hex(i) for i in range(16))
hex_dict = dict(zip(range(16), val))
print(hex_dict)

# or with a one liner but it is a little hard to read
hex_dict = dict(zip(range(16), (hex(i) for i in range(16))))
print(hex_dict)


#3 Do the previous entirely with a dict comprehension – should be a one-liner
new_dict = {i: hex(i) for i in range(16)}
print(new_dict)


#4 Using the dictionary from item (1): Make a dictionary using the same keys but with the number of ‘a’s in each value. 
# You can do this either by editing the dict in place, or making a new one. If you edit in place make a copy first!
# LONG VERSION
food_prefs = {}

food_prefs2 = food_prefs # Curious as to why I would need to make a copy of the first

food_dict = {}
for key, val in food_prefs2.items():
    food_dict[key] = val.count('a')
print(food_dict) 

# SHORT dict comprehension version
food_dict = {key: food_prefs[i].count('a') for i in food_prefs}


# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
# This is the long version!!!
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

# Here is how I can shorten it using set comprehension
s2 = set([i for i in range(21) if not i % 2])
s3 = set([i for i in range(21) if not i % 3])
s4 = set([i for i in range(21) if not i % 4])

print(s2)
print(s3)
print(s4)


# create a sequence that holds all the divisors you might want
divisors = range(2,10)
# loop through that sequence to build the sets up
seq = []
for i in divisors:
    set_n = {s for s in range(21) if s % i == 0}
    seq.append(set_n)
print(seq)

# do it all as a one-liner
seq = [{s for s in range(21) if s % i == 0} for i in divisors]
print(seq)























