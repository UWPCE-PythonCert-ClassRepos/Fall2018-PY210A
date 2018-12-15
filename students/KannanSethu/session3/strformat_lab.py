#!/usr/bin/env python3
"""
Task One
Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'
So you need to find a string formatting operator that will “pad” the number with zeros for you.
The second element is a floating point number. You should display it with 2 decimal places shown.
The third value is an integer, but could be any number. \
You should display it in scientific notation, with 2 decimal places shown.
The fourth value is a float with a lot of digits – \
display it in scientific notation with 3 significant figures.
"""
IN_TUPLE = (2, 123.4567, 10000, 12345.67)
FORMAT_FILE = "file_00{:d}"
FORMAT_2DEC = "{:.2f}"
FORMAT_2EXP = "{:.2e}"
FORMAT_3G = "{:.3g}"
FORMAT_STRING = FORMAT_FILE+' :  '+FORMAT_2DEC+', '+FORMAT_2EXP+', '+FORMAT_3G
OUT_TUPLE = FORMAT_STRING.format(*IN_TUPLE)
"""
Task Two
Using your results from Task One, repeat the exercise, but this time using an alternate type of \
format string (hint: think about alternative ways to use .format() (keywords anyone?), and also \
consider f-strings if you’ve not used them already).
"""
OUT_TUPLE_2 = f'file_00{IN_TUPLE[0]:d} :  {IN_TUPLE[1]:.2f}, {IN_TUPLE[2]:.2e}, {IN_TUPLE[3]:.3g}'
"""
Task Three
Dynamically Building up Format Strings
"""
def formatter(in_tuple):
    """
    Rewrite:
    "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
    to take an arbitrary number of values.
    Hint: You can pass in a tuple of values to a function with a *:
    """
    length = len(in_tuple)
    in_exp = '{:d}, '*(len(in_tuple)-1)+'{:d}'
    format_string = f'the {length} numbers are: {in_exp}'
    return format_string.format(*in_tuple)

"""
Task Four
Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'
"""
IN_TUPLE_2 = (4, 30, 2017, 2, 27)
OUT_TUPLE_2 = f'{IN_TUPLE_2[3]:0>2} {IN_TUPLE_2[4]:0>2} {IN_TUPLE_2[2]} \
{IN_TUPLE_2[0]:0>2} {IN_TUPLE_2[1]:0>2}'

"""
Task Five
Here’s a task for you: Given the following four element list:
['oranges', 1.3, 'lemons', 1.1]
Write an f-string that will display:
The weight of an orange is 1.3 and the weight of a lemon is 1.1
"""
IN_TUPLE_3 = ['oranges', 1.3, 'lemons', 1.1]
OUT_TUPLE_3 = f'The weight of an {IN_TUPLE_3[0][:-1]} is {IN_TUPLE_3[1]} and \
the weight of a {IN_TUPLE_3[2][:-1]} is {IN_TUPLE_3[3]}'
"""
Now see if you can change the f-string so that it displays the names of the fruit in upper case, \
and the weight 20% higher (that is 1.2 times higher).
"""
OUT_TUPLE_3_1 = f'The weight of an {IN_TUPLE_3[0][:-1].upper()} is {IN_TUPLE_3[1]*1.2} and \
the weight of a {IN_TUPLE_3[2][:-1].upper()} is {IN_TUPLE_3[3]*1.2}'

"""
Task Six
Often it’s convenient to display data in columns. \
String formatting helps to make this straightforward.
Write some Python code to print a table of several rows, each with a name, an age and a cost. \
Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
"""
#table_data = [('John', 32, '10000'), ('Joseph', 40, '20000'), ('Mary', 50, '10'), ('Catherine', 60, '200'), ('Sheniqua', 32, '1000000'), ('Bonquisha', 40, '2000000')]
TABLE_DATA = [('John', 32, 10000.65000), \
                ('Joseph', 40, 20000), \
                ('Mary', 50, 10), \
                ('Catherine', 60, 200), \
                ('Sheniqua', 32, 1000000.65000), \
                ('Bonquisha', 40, 2000000)]


for name, age, cost in TABLE_DATA:
    TABLE_FORMAT = f'Name: {name:<20} Age: {age:<5} Cost: {cost:<10.2f}'
    print(TABLE_FORMAT)

"""
And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print \
the tuple in columns that are 5 charaters wide? It’s easily done on one short line!
"""
TEST_TUPLE = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(('{:5}'*len(TEST_TUPLE)).format(*TEST_TUPLE))

