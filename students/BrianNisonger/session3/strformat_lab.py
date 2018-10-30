def task_one(seq):
    """
    Format strings w/ .format
    """
    return ("File_{:0>3d}".format(seq[0]),"{:.2f}".format(seq[1]),"{:.2E}".format(seq[2]),"{:.3G}".format(seq[3]))

def task_two(seq):
    """
    Format strings w/ fstring
    """
    return (f'File_{seq[0]:0>3d}',f'{seq[1]:.2f}',f'{seq[2]:.2E}',f'{seq[3]:.3G}')

def formatter(seq):
    """
    Variable length format strings
    """
    format_string=""
    for number in (seq):
        format_string+="{:d},"
    format_string="the {} numbers are:".format(len(seq))+format_string[0:len(format_string)-1]
    return format_string.format(*seq)
    
def task_four(seq):
    """
    Rearrange tuple using fstrings
    """  
    str_out=f'{seq[3]:0>2d} {seq[4]} {seq[2]} {seq[0]:0>2d} {seq[1]}'
    print(str_out)

def task_five(seq):
    """
    Using fstrings specifically
    """
    str_orange=seq[0]
    str_lemon=seq[2]
    str_orange=str_orange[0:len(str_orange)-1]
    str_lemon=str_lemon[0:len(str_lemon)-1]
    string_out=f'The weight of an {str_orange} is {seq[1]} and the weight of a {str_lemon} is {seq[3]}'
    string_out_bonus=f'The weight of an {str_orange.upper()} is {seq[1]*1.2} and the weight of a {str_lemon.upper()} is {seq[3]*1.2}'
    return string_out
    
def task_six(seq):
    """
    Align info in a grid
    """
        for item in alignment_tuple:
            print(f'{item[0]:<3} {item[1]:<15} {item[2]:<7}')
  
if __name__ == "__main__":
    seq=( 2, 123.4567, 10000, 12345.67)
    format_seq=( 2,3,5,6,7,8)
    test_seq=( 4, 30, 2017, 2, 27)
    test_list=['oranges', 1.3, 'lemons', 1.1]
    alignment_tuple=([42,"Brian",100.09],[55,"Jack",1000.19],[125,"Bob",9.99])
    assert task_one(seq) == ('File_002', '123.46', '1.00E+04', '1.23E+04')
    assert task_two(seq) == ('File_002', '123.46', '1.00E+04', '1.23E+04')
    assert formatter(format_seq) == "the 6 numbers are:2,3,5,6,7,8"
    task_four(test_seq)
    assert task_five(test_list) == "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
    task_six(alignment_tuple)
    print("tests passed")
    