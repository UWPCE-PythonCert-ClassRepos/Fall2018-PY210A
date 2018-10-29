#!/usr/bin/env python


def file_format(number):
    """
    takes a number and returns a file format as a string file_XXX with the numbers
    """
    return 'file_' + '{:03.0f}'.format(number) + ' :   '

def three_sig_fig(number):
    """
    takes a number and returns the same number with two decimal spaces shown
    """
    return '{:.2f}'.format(number)

def scientific_notation(number):
    """
    takes a number and returns it with exponential scientific_notation
    """
    return "{:.2e}".format(number)

def task_one(file_num, two_dec, exp1, exp2):
    """
    function that performs actions to satisfy task one of session three in PY210
    """
    output_string = ""
    output_string += file_format(file_num)
    output_string += three_sig_fig(two_dec)
    output_string += ', '
    output_string += scientific_notation(exp1)
    output_string += ', '
    output_string += scientific_notation(exp2)
    return output_string


def zeros(num):
    """
    returns a number padded to the left with '0's up to a length of three_sig_fig
    """

    return "0" * (3-len(num)) + num


def r_num(num, _num):
    """
    rounds a number num with a next number _num as input
    returns a single number as a form_string
    """
    if int(_num) >= 5:
        output = str(int(num) + 1)
    else:
        output = str(num)
    return output


def task_2_decimal(num):
    """
    returns a number with two decimal places for task two of session three of PY201
    """
    decimal_index = num.find('.')
    output = num[:decimal_index + 2] + r_num(num[decimal_index + 2], num[decimal_index + 3])
    return output

def task_2_sci(num):
    """
    returns a number with explonential notation for task two of session three of PY201
    """
    decimal_index = num.find('.')
    if decimal_index == -1:
        length = len(num)
    else:
        length = decimal_index
    output_string = num[0] + "." + num[1] + r_num(num[2], num[3])
    e_value = 'e+0' + str(length - 1)
    output_string += e_value
    return output_string

def task_two(file_num, two_dec, exp1, exp2):
    """
    Function that performs the tasks requred by task two of session three PY201
    """
    num1 = two_dec
    num2 = exp1
    num3 = exp2
    return (F"file_{zeros(str(file_num))} :   {task_2_decimal(str(num1))}, {task_2_sci(str(num2))}, {task_2_sci(str(num3))}")


def task_three(*t):
    """
    Takes an arbritary number of arguments as t and returns a string that explains the quantity and lists the numbers
    """
    form_string = "{:d}, " * (len(t) -1) + "{:d}"
    output_string = F"the " + str(len(t)) + " numbers are: " + form_string
    output = output_string.format(*t)
    return output


def task_four(*t):
    """
    takes in a specific date-time format and returns a string in a month-day-year-hour-minute format with leading zeros as needed
    """
    hour = '{:02.0f}'.format(t[0])
    minute = '{:02.0f}'.format(t[1])
    year = '{:04.0f}'.format(t[2])
    month = '{:02.0f}'.format(t[3])
    day = '{:02.0f}'.format(t[4])
    return(F"{month} {day} {year} {hour} {minute}")

def task_five(l, bonus=False):
    """
    returns a string explain fruit weights as provided by an input listself.
    bonus if true returns the fruit names in all capital letters and a 20% increase to the fruit weight in the string returned.
    """
    fruit1 = l[0][:-1]
    fruit1_weight = l[1]
    fruit2 = l[2][:-1]
    fruit2_weight = l[3]

    if not bonus:
        output_string = F'The weight of an {fruit1} is {fruit1_weight} and the weight of a {fruit2} is {fruit2_weight}'
    elif bonus:
        output_string = F'The weight of an {fruit1.upper()} is {fruit1_weight * 1.2} and the weight of a {fruit2.upper()} is {fruit2_weight * 1.2}'
    return(output_string)


def longest(values):
    """
    takes a list of values and returns the length of the longest value
    """
    cur_longest = 0
    for i in values:
        if len(i) > cur_longest:
            cur_longest = len(i)
    return(cur_longest)

def task_six(l, pad=3):
    """
    takes a list of name-age-cost records and returns a printable string with the data in columns padded by the value pad
    """
    column_1 = []
    column_2 = []
    column_3 = []
    for line in l:
        column_1.append(line[0])
        column_2.append(str(line[1]))
        column_3.append(str(line[2]))
    column_widths = [longest(column_1)+pad, longest(column_2)+pad, longest(column_3)+ pad]
    #print(column_widths)

    l.insert(0, ['Name', 'Age', 'Cost'])
    output = ""
    #print(l)
    for line in l:
        output += ('{:<{width}}'.format(line[0], width=column_widths[0]) + '{:<{width}}'.format(line[1], width=column_widths[1])+ '{:>{width}}'.format(line[2], width=column_widths[2]) + '\n')
    return output


if __name__ == '__main__':
    assert task_one(2, 123.4567, 10000, 12345.76) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    assert task_two(2, 123.4567, 10000, 12345.76) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    assert task_three(1, 2, 3) == "the 3 numbers are: 1, 2, 3"
    assert task_three(5, 2, 7, 19, 14) == "the 5 numbers are: 5, 2, 7, 19, 14"

    assert task_four(4, 30, 2017, 2, 27) == '02 27 2017 04 30'
    assert task_five(['oranges', 1.3, 'lemons', 1.1]) == 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'
    assert task_five(['oranges', 1.3, 'lemons', 1.1], bonus=True) == 'The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32'

    task_six_values = [['Frankie', 22, 10000],
                       ['Sarah', 39, 100],
                       ['Billybob', 50, 10000000],
                       ['Rico', 2, 2]]
    print(task_six(task_six_values))

    print('Assserted')
