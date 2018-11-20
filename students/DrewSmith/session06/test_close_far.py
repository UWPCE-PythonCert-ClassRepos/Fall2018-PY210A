#!/usr/bin/env python

"""
Given three ints, a b c, return True if one of b or c is "close"
(differing from a by at most 1), while the other is "far", 
differing from both other values by 2 or more. Note: abs(num) 
computes the absolute value of a number.
"""

from close_far import close_far

def test_1():
    assert close_far(1, 2, 10) is True


def test_2():    
    assert close_far(1, 2, 3) is False	


def test_3():
    assert close_far(4, 1, 3) is True


def test_4():
    assert close_far(4, 5, 3) is False	


def test_5():
    assert close_far(4, 3, 5) is False	


def test_6():
    assert close_far(-1, 10, 0) is True


def test_7():
    assert close_far(0, -1, 10) is True


def test_8():
    assert close_far(10, 10, 8) is True	


def test_9():
    assert close_far(10, 8, 9) is False	


def test_10():
    assert close_far(8, 9, 10) is False	


def test_11():
    assert close_far(8, 9, 7) is False	


def test_12():
    assert close_far(8, 6, 9) is True