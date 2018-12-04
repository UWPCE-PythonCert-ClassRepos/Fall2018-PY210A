
def exchange_first_last(seq):

    '''with the first and last items exchanged.'''

    new_sequence = seq[-1:]+seq[1:-1]+seq[:1]

    return new_sequence


def remove_every_other(seq):

    '''with every other item removed'''

    seq = seq[::2]
    return seq

def remove_FL_four_every_other(seq):

    '''with the first 4 and the last 4 items removed, and then every other item.'''

    new_seq = seq[4:-4]
    new_seq = new_seq[::2]
    return new_seq

def reversed_sequence(seq):

    '''with the elements reversed (just with slicing).'''

    seq = seq[::-1]
    return seq

def LMF_third_sequence(seq):

    new_sequence = reversed_sequence(seq[-3:])+reversed_sequence(seq[:3])+reversed_sequence(seq[3:6])
    return new_sequence


if __name__ == '__main__':

    a_string = 'this is a string'
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_longer_tuple = (2, 54, 13, 12, 5, 32, 16, 19, 43, 65, 78)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)

    assert remove_FL_four_every_other(a_string) == " sas"
    assert remove_FL_four_every_other(a_longer_tuple) == (5, 16)

    assert reversed_sequence(a_string) == "gnirts a si siht"
    assert reversed_sequence(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert LMF_third_sequence(a_string) == "gniihti s"
    assert LMF_third_sequence(a_longer_tuple) == (78, 65, 43, 13, 54, 2, 32, 5, 12)


    print("All tests passed")

