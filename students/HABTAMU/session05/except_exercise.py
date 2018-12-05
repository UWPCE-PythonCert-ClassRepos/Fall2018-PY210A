#!/usr/bin/python

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun


# Figure out what the exception is, catch it and while still
# in that catch block, try again with the second item in the list
first_try = ['spam', 'cheese', 'mr death']
for i, name in enumerate(first_try[:2]):
    try:
        joke = fun(first_try[i])
        print(joke)
    except NameError as err:
        #raise NameError("name 's' is not defined message")
        print("\n Exception :-> NameError {}:".format(err))

# Here is a try/except block. Add an else that prints not_joke
try:
    not_joke = fun(first_try[2])
except SyntaxError:
    print('Run Away!')
    raise NameError("name 's' is not defined")
else:
    print(not_joke)

# What did that do? You can think of else in this context, as well as in
# loops as meaning: "else if nothing went wrong"
# (no breaks in  loops, no exceptions in try blocks)

# Figure out what the exception is, catch it and in that same block
#
# try calling the more_fun function with the 2nd language in the list,
# again assigning it to more_joke.
#
# If there are no exceptions, call the more_fun function with the last
# language in the list

# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)

langs = ['java', 'c', 'python']
# for i, name in enumerate(langs):
while True:
    try:
        more_joke = more_fun(langs[1])
        print(more_joke)
        last_fun()
    except IndexError as in_err:
        print("\n2nd Exception :-> IndexError: {}".format(str(in_err)))   
    else:
        more_joke = more_fun(langs[2])
        print("Nothing to return {}".format(more_joke))
    break
