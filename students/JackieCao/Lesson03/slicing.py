
# with the first and last items exchanged

def exchange_first_last(seq):
    z = seq[-1:]
    a = seq[0:1]
    new_seq = z + seq[1:-1] + a
    return new_seq


a_string = "this is a string"
a_tuple = (2, 54, 13, 3, 15, 11, 18, 19, 22, 88, 45, 43, 12, 5, 32)

assert exchange_first_last(a_tuple) == (32, 54, 13, 3, 15, 11, 18, 19, 22, 88, 45, 43, 12, 5, 2)
assert exchange_first_last(a_string) == 'ghis is a strint'


# with every other item removed

def remove_every_other(seq):
    new_seq = seq[::2]
    return new_seq

assert remove_every_other(a_tuple) == (2, 13, 15, 18, 22, 45, 12, 32)

# with the first 4 and the last 4 items removed, 
# and then every other item in the remaining sequence

def remove_f4l4_every_other(seq):
    new_seq = seq[4:-4]
    new_seq = new_seq[::2]
    return new_seq

assert remove_f4l4_every_other(a_tuple) == (15, 18, 22, 45)

# with the elements reversed (just with slicing)

def reverse(seq):
    new_seq = seq[::-1]
    return new_seq

a_tuple = (1, 2, 3, 4, 5)
assert reverse(a_tuple) == (5, 4, 3, 2, 1)

# with the last third, then first third, then the middle third in the new order

def new_order(seq):
    l = int(len(seq)/3)
    new_seq = seq[l*2:]+seq[:l]+seq[l:l*2]
    return(new_seq)

a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
assert new_order(a_tuple) == (7, 8, 9, 1, 2, 3, 4, 5, 6)





