#!/usr/bin/env python3

"""
PY210A-Session03
Cheng Liu
String formating
"""

print("file_{:03d} : {:9.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67))


values = input("Enter three numbers: ")
print("the 3 numbers are: {:d}, {:d}, {:d}".format(values(0), values(1), values(2)))


element = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {element[0]} is {element[1]} and the weight of a {element[2]} is {element[3]}")


