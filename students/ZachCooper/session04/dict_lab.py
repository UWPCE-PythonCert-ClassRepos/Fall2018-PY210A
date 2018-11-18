 #!/usr/bin/env python


# DICTIONARIES #1
# Create a dictionary containing "name", "city", and "cake" for
# Switching it up to make a dictionary for myself
# Born in Chitown and love my Grandmothers cheesecake

dict = {"name": "Zach",
     "city": "Chicago",
     "pie": "Chicago Deep-dish Pizza"}

# Display dictionary
print(dict)

# Delete the entry "cake" ane display dict
del dict["pie"]
print(dict) 

# Add an entry "fruit" with "Mango" as value; display dict
dict["fruit"] = "Mango"

print(dict)

# Display the dict keys
print(dict.keys())

# Display the dict values
print(dict.values())

# Display if "cake" is a key in the dict or not (False)
print('pie' in dict)

# Display if "Mango" is a value in the dict or not (True)
print('Mango' in dict.values())

#DICTIONARIES #2
#Make a dictionary using the same keys but with the number of 'c's in each value as the value
dict2 = {}
for key, value in dict.items():
    # Can you use an abbreviation value as val. Returns int has not object count
    dict2[key] = value.count('c')
    print(dict2)

#SETS
# Create s2, s3, and s4 as sets that contain numbers from 0 through 20, divisible by 2, 3, & 4
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

#Display the sets
print(s2)
print(s3)
print(s4)

# Display if s3 is a subst of s2
print(s3.issubset(s2))

# Is s4 a subset of s2
print(s4.issubset(s2))

#SETS2
# Create a set with the letters in 'Python' and add 'i' to the set
set_python = set('Python')
set_python.add('i')

print(set_python)

# Create a frozenset with the letters in 'marathon'
fs = frozenset('Marathon')

# Display union and instersection of the two sets
print("union:", s.union(fs))
print("intersection:", s.intersection(fs))













