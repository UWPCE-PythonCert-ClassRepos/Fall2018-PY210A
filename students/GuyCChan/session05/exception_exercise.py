"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.
Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun
first_try = ['spam', 'cheese', 'mr death']
try:
    joke = fun(first_try[0])
except NameError:
    more_joke = fun(first_try[1])
# Something's not right, picking up SyntaxError even at the last commented line.
try:
    not_joke = fun(first_try[2])
except SyntaxError:
    print("Run Away!")
else:
    print(not_joke)
# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)
langs = ['java', 'c', 'python']
try:
    more_joke = more_fun(langs[0])
except IndexError:
    even_more_joke = more_fun(langs[1])
finally:
    last_fun()
