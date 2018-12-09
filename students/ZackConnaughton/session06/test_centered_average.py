"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
"""

from centered_average import centered_average

def test0():
    assert centered_average([1, 2, 3, 4, 100]) == 3
def test1():
    assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5
def test2():
    assert centered_average([-10, -4, -2, -4, -2, 0]) == -3
def test3():
    assert centered_average([5, 3, 4, 6, 2]) == 4
def test4():
    assert centered_average([5, 3, 4, 0, 100]) == 4
def test5():
    assert centered_average([100, 0, 5, 3, 4]) == 4
def test6():
    assert centered_average([4, 0, 100]) == 4
def test7():
    assert centered_average([0, 2, 3, 4, 100]) == 3
def test8():
    assert centered_average([1, 1, 100]) == 1
def test9():
    assert centered_average([7, 7, 7]) == 7
def test10():
    assert centered_average([1, 7, 8]) == 7
def test11():
    assert centered_average([1, 1, 99, 99]) == 50
def test12():
    assert centered_average([1000, 0, 1, 99]) == 50
