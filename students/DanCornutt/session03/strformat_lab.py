#!/usr/bin/env python3

"""Creates usable file name based on input of a tupleself.

param1(tuple): 4 elements. 1st is file number, last 3 are unknown.

Returns string of wanted file name
"""

def fname_tsk1(tup): #Task 1 & 2
    fname1 = f"file_{str(tup[0]).zfill(3):}:   {tup[1]:.2f}, {tup[2]:.2e}, {tup[3]:.2e}"
    return(fname1)


def fname_tsk3(tup):
    t_size = str(len(tup))
    fname3 = "The " + t_size + " numbers are: "
    for t in tup:
        fname3 = fname3 + "{:d}, "
    return fname3[:-2].format(*tup)


def fname_tsk4(tup):
    form_string = "{3:02d} {4:d} {2:d} {0:02d} {1:d}"
    return form_string.format(*tup)

def del_lst(item):
    return item[:-1]

def fname_tsk5(lst):
    lst[0] = del_lst(lst[0])
    lst[2] = del_lst(lst[2])
    body = "The weight of an {0} is {1} and the weight of a " \
    "{2} is {3}"
    return body.format(*lst)


def fname_tsk6(tup):
    pass

    
if __name__ == "__main__":
    #Task 1 &2
    input1 = (2, 123.4567, 10000, 12345.67)
    input2 = (111, 12.999, 2, 13444343.6)
    #Task 3
    input3 = (1,2,3)
    input4 = (3,2,1,0)
    #Task 4
    input5 = ( 4, 30, 2017, 2, 27)
    input6 = ['oranges', 1.3, 'lemons', 1.1]

#Tests
    fname_tsk6

    assert fname_tsk1(input1) == "file_002:   123.46, 1.00e+04, 1.23e+04"
    assert fname_tsk1(input2) == "file_111:   13.00, 2.00e+00, 1.34e+07"
    assert fname_tsk3(input3) == "The 3 numbers are: 1, 2, 3"
    assert fname_tsk3(input4) == "The 4 numbers are: 3, 2, 1, 0"
    assert fname_tsk4(input5) == ("02 27 2017 04 30")
    assert fname_tsk5(input6) == ("The weight of an orange is 1.3 and "\
        "the weight of a lemon is 1.1")

    print("All tests passed! yay :)")
