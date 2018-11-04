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
    list_string = list(seq)
    return seq[-3:3] + str(list_string/2)
print(last3_first3_middle3("This is a string"))
