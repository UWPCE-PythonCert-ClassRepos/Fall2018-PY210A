#!/usr/bin/env python3

"""
This module experiments with slicing of sequences.

def exchange_first_last is with the first and last items exchanged.
def remove_every_other is with every other item removed.
def remove_out_4_skip_mid is with the first 4 and the last 4 items removed,
    and then every other item in the remaining sequence.
def rev is with the elements reversed (just with slicing).
def third is with the last third, then first third, then the middle third in the new order.
"""

def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other(seq):
    return seq[::2]

def remove_out_4_skip_mid(seq):
    if len(seq) < 8:
        return "Length Error"
    else:
        return seq[4:-4:2]

def rev(seq):
    return seq[::-1]

def third(seq):
    """Returns last third, then 1st and 2nd third of squence.
        Returns None if sequence length is not a multiple of 3
    """

    if len(seq) % 3:
        print("Sequence is length: {}".format(len(seq)))
        return None
    else:
        thrd = int(len(seq)/3)*-1
    return seq[thrd:] + seq[:thrd]

if __name__ == "__main__":

    a_string = "This is a string"
    a_string15 = "This is a strin"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_long_tuple = (2, 5, 7, 9, 11, 15, 55, 98, 1, 70, 44, 21, 95)
    a_tuple_12 = (2, 5, 7, 9, 11, 15, 55, 98, 1, 70, 44, 21)

    assert exchange_first_last(a_string) == "ghis is a strinT"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert remove_every_other(a_string) == "Ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    assert remove_out_4_skip_mid(a_string) == " sas" #returns "Length Error" if seq is too short
    assert remove_out_4_skip_mid(a_tuple) == ("Length Error")
    assert remove_out_4_skip_mid(a_long_tuple) == (11, 55, 1)
    assert rev(a_string) == "gnirts a si sihT"
    assert rev(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert third(a_string) == None #prints length of sequence
    assert third(a_string15) == "strinThis is a "
    assert third(a_tuple) == (5, 32, 2, 54, 13, 12)
    assert third(a_tuple_12) == (1, 70, 44, 21, 2, 5, 7, 9, 11, 15, 55, 98)
