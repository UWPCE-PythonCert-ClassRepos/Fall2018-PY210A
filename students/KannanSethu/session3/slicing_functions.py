"""some functions that take a sequence as an argument, and return a copy of that sequence"""

A_STRING = "this is a string"
A_TUPLE = (2, 54, 13, 12, 5, 32)


def exchange_first_last(seq):
    """ with the first and last items exchanged """
    return seq[-1:] + seq[1:-1] + seq[0:1]


assert exchange_first_last(A_STRING) == "ghis is a strint"
assert exchange_first_last(A_TUPLE) == (32, 54, 13, 12, 5, 2)

def every_other_removed(seq):
    """with every other item removed"""
    return seq[0::2]

assert every_other_removed(A_STRING) == "ti sasrn"
assert every_other_removed(A_TUPLE) == (2, 13, 5)


def remove_first_last_n(seq):
    """    with the first and last 4 items removed, and every other item in between """
    return seq[4:-4:2]

assert remove_first_last_n(A_STRING*2) == " sasrnti sas"
assert remove_first_last_n(A_TUPLE*2) == (5, 2)

def exchange_reverse(seq):
    """    with the elements reversed"""
    return seq[::-1]

assert exchange_reverse(A_STRING) == "gnirts a si siht"
assert exchange_reverse(A_TUPLE) == (32, 5, 12, 13, 54, 2)

def mixed_third(seq):
    """    with the last third, then first third, then the middle third in the new order """
    return seq[len(seq)//3:]+seq[:len(seq)//3]

assert mixed_third(A_STRING) == "is a stringthis "
assert mixed_third(A_TUPLE) == (13, 12, 5, 32, 2, 54)