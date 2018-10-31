# Lesson 03 Exercise: String Formatting Lab

# Task One
print("Task One")

# Write a format string that takes a 4 element tuple and produces: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
tuple_4 = (2, 123.4567, 10000, 12345.67)


def format_file(t):
    """
    Returns formatted string with filename, floating point number, integer, and long floating point number
    :param t: Four element tuple
    """
    # Pad filename with leading zeros if necessary
    file_name = "file_{:03d}".format(t[0])

    # Floating point number with two decimals
    file_float = "{:.2f}".format(t[1])

    # Integer in scientific notation with two decimals
    file_int = "{:.2e}".format(t[2])

    # Long floating point number in scientific notation with three significant figures
    file_long_float = "{:3.2e}".format(t[3])

    return "{} :   {}, {}, {}".format(file_name, file_float, file_int, file_long_float)


# Test
print(format_file(tuple_4))

# Task Two
print("\nTask Two")

# Use an alternative type of format string


def format_file_2(t):
    """
    Returns formatted string with filename, floating point number, integer, and long floating point number
    :param t: Four element tuple
    """
    file_name = "file_{:03d}".format(t[0])
    file_float = "{:.2f}".format(t[1])
    file_int = "{:.2e}".format(t[2])
    file_long_float = "{:3.2e}".format(t[3])
    return f"{file_name} :   {file_float}, {file_int}, {file_long_float}"


# Test
print(format_file_2(tuple_4))

# Task Three
print("\nTask Three")

# Rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to take an arbitrary number of values


def formatter(in_tuple):
    form_string = "the {} numbers are: "

    numbers = []

    for i in in_tuple:
        numbers.append("{:d}")

    form_string += ", ".join(numbers)

    return form_string.format(len(in_tuple), *in_tuple)


# Tests
tuple_1 = (2, 3, 5)
print(formatter(tuple_1))

tuple_2 = (2, 3, 5, 7, 9)
print(formatter(tuple_2))

# Task Four
print("\nTask Four")

# Use a 5 element tuple
tuple_5 = (4, 30, 2017, 2, 27)

# Use string formatting to print "02 27 2017 04 30"


def format_numbers(t):
    """
    Return a specific formatted string
    :param t: Five element tuple
    """
    return "{:02d} {} {} {:02d} {}".format(t[3], t[4], t[2], t[0], t[1])


print(format_numbers(tuple_5))

# Task Five
print("\nTask Five")

# Use this four element list
fruit = ["oranges", 1.3, "lemons", 1.1]

# Print sentence
print(f"The weight of an {fruit[0][:-1]} is {fruit[1]} and the weight of a {fruit[2][:-1]} is {fruit[3]}.")

# Change fruit names to upper case and make the weight 20% higher (1.2 x)
print(f"The weight of an {fruit[0][:-1].upper()} is {fruit[1]*1.2} and the weight of a {fruit[2][:-1].upper()} is {fruit[3]*1.2}.")

# Task Six
print("\nTask Six")

headers = ("ANIMAL", "AGE", "COST")

animals = [("zebra", 2, 400.5), ("giraffe", 5, 10000), ("lion", 10, 2000.25), ("whale", 100, 21350.85)]

# Print a table of several rows, but make sure things are aligned


def print_table(l):
    print("{:10}{:>10}{:>15}".format(*headers))

    for x in l:
        print("{:10}{:>10}{:>15}".format(x[0], x[1], ("{0:,.2f}".format(x[2]))))


# Test
print_table(animals)

print("\nBonus")
tuple_10 = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11)


def print_table_2(t):
    """
    Prints the tuple in columns that are 5 characters wide
    """
    for x in t: print(str(x).ljust(5, " "), end="")


print_table_2(tuple_10)
