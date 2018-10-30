#!/usr/bin/env python3

"""File experiments with string formatting
"""

def fname_tsk1(tup): #Task 1 & 2
    """Creates usable file name based on input of a tupleself.
    param1(tuple): 4 elements. 1st is file number, last 3 are unknown.
    Returns string of wanted file name
    """
    fname1 = f"file_{str(tup[0]).zfill(3):}:   {tup[1]:.2f}, {tup[2]:.2e}, {tup[3]:.2e}"
    return(fname1)


def fname_tsk3(tup):
    """Creates usable file name based on input of a tupleself.
    param1(tuple): 4 elements. 1st is file number, last 3 are unknown.
    Returns string of wanted file name
    """
    t_size = str(len(tup))
    fname3 = "The " + t_size + " numbers are: "
    for t in tup:
        fname3 = fname3 + "{:d}, "
    return fname3[:-2].format(*tup)


def fname_tsk4(tup):
    """Rearranges tuple based on workstatement.
    param1(tuple): 4 elements
    Returns tuple of text order and format
    """
    form_string = "{3:02d} {4:d} {2:d} {0:02d} {1:d}"
    return form_string.format(*tup)


def del_lst(item):
    return item[:-1]


def fname_tsk5(lst):
    """Creates sting of fruits and weights based on input of a list.
    param1(list): 4 elements. 1st is fruit #1 name, 2nd is fruit #1 weight
    3rd is fruit #2 name, 4th is fruit #2 weight.
    Returns string of fruits and their weight
    """
    lst[0] = del_lst(lst[0])
    lst[2] = del_lst(lst[2])
    body = "The weight of an {0} is {1} and the weight of a " \
    "{2} is {3}"
    return body.format(*lst)


def fname_tsk6(lst):
    """Creates report based on input of a list.
    param1(list): 3 elements. 1st is vehicle name, 2nd is the vehicle age,
    3rd is the current price.
    Returns string formatted report
    """
    max_name = max(len(lst[0][0]), len(lst[1][0]), len(lst[2][0]), len('Name'))
    max_year = max(len(str(lst[0][1])), len(str(lst[1][1])),
                   len(str(lst[2][1])), len('Year'))
    max_price = max(len(str(lst[0][2])), len(str(lst[1][2])),
                    len(str(lst[2][2])), len('Price'))
    length = [max_name, max_year, max_price]
    report = ("Name" + (max_name - len("Name")) * " " + "|" +
              (max_year - len("Year")) * " " + "Year" + "|" +
              (max_price - len("Price")) * " " + "Price|\n")
    for car in lst:
        new_line = "{nm:{mnm}}|{y:{my}}|{pri:{mpri}}|".format(
            nm=car[0], y=car[1], pri=car[2], mnm=length[0], my=length[1], mpri=length[2]
        )
        report += new_line + "\n"
    return report


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
    input7 = [['Volkswagen Beetle', 50, 10000], ['Daewoo Lanos', 15, 25], ['MG 14/25', 80, 250000]]

#Tests
    fname_tsk6(input7)

    assert fname_tsk1(input1) == "file_002:   123.46, 1.00e+04, 1.23e+04"
    assert fname_tsk1(input2) == "file_111:   13.00, 2.00e+00, 1.34e+07"
    assert fname_tsk3(input3) == "The 3 numbers are: 1, 2, 3"
    assert fname_tsk3(input4) == "The 4 numbers are: 3, 2, 1, 0"
    assert fname_tsk4(input5) == ("02 27 2017 04 30")
    assert fname_tsk5(input6) == ("The weight of an orange is 1.3 and "\
        "the weight of a lemon is 1.1")
    assert fname_tsk6(input7) == (
                """Name             |Year| Price|
Volkswagen Beetle|  50| 10000|
Daewoo Lanos     |  15|    25|
MG 14/25         |  80|250000|
""")

    print("All tests passed! yay :)")
