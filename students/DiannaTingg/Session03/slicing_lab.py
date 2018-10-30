# Lesson 03 Exercise: Slicing Lab


def format_seq(seq, new_seq):
    """
    Format new sequence so it matches the type of the original sequence.
    """
    if type(seq) == str:
        return "".join(new_seq)
    elif type(seq) == tuple:
        return tuple(new_seq)
    else:
        return new_seq


def exchange_first_last(seq):
    """
    Return sequence with first and last items exchanged.
    """
    # Create new list and set it to the last element of the original sequence
    new_seq = [seq[-1]]

    # Add the middle elements from the original sequence
    new_seq.extend(seq[1:-1])

    # Add the first element from the original sequence
    new_seq.append(seq[0])

    # Run new sequence through formatting function
    return format_seq(seq, new_seq)


def remove_every_other(seq):
    """
    Return sequence with every other item removed.
    """
    # Make a copy of the original sequence and step by 2
    new_seq = seq[::2]

    return new_seq


def remove_four_and_every_other(seq):
    """
    Return sequence with the first four and last four items removed, plus every other item in the remaining sequence.
    """
    # Make a copy of the original sequence, but omit the first four and last four elements
    new_seq = seq[4:-4]

    # Make a copy of new sequence and step by 2
    new_seq = new_seq[::2]

    return new_seq


def reverse_elements(seq):
    """
    Return a sequence with the elements reversed (just with slicing).
    """

    new_seq = []

    i = -1

    while i >= -len(seq):
        new_seq.append(seq[i])
        i -= 1

    return format_seq(seq, new_seq)


def last_first_middle_third(seq):
    """
    Return a sequence with the last third, then first third, then middle third in the new order.
    """
    # Using the length of the sequence, figure out roughly what one third should be
    one_third = len(seq) // 3

    new_seq = list(seq[-one_third:])
    new_seq.extend(seq[:-one_third])
    return format_seq(seq, new_seq)


# Write tests for each of the functions above
if __name__ == "__main__":
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_array = [1, 2, 3, 4, 5]

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_array) == [5, 2, 3, 4, 1]

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    assert remove_every_other(a_array) == [1, 3, 5]

    long_string = "abcdefghijklmn"
    long_tuple = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22)
    long_array = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

    assert remove_four_and_every_other(long_string) == "egi"
    assert remove_four_and_every_other(long_tuple) == (10, 14)
    assert remove_four_and_every_other(long_array) == [20, 30, 40]

    assert reverse_elements(long_string) == "nmlkjihgfedcba"
    assert reverse_elements(long_tuple) == (22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2)
    assert reverse_elements(long_array) == [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]

    test_string = "ABCDEFGHIJKL"
    test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    assert last_first_middle_third(test_string) == "IJKLABCDEFGH"
    assert last_first_middle_third(test_tuple) == (9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8)
    assert last_first_middle_third(test_array) == [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8]

    print("Tests passed!")
