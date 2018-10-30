


tuple = ( 2, 123.4567, 10000, 12345.67)

# TASK 1

# String formatting operator that will “pad” the number with zeros
print("file{0:0>3}:".format(2))

# Floating point number. You should display it with 2 decimal places shown.
a = 123.4567

# New version using f as format
print("%.2f" % a)

# Old version using .format
print("{:.2f}".format(a))

# Display '10000' in scientific notation, with 2 decimal places shown.
precision = 2
number_to_convert = 10000
print("%0.*e" % (precision, number_to_convert))

# Display 12345.67 in scientific notation with 3 significant figures
precision = 2
number_to_convert = 12345.67
print("%0.*e" % (precision, number_to_convert))

#Start with
tuple = ( 2, 123.4567, 10000, 12345.67)

#End with
print(("file{0:0>3}:".format(2)), ("{:.2f},".format(123.4567)), ("%0.*e," % (2, 10000)), ("%0.*e" % (2, 12345.67)))


# TASK 2

# TASK 3

# Rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to take arbitrary number of values
def formatter(seq):

	# Length measures length of arbitrary numbers
	length = len(seq)
	# Dynamic string to accomdate total length of string and output arbitrary numbers
	print(("The {} numbers are:" + ", ".join(["{}"] * length)).format(length, *seq))


formatter([2, 3, 4, 5, 6, 7, 78])

# Task 4

# Given 5 element tuple
tup = (4, 30, 2017, 2, 27)
# Use format to convert single value elements to two integers
print(format(tup[3], "02"), tup[4], tup[2], format(tup[0], "02"), tup[1])

# Task 5
f_list = ['oranges', 1.3, 'lemons', 1.1]

# Use slicing to make the fruits singular and use index to call list items
f"The weight of an {f_list[0][:-1]} is {f_list[1]} and the weight of a {f_list[2][:-1]} is {f_list[3]}"

# Add upper to fruit index and increase weight by 20%
f"The weight of an {f_list[0][:-1].upper()} is {f_list[1] * 1.2} and the weight " \
	f"of a {f_list[2][:-1].upper()} is {f_list[3] * 1.2}"


# Task 6

'{:5}{:20}{:3}{:15}{:5}{:5}'.format('Name:', 'Zach Cooper', 'Age:', '30', 'Cost:', '1000')


