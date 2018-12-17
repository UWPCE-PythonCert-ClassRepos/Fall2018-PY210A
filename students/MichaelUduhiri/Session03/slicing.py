def first_last_exchange(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]
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
    str_length = len(seq)//3
    first = seq[:str_length]
    second = seq[str_length:2 * (str_length)]
    third = seq[-str_length:]
    return third + first + second
print(last3_first3_middle3("aaabbbccc"))

assert last3_first3_middle3("aaabbbccc") == "cccaaabbb"
