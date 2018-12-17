#!/usr/bin/env python3

"""
We want make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5 kilos each).

Return the number of small bars to use,
assuming we always use big bars before small bars.
Return -1 if it can't be done.
"""

from make_chocolate import make_chocolate


def test_1():
    assert make_chocolate(4, 1, 9) == 4


def test_2():
    assert make_chocolate(4, 1, 10) == -1


def test_3():
    assert make_chocolate(4, 1, 7) == 2


def test_4():
    assert make_chocolate(6, 2, 7) == 2


def test_5():
    assert make_chocolate(4, 1, 5) == 0


def test_6():
    assert make_chocolate(6, 1, 10) == 5


def test_7():
    assert make_chocolate(6, 1, 11) == 6


def test_8():
    assert make_chocolate(6, 1, 13) == -1


def test_9():
    assert make_chocolate(60, 100, 550) == 50


def test_10():
    assert make_chocolate(1000, 1000000, 5000006) == 6
