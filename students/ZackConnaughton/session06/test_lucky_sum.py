#!/usr/bin/env python

"""
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
"""

from lucky_sum import lucky_sum_function

def test1():
    assert lucky_sum_function(1, 2, 3) == 6
def test2():
    assert lucky_sum_function(1, 2, 13) == 3
def test3():
    assert lucky_sum_function(1, 13, 3) == 1
def test4():
    assert lucky_sum_function(1, 13, 13) == 1
def test5():
    assert lucky_sum_function(6, 5, 2) == 13
def test6():
    assert lucky_sum_function(13, 2, 3) == 0
def test7():
    assert lucky_sum_function(13, 2, 13) == 0
def test8():
    assert lucky_sum_function(13, 13, 2) == 0
def test9():
    assert lucky_sum_function(9, 4, 13) == 13
def test10():
    assert lucky_sum_function(8, 13, 2) == 8
def test11():
    assert lucky_sum_function(7, 2, 1) == 10
def test12():
    assert lucky_sum_function(3, 3, 13) == 6
