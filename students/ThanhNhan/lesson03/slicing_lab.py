#!/usr/bin/env python

def exchange_first_last (seq):
    # If sequence length is one return seq
    if len(seq) == 1:
        print (seq)
        return seq
    else:
        seq = seq[-1:] + seq[1:-1] + seq[:1]
        print (seq)
        return seq


def remove_every_o_items (seq):
    #a copy of the original sequence and remove every step 2
    print (seq[::2])
    return seq[::2]

def remove_f4_l4 (seq):
    #start from 4 and end from 4
    print (seq[4:-4])
    return seq[4:-4]

def reverse_elements(seq):
    #a copy of the original sequence and reverse (-1)
    print (seq[::-1])
    return seq[::-1]

def last3_first3_middle3(seq):
    #define by length of each sequence divide to 3
    print(seq)
    e_third = len(seq) // 3
    print (seq[-e_third:] + seq[:-e_third])
    return (seq[-e_third:] + seq[:-e_third])


if __name__ == "__main__":
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_list = [2, 54, 13, 12, 5, 32]

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_list) == [32, 54, 13, 12, 5, 2]

    assert remove_every_o_items(a_string) == "ti sasrn"
    assert remove_every_o_items(a_tuple) == (2, 13, 5)
    assert remove_every_o_items(a_list) == [2, 13, 5]

    a_string = "this is a interest string"
    a_tuple = (2, 54, 13, 12, 5, 32, 12, 23, 3, 23, 1)
    a_list = [2, 54, 13, 12, 5, 32, 12, 23, 3, 23, 1]
    
    assert remove_f4_l4(a_string) == " is a interest st"
    assert remove_f4_l4(a_tuple) == (5, 32, 12)
    assert remove_f4_l4(a_list) == [5, 32, 12]

    assert reverse_elements(a_string) == "gnirts tseretni a si siht"
    assert reverse_elements(a_tuple) == (1, 23, 3, 23, 12, 32, 5, 12, 13, 54, 2)
    assert reverse_elements(a_list) == [1, 23, 3, 23, 12, 32, 5, 12, 13, 54, 2]

    assert last3_first3_middle3(a_string) == "t stringthis is a interes"
    assert last3_first3_middle3(a_tuple) == (3, 23, 1, 2, 54, 13, 12, 5, 32, 12, 23)
    assert last3_first3_middle3(a_list) == [3, 23, 1, 2, 54, 13, 12, 5, 32, 12, 23]

    print("complete test")