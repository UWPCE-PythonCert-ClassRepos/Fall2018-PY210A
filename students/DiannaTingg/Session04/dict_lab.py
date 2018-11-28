# Lesson 04 Exercise: Dictionary and Set Lab

# Dictionaries 1
print("Dictionaries 1")

# Create a dictionary
dict_1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

# Print the dictionary
print(f"Dictionary contains: {dict_1}")

# Delete the entry for "cake"
del dict_1["cake"]

# Print the dictionary
print(f"Dictionary contains {dict_1}")

# Add entry for "fruit" with "Mango" and print dictionary
dict_1["fruit"] = "Mango"
print(f"Dictionary contains {dict_1}")

# Print dictionary keys
d_keys = []

for key in dict_1:
    d_keys.append(key)

print("Dictionary keys are: {}".format(", ".join(d_keys)))

# Print the dictionary values
d_values = []

for k, v in dict_1.items():
    d_values.append(v)

print("Dictionary values are: {}".format(", ".join(d_values)))

# Check if "cake" is a key in the dictionary
print('Is "cake" in the dictionary? {}'.format("cake" in dict_1))

# Check if "Mango" is a value in the dictionary
print('Is "Mango" a value in the dictionary? {}'.format("Mango" in dict_1.values()))

# Dictionaries 2
print("\nDictionaries 2")

# Make a dictionary with the same keys as exercise 1, but the value is the number of t's in each value
dict_2 = {}

for x in dict_1:
    dict_2[x] = x.lower().count("t")

print(f"Dictionary contains: {dict_2}")

# Sets 1
print("\nSets 1")

# Using numbers 0-20, create sets for numbers divisible by 2, 3, 4
s2 = set()
s3 = set()
s4 = set()

for x in range(21):
    if x % 2 == 0:
        s2.add(x)
    if x % 3 == 0:
        s3.add(x)
    if x % 4 == 0:
        s4.add(x)

# Print sets
print(f"Set 2 = {s2}")
print(f"Set 3 = {s3}")
print(f"Set 4 = {s4}")

# Is s3 a subset of s2?
print("Is Set 3 a subset of Set 2?: {}".format(s3.issubset(s2)))

# Is s4 a subset of s2?
print("Is Set 4 a subset of Set 2?: {}".format(s4.issubset(s2)))

# Sets 2
print("\nSets 2")

# Create a set with the letters in "Python"
word_1 = "python"

p = set()

for x in word_1:
    p.add(x)

print(f"P set contains: {p}")

# Add the letter "i" to the set
p.add("i")
print(f"P set now contains: {p}")

# Create a frozenset with the letters in marathon
word_2 = "marathon"

m = set()

for x in word_2:
    m.add(x)

frozen_m = frozenset(m)

print(f"M set contains: {frozen_m}")

# Display the union and intersection of the two sets.
print("The union of the sets is: {}".format(p.union(m)))

print("The intersection of the sets is {}".format(p.intersection(m)))
