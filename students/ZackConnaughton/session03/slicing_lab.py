

def exchange_first_last(seq):
    """
    Sequence entry returns a copy of the sequence with the first and last items
    swapped
    """
    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other(seq):
    """
    Sequence entry returns a copy of the sequence with every other item removed
    """
    return seq[0:len(seq):2]

def remove_first_and_last(seq, num=4):
    """
    Sequence entry returns a copy of the sequence with a number of items
    removed from the start and the end. Returns every other item in the
    remaining.
    num - The number of items to remove, default is 4
    """
    return remove_every_other(seq[num:-num])


def sequence_reverse(seq):
    """
    Sequence entry returns a copy of the sequence with the items in reversere
    order from the entry
    """
    return seq[::-1]

def last_third_first(seq):
    """
    Sequence entry returns a copy of the sequence with the last third first,
    then first third then middle third in order
    """
    return seq[-len(seq)//3:] + seq[:-len(seq)//3]

if __name__ == '__main__':
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_longer_tuple = (1, 15, 23, 55, 80, 17, 4, 33, 12, 10, 100, 9)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)

    assert remove_first_and_last(a_string) == " sas"
    assert remove_first_and_last(a_longer_tuple) == (80, 4)
    assert remove_first_and_last(a_tuple, 2) == (13,)

    assert sequence_reverse(a_string) == "gnirts a si siht"
    assert sequence_reverse(a_tuple) == (32,5,12,13,54,2)

    assert last_third_first(a_string) == "stringthis is a "
    assert last_third_first(a_tuple) == (5, 32, 2, 54, 13, 12)
    print("We did it!")
