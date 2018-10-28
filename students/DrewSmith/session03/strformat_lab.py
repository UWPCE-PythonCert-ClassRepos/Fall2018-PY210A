#!/usr/bin python3

def task_one(tup):
    return "file_{:0>3d} :   {:.2f}, {:.2e}, {:.2e}".format(*tup)

def task_two(tup):
    return f"file_{tup[0]:0>3d} :   {tup[1]:.2f}, {tup[2]:.2e}, {tup[3]:.2e}"

def task_three(tup):
    format_list = [r"{:d}"] * len(tup)
    format_string = f"the {len(tup)} numbers are: {', '.join(format_list)}"
    return format_string.format(*tup)

def task_four(tup):
    return "{3:0>2d} {4:d} {2:d} {0:0>2d} {1:d}".format(*tup)

def task_five(values):
    return f"The weight of an {values[0][0:-1]} is {values[1]} and the weight of a {values[2][0:-1]} is {values[3]}"

def task_five_upper_20(values):
    return f"The weight of an {values[0][0:-1].upper()} is {values[1] * 1.2} and the weight of a {values[2][0:-1].upper()} is {values[3] * 1.2}"

def task_six():
    records = [("John B", 35, 23.99),
        ("Samantha A", 29, 432.13),
        ("Tom C", 53, 1284.15)]
    
    print("{:<12}{:>3}{:>9}".format("Name", "Age", "Price"))
    for record in records:
        print("{:<12}{:>3}{:>9}".format(*record))

def task_six_bonus(tup):    
    print(("{:>5}" * len(tup)).format(*tup))

if __name__ == "__main__":
    assert task_one((2, 123.4567, 10000, 12345.67)) == "file_002 :   123.46, 1.00e+04, 1.23e+04"
    assert task_two((2, 123.4567, 10000, 12345.67)) == "file_002 :   123.46, 1.00e+04, 1.23e+04"
    assert task_three((1,2,3,4)) == "the 4 numbers are: 1, 2, 3, 4"
    assert task_four((4, 30, 2017, 2, 27)) == '02 27 2017 04 30'
    assert task_five(['oranges', 1.3, 'lemons', 1.1]) == "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
    assert task_five_upper_20(['oranges', 1.3, 'lemons', 1.1]) == "The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32"
    task_six()
    print()
    task_six_bonus((1,2,3,4,5,6,7,8,9,0))