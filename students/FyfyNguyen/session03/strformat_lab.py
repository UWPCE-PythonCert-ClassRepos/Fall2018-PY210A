#!/usr/bin/env python3

"""
String formatting lab
"""

# Task One 
print("file_{:03d}: {:.2f}, {:.2e}, {:.3e}".format(
        2, 123.4567, 10000, 12345.67))

# Task Two
tup = 2, 123.4567, 10000, 12345.67

# old style
print("file_00%d: %.2f, %.2e, %.3e" % (tup[0], tup[1], tup[2], tup[3]))

# f-string
print(f"file_{tup[0]:03d}: {tup[1]:.2f}, {tup[2]:.2e}, {tup[3]:.3e}")


# Task Three
# Format arbitrary object just using {}
# Multiply a list by length of the sequence to get number of "{}" needed
# Use str.join() method to join seq separated by commas
def formatter(seq):
    seq_len = len(seq)
    string = ("the {} numbers are: " + ", ".join(["{}"]*seq_len)).format(
            seq_len, *seq)
    return string.format(*seq)

# Task Four
print(formatter((4, 30, 2017, 2, 27)))

num = (4, 30, 2017, 2, 27)
print("{:02d} {} {} {:02d} {}".format(num[3], num[4], num[2], num[0], num[1]))

# Task Five
fruit = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {fruit[0][0:-1]} is {fruit[1]} and the weight of a {
        fruit[2][0:-1]} is {fruit[3]}")

print(f"The weight of an {fruit[0][0:-1].upper()} is {fruit[1] * 1.2} and the "
      "weight of a {fruit[2][0:-1].upper()} is {fruit[3] * 1.2}")

# Task Six
data = [("Beyonce", 37, 355.00),
        ("Jay-Z", 48, 810.00),
        ("Blue Ivy", 6, 1, 165.00)
        ]

print("{:20s} | {:5s} | {:8s}".format("Name", "Age", "Price"))
print("-" * 42)
for item in data:
    print("{:20s}   {:5d}   $ {:8,.2f}".format(*item))
