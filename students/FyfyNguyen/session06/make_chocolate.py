#!/usr/bin/env python3

"""
We want make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5 kilos each).

Return the number of small bars to use,
assuming we always use big bars before small bars.
Return -1 if it can't be done.
"""


def make_chocolate(small, big, goal):
    big_fit = goal // 5
    big_in_box = min(big, big_fit)

    in_box = big_in_box * 5
    space_left = goal - in_box

    if small < space_left:
        return -1
    else:
        return space_left
