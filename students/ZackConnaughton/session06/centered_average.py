"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
"""

import math

def centered_average(data_list):
    print(max(data_list))
    print(min(data_list))
    total = math.fsum(data_list) - max(data_list) - min(data_list)
    count = len(data_list) - 2
    return total//count
