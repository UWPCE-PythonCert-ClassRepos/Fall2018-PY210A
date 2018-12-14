#!/usr/bin/env python3

"""
Dictionary and Set Lab with comprehensions
"""

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

# Print dict by passing it to str format method
print("{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.".format(**food_preps))

# Use list comprehension to build dict of numbers from 0-15
# and the hexadecimal equivalent (string is fine)
dict({(num, hex(num)) for num in range(16)})

# Do the previous entirely with a dict comprehension in one line
{num: hex(num) for num in range(16)}

#  Use dict from item 1: Make a dict using the same keys
# but with the number of 'a's in each value. Either edit the dict in place
# or make a new one. If you edit in place, make a copy first!
{key: value.count('a') for key, value in food_prefs.items()}

# Create sets s2, s3, and s4 that contain numbers from 0-20
# divisible 2, 3, and 4
s2 = {i for i in range(21) if not i % 2}
s3 = {i for i in range(21) if not i % 3}
s4 = {i for i in range(21) if not i % 4}

# Create sequence that holds any arbitrary divisors
# Loop through that sequence to build sets - you will end up with
# a list of sets - one set for each divisor in your sequence
divisors = [2, 3, 4]
my_sets = []

for idx in divisors:
    my_sets.append({i for i in range(21) if not i % idx})
