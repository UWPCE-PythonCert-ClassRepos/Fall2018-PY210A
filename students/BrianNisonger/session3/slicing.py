def exchange_first_last(seq):
    """
    Exchanges first and last element of a list,string,tuple
    """
    a_new_sequence=seq[-1:]+seq[1:-1]+seq[:1]
    return a_new_sequence

def remove_every_other(seq):
    """
    Removes every other element of a string,list,tuple
    """
    a_new_sequence=seq[::2]
    return a_new_sequence    
   
def first_last_everyother(seq):
    """
    Removes first 4 elements, last 4 elements, and then every other element of string,list, tuple
    """
    a_new_sequence=seq[4:(len(seq)-4)]
    a_new_sequence=remove_every_other(a_new_sequence)
    return a_new_sequence
    
def reverse_sequence(seq):
    """
    Reverse elements of a sequence
    """
    a_new_sequence=seq[::-1]
    return a_new_sequence


def reorder_thirds(seq):
    """
    Rearranges by thirds (Last,First,Middle) and reverses order of sequences
    """
    a_new_sequence=reverse_sequence(seq[-len(seq)//3:])+reverse_sequence(seq[:len(seq)//3])+reverse_sequence(seq[len(seq)//3:-len(seq)//3])
    return a_new_sequence

if __name__ == "__main__":
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_long_tuple = (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024)
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2,13,5)
    assert first_last_everyother(a_string) == " sas"
    assert first_last_everyother(a_long_tuple) == (32,)
    assert reverse_sequence(a_string) == "gnirts a si siht"
    assert reverse_sequence(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert reorder_thirds(a_string) == "gnirts siht a si"
    assert reorder_thirds(a_tuple) == (32, 5, 54, 2, 12, 13)
    assert reorder_thirds(a_long_tuple) == (1024, 512, 256, 128, 8, 4, 2, 64, 32, 16)
    print ("tests passed")