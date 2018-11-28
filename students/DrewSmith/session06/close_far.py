#!/usr/bin/env python

"""
Given three ints, a b c, return True if one of b or c is "close"
(differing from a by at most 1), while the other is "far", 
differing from both other values by 2 or more. Note: abs(num) 
computes the absolute value of a number.
"""


def close_far(a, b, c):
    if abs(b - c) < 2:
        return False
    ab = abs(a - b)
    ac = abs(a - c)    
    return (ab <= 1 and ac >= 2) or (ac <= 1 and ab >= 2)

        
