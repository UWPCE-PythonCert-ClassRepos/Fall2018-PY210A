def first_last_exchange(seq):
    list_string = list(seq)
    list_string[0], list_string[-1] = list_string[-1], list_string[0]
    return "".join(list_string)
print(first_last_exchange("This is a string"))


def every_other_removed(seq):
    return seq[0:20:2]
print(every_other_removed("This is a string"))


def first_four_last_four(seq):
    return seq[4:-4:2]
print(first_four_last_four("This is a string"))


def reverse_string(seq):
    return seq[::-1]
print(reverse_string("This is a string"))


def last3_first3_middle3(seq):
    seq
