 #!/usr/bin/env python

"""
dict/set lab solutions: MODIFIED Chris' version.
"""

# Create a dictionary containing "name", "city", and "cake" for
# "Santa" from "NorthPole" who likes "Lemon".


gen_d = {"name": "Santa",
     "city": "NorthPole",
     "cake": "Lemon"}

# Display the dictionary.
print("\nGeneric printing of dictionary {}".format(gen_d))
print()

# or something fancier, like:
print ("{name} is from {city}, and likes {cake} cake.".format(name=gen_d['name'],
                                                              city=gen_d['city'],
                                                              cake=gen_d['cake']))

# But if that seems like unnecceasry typing -- it is:
# we'll learn the **d form is session05:
print("\tUsing the ** form")
print("{name} is from {city}, and likes {cake} cake.\n".format(**gen_d))


# Delete the entry for "cake".
# Display the dictionary.

print("Deleting the cake entry.....")
del gen_d["cake"]

print(gen_d)

# Add an entry for "fruit" with "Mango" and display the dictionary.

print("Now let's add in a fruit to the dictionary")
gen_d['fruit'] = 'Mango'

print(gen_d)

# Display the dictionary keys.

print("\n\tHere are the keys:", gen_d.keys())

# Display the dictionary values.

print("\n\tHere are the values:", gen_d.values())

# Display whether or not "cake" is a key in the dictionary (i.e. False) (now).


print("\nIs the word cake in the dict? And the answer is: ", ('cake' in gen_d))

# Display whether or not "Mango" is a value in the dictionary.

print("Is the word Mango in the dictionary? The answer is: ", ('Mango' in gen_d.values()),"\n")

# Using the dict constructor and zip, build a dictionary of numbers
# from zero to fifteen and the hexadecimal equivalent (string is fine).
# did you find the hex() function?"
nums = range(16)
hexes = []
for num in nums:
    hexes.append(hex(num))

print("Built list of hexified numbers *** \n", hexes)

print("Then we package together the decimal:hex pairing ***")
hex_dict = dict(zip(nums, hexes))

print(hex_dict,"\n")


# Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of 't's in each value.

print("Using the Santa Dictionary", gen_d.items())

a_dict = {}
for key, val in gen_d.items():
    a_dict[key] = val.count('t')
print("This dictionary is derived from Santa dictionary using count of letter t for values", a_dict, "\n")


# replacing the values in the original dict:
for key, val in gen_d.items():
    gen_d[key] = val.count('t')
print("Replace in orig dict: ","\t" ,gen_d)

# Or the direct way -- update() is very handy!
gen_d.update(a_dict)
print("Or the update method:","\t", gen_d)

# Create sets s2, s3 and s4 that contain numbers from zero through
# twenty, divisible 2, 3 and 4.

# Display the sets.

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


# Display if s3 is a subset of s2 (False)
print(s3.issubset(s2))

# and if s4 is a subset of s2 (True).
print(s4.issubset(s2))

# Create a set with the letters in 'Python' and add 'i' to the set.

s = set('Python')
s.add('i')

print(s)

# maybe:
s = set('Python'.lower())  # that wasn't specified...
s.add('i')

# Create a frozenset with the letters in 'marathon'

fs = frozenset('marathon')

# display the union and intersection of the two sets.

print("union:", s.union(fs))
print("intersection:", s.intersection(fs))

# note that order doesn't matter for these:

print("union:", fs.union(s))
print("intersection:", fs.intersection(s))
