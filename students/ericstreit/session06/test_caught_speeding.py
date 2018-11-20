#!/usr/bin/env python

"""

You are driving a little too fast, and a police officer stops you.
Write code to compute the result, encoded as an int value:

0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0.

If speed is between 61 and 80 inclusive, the result is 1.
If speed is 81 or more, the result is 2.

Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

"""


# you can change this import to test different versions
from caught_speeding import caught_speeding
# from cigar_party import cigar_party2 as cigar_party
# from cigar_party import cigar_party3 as cigar_party


def test_1():
    assert caught_speeding(60, False) == 0


def test_2():
    assert caught_speeding(65, False) == 1


def test_3():
    assert caught_speeding(65, True) == 0


def test_4():
    assert caught_speeding(81, False) == 2

def test_5():
    assert caught_speeding(81, True) == 1
