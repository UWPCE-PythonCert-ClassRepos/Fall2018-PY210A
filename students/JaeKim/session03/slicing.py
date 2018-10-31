def exchange_first_last(seq):
    '''
    first_letter = seq[0:1]
    last_letter = seq[-1]

    everything = last_letter + seq[1:-1] + first_letter
    '''
    if isinstance(seq, str):
        first = seq[0:1]
        last = seq[-1]
        content = seq[1:-1]

        joined = last + ''.join(content) + first
    else:
        print("executing INT code")

        lst = list(seq)
        lst[0] = seq[-1]
        lst[-1] = seq[0]

        t = tuple(lst)

        joined = t

    return joined

def every_other_item(seq):
    return seq[::2]


def first_last_four(seq):
    seq = seq[4:-4]
    return seq[::2]


def reversed(seq):
    return seq[::-1]


def reversed_thirds(seq):

    third = (len(seq) // 3)

    first_third = seq[0:third]
    middle_third = seq[third:third*2]
    last_third = seq[third*2::]

    return '{}{}{}'.format(last_third, first_third, middle_third)

a_string = "one two tre"
a_string2 = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

print(exchange_first_last(a_string2))
print(every_other_item(a_string2))
print(first_last_four(a_string2))
print(reversed(a_string2))
print(reversed_thirds(a_string2))

assert exchange_first_last(a_string) == "ene two tro"
assert every_other_item(a_string) == "oetote"
assert first_last_four(a_string) == "to"
assert reversed(a_string) == "ert owt eno"
assert reversed_thirds(a_string) == "o treone tw"
