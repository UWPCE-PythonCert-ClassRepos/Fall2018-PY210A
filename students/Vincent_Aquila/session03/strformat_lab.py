"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
assignment objective: String Formatting Lab
"""


# task 1
print("---Task 1")
"""
Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'
"""
t1 = (2, 123.4567, 10000, 12345.67)
print("file_{:03} : {:.2f} {:.2e} {:.2e}".format(t1[0], t1[1], t1[2], t1[3]))


# task 2
print("---Task 2")
"""
Using your results from Task One, repeat the exercise, but this time using an alternate
type of format string (hint: think about alternative ways to use .format() (keywords anyone?),
and also consider f-strings if you’ve not used them already).
"""
t2 = (2, 123.4567, 10000, 12345.67)
print(f'file_{t2[0]:03} : {t2[1]:.2f} {t2[2]:.2e} {t2[3]:.2e}')


# task 3
print("---Task 3")
"""
Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
to take an arbitrary number of values.
"""
def display_items(seq):
    l = len(seq)
    print(("There are {} items, and they are: " + ", ".join(["{}"]*l)).format(l, *seq))
display_items([2,4,7,12,5,19])


# task 4
print("---Task 4")
"""
Given a 5 element tuple:
(4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'
Hint: use index numbers to specify positions.
"""
t4 = (4, 30, 2017, 2, 27)
print("{:02} {} {} {:02} {}".format(t4[3], t4[4], t4[2], t4[0], t4[1]))

#5 task 5
print("---Task 5")
"""
- specifically use f-strings -
Here’s a task for you: Given the following four element list: ['oranges', 1.3, 'lemons', 1.1]
Write an f-string that will display: The weight of an orange is 1.3 and the weight of a lemon is 1.1

Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight
20% higher (that is 1.2 times higher).
"""
fruit1 = 'orange'
pounds1 = '1.3'
fruit2 = 'lemon'
pounds2 = '1.1'
x = 1.3
y = 1.1
print(f"The weight of an {fruit1} is {pounds1} and the weight of a {fruit2} is {pounds2}.")
print(f"The weight of an {fruit1.upper()} is {x * 1.2} and the weight of a {fruit2.upper()} is {y * 1.2}.")

#6 task 6
print("---Task 6")
print("These are my cats:")
print('{:10}{:10}{:10}{:10}{:10}{:10}'.format('Name', 'Watson', 'Age', '6', 'Cost', '$1,100.00'))
print('{:10}{:10}{:10}{:10}{:10}{:14}'.format('Name', 'Oscar', 'Age', '7', 'Cost', '$800.00'))
print('{:10}{:10}{:10}{:10}{:10}{:14}'.format('Name', 'Cleo', 'Age', '20', 'Cost', '$2,000.00'))

#extra task
print("---Extra Task")
a = (1,2,3,4,5,6,7,8,9,10)
print("".join(["  -    {}   "] * 10).format(* a))
