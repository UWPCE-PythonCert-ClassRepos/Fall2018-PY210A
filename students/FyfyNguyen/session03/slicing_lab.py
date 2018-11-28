#!/usr/bin/env python3

"""
Write some functions that take a sequence as an argument,
and return a copy of that sequence:
"""


# with the first and last items exchanged
def exchange_first_last(seq):
    n = len(seq)
    if n < 2:
        return seq[:]
    first = seq[0:1]
    last = seq[n-1:n]
    mid = seq[1:-1]
    return last + mid + first


# with every other item removed
def remove_every_other(seq):
    return seq[::2]


# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence
def four_removed(seq):
    return seq[4:-4:2]


# with the elements reversed (just with slicing)
def reversed(seq):
    return seq[::-1]


# with the third, then first third, then the middle third in the new order
def switch_thirds(seq):
    if len(seq) < 3:
        return seq[:]
    third = len(seq) // 3
    return seq[-third:] + seq[:third] + seq[third:-third]
