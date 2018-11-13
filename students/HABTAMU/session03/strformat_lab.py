#!/usr/bin/env python3

# Task 1:
str = r" file_{:0>3d} {:.2f} {:.2e} {:.2e}?".format(2, 123.4567, 10000, 12345.67)
print(str)

# Task 2:
pos = (2, 123.4567, 10000, 12345.67)
str = f" file_{pos[0]:0>3d}:  {pos[1]:.2f} {pos[2]:.2e} {pos[3]:.2e}".format(pos=pos)
print(str)

# Task 3:
def formatter(str):
    lst = [r"{:d}"] * len(str)
    a_str = f"the {len(str)} numbers are: {', '.join(lst)}"
    return a_str.format(*str)
formatter((1, 2, 3, 4))

# Task 4:
print("{3:0>2d} {4:d} {2:d} {0:0>2d} {1:d}".format(4, 30, 2017, 2, 27))

# Task 5:
