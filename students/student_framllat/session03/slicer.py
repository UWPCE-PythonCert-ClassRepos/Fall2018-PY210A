#!/usr/bin/env python3

def exch_first_last(n):

    """ This will swap first/last element in sequence
    """

    a = list(n)
    a[0], a[-1] = a[-1], a[0]
    if type(a[0]) is str:
        return ''.join(a)
    elif type(a[0]) is int:
        return a
    else:
        return None

def rm_every_oth(n):

    """ This will remove every other element in sequence
    """

    a = list(n)
    del a[1::2]
    if type(a[0]) is str:
        return ''.join(a)
    elif type(a[0]) is int:
        return a

def four_rm_four(n):

    """ This function will remove first 4 elements and last 4 elements
        then will remove every other remaining element
    """

    a = list(n)
    if type(a[0]) is str:
        tmp = a[4:-4]
        return ''.join(tmp[1::2])
    elif type(a[0]) is int:
        tmp = a[4:-4]
        return tmp[1::2]

def reverse(n):

    """ This function will reverse the sequence
    """
    return n[::-1]

def thirds(n):
    last = n[len(n)//3*2:len(n)]
    middle = n[len(n)//3:len(n)//3*2]
    first = n[:len(n)//3]
    return last+first+middle

my_string = "To whom it may concern it is nominal"
#my_string = "ssssybpnmlwqtttt"
my_tuple = (12, 33, 19, 66, 101, 9, 88, 102, 33, 119, 200, 0, 32, 4)

out_str = exch_first_last(my_string)
out_tup = exch_first_last(my_tuple)

out_rem_str = rm_every_oth(my_string)
out_rem_tup = rm_every_oth(my_tuple)

out_four_str = four_rm_four(my_string)
out_four_tup = four_rm_four(my_tuple)

out_reverse_str = reverse(my_string)
out_reverse_tup = reverse(my_tuple)


out_thirds_str = thirds(my_string)
out_thirds_tup = thirds(my_tuple)

print(out_str)
print(out_tup)
print(out_rem_str)
print(out_rem_tup)
print(out_four_str)
print(out_four_tup)
print(out_reverse_str)
print(out_reverse_tup)
print(out_thirds_str)
print(out_thirds_tup)
