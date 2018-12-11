#function to take a sequence as an arg, return a copy of that sequence:

#...with the first and last items exchanged:
def exchange_first_last(seq):
    new_seq = seq[-1:] + seq[1:-1] + seq[:1]
    return new_seq

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)    


#...with every other item removed:
def remove_items(seq):
    return seq[0::2]

assert remove_items(a_tuple) == (2, 13, 5)


#...the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def four_items(seq):
    return seq[4:-4:2]

assert four_items(a_string) == (" sas")


#...with the elements reversed (just with slicing).
def reverse(seq):
    return seq[::-1]

assert reverse(a_string) == "gnirts a si siht"


#...with the last third, then first third, then the middle third in the new order.
def thirds(seq):
    third = len(seq) // 3
    seq_thirds = seq[-third:] + seq[0:third] + seq[third:-third]
    return seq_thirds

test_thirds = "firsthellothird"
assert thirds(test_thirds) == "thirdfirsthello"
    
