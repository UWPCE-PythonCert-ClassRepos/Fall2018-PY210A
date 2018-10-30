#!/usr/bin/env python3

"""Creates usable file name based on input of a tupleself.

param1(tuple): 4 elements. 1st is file number, last 3 are unknown.

Returns string of wanted file name
"""

def fname(tup):
#( 2, 123.4567, 10000, 12345.67)
    fname = "file_{0:0=3d} :   {4d}".format(tup[0], tup[1])
    print(fname)


if __name__ == "__main__":
    input = (2, 123.4567, 10000, 12345.67)
    fname(input)
