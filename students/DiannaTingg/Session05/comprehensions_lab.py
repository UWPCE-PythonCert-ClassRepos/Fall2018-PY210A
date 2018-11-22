# Lesson 05 Exercise: Comprehensions Lab

# Count Even Numbers
# Using a list comprehension, return the number of even integers in the given list.


def count_evens(l):
    return len([i for i in l if i % 2 == 0])


assert count_evens([2, 1, 2, 3, 4]) == 3
assert count_evens([2, 2, 0]) == 3
assert count_evens([1, 3, 5]) == 0

# Revisiting the Dictionary and Set Lab
food_prefs = {"name": "Chris", "city": "Seattle", "cake": "chocolate", "fruit": "mango",
              "salad": "greek", "pasta": "lasagna"}

# Print dictionary using a string format method
print("{name} is from {city} and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta."
      .format(**food_prefs))

# Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string)
# the hex() function gives you the hexidecimal representation of a number as a string


def hex_dictionary():
    my_dict = dict([(i, hex(i)) for i in range(16)])
    return my_dict


print(hex_dictionary())

# Make another hex dictionary, but use a one line dictionary comprehension


def better_hex_dictionary():
    return {key: hex(key) for key in range(16)}


print(better_hex_dictionary())

# Using the food_prefs dictionary: Make a dictionary using the same keys but with the number of ‘a’s in each value.


def a_values_dict(original_dict):
    return {key: value.count("a") for key, value in original_dict.items()}


print(a_values_dict(food_prefs))

# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
s2 = set(i for i in range(21) if i % 2 == 0)
s3 = set(i for i in range(21) if i % 3 == 0)
s4 = set(i for i in range(21) if i % 4 == 0)

print("s2:", s2)
print("s3:", s3)
print("s4:", s4)

# Create a sequence that holds all the divisors you might want – could be any number of divisors.
# Loop through that sequence to build the sets up. You will end up with a list of sets – one set for each divisor.


def make_sets(divisor_list):
    sets = []

    for x in divisor_list:
        subset = set(i for i in range(21) if i % x == 0)
        sets.append(subset)

    return sets


print(make_sets([2, 3, 4, 5]))

# Extra credit: do it all as a one-liner by nesting a set comprehension inside a list comprehension.


def make_better_sets(divisor_list):
    return [set(i for i in range(21) if i % number == 0) for number in divisor_list]


print(make_better_sets([2, 3, 4, 5]))
