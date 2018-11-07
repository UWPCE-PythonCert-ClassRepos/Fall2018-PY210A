#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr)
Date: 10/30/2018

"""

#functions
def exchange_first_last(seq):
    l = seq
    l_start = l[:1]
    l_end = l[-1:]
    l_middle = l[1:-1]
    l_final = l_end + l_middle + l_start
    return (l_final)


def every_other_removed(seq):
    l = seq
    l_seq = l[::2]
    return l_seq


def first4_last4_removed(seq):
    l = seq
    l_seq = l[4:-4]
    l_reversed = l_seq[::2]
    return l_reversed


def reversed(seq):
    l = seq
    l_seq = l[::-1]
    return l_seq


def thirds(seq):
    l = seq
    length = len(l) // 3
    l_first = l[:len(l) // 3]
    l_last = l[-(length):]
    l_middle = l[len(l_first):-(len(l_last))]
    l_new = l_last + l_first + l_middle
    return l_new


#strings and tuples
a_string = 'aabbccddeeffgghh'
a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)


#print tuples and strings
print(exchange_first_last(a_tuple))
print(every_other_removed(a_tuple))
print(first4_last4_removed(a_tuple))
print(reversed(a_tuple))
print(thirds(a_tuple))

print(exchange_first_last(a_string))
print(every_other_removed(a_string))
print(first4_last4_removed(a_string))
print(reversed(a_string))
print(thirds(a_string))


#unit tests
assert exchange_first_last(a_string) == "habbccddeeffggha", 'exchange_first_last string result incorrect'
assert exchange_first_last(a_tuple) == (16, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1), 'exchange_first_last tuple result incorrect'

assert every_other_removed(a_string) == 'abcdefgh', 'every_other_removed string result incorrect'
assert every_other_removed(a_tuple) == (1, 3, 5, 7, 9, 11, 13, 15), 'every_other_removed tuple result incorrect'

assert first4_last4_removed(a_string) == 'cdef', 'first4_last4_removed a_string result incorrect'
assert first4_last4_removed(a_tuple) == (5, 7, 9, 11), 'first4_last4_removed a_tuple result incorrect'

assert reversed(a_string) == 'hhggffeeddccbbaa', 'reversed a_string result incorrect'
assert reversed(a_tuple) == (16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1), 'reversed a_tuple result incorrect'

assert thirds(a_string) == 'fgghhaabbccddeef', 'thirds a_string result incorrect'
assert thirds(a_tuple) == (12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), 'thirds a_tuple result incorrect'
