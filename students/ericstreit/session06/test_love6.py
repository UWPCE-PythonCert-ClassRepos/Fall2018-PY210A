#!/usr/bin/env python

"""

The number 6 is a truly great number.
Given two int values, a and b, return True if either one is 6.
Or if their sum or difference is 6.

Note: the function abs(num) computes the absolute value of a number.

"""


# you can change this import to test different versions
from love6 import love6
# from cigar_party import cigar_party2 as cigar_party
# from cigar_party import cigar_party3 as cigar_party


def test_1():
    assert love6(6, 4) is True

def test_2():
    assert love6(4, 5) is False

def test_3():
    assert love6(1, 5) is True

def test_4():
    assert love6(1, 7) is True

def test_5():
    assert love6(-4, -10) is True

def test_6():
    assert love6(7, 1) is True

def test_7():
    assert love6(0, 9) is False

def test_8():
    assert love6(0, 6) is True
