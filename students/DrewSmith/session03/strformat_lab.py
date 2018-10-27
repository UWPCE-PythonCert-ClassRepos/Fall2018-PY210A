#!/usr/bin python3

def task_one(tup):
    return "file_{:0>3d} :   {:.2f}, {:.2e}, {:.2e}".format(*tup)

def task_two(tup):
    return f"file_{tup[0]:0>3d} :   {tup[1]:.2f}, {tup[2]:.2e}, {tup[3]:.2e}"

def task_three(tup):
    format_list = [r"{:d}"] * len(tup)
    format_string = f"the {len(tup)} numbers are: {', '.join(format_list)}"
    return format_string.format(*tup)


if __name__ == "__main__":
    assert task_one((2, 123.4567, 10000, 12345.67)) == "file_002 :   123.46, 1.00e+04, 1.23e+04"
    assert task_two((2, 123.4567, 10000, 12345.67)) == "file_002 :   123.46, 1.00e+04, 1.23e+04"
    assert task_three((1,2,3,4)) == "the 4 numbers are: 1, 2, 3, 4"