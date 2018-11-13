"""

This exercise covers the basics of slicing sequences using Python.

Exercises include: 
1) return first and last item swapped in sequence
2) return every other item in sequence
3) return sequence with first 4 and last 4 items remove plus every other item in remaining section
4) return reversed sequence
5) return sequence with last third, then first third, then middle third

"""


def first_last(seq):
	return seq[-1:] + seq[1:-1] + seq[:1]


def every_other(seq):
	return seq[::2]


def remove_first_last_four(seq):
	if len(seq) < 8:
		return "Error"
	else:
		return seq[4:-4:2]


def reverse_sequence(seq):
	return seq[::-1]


def thirds(seq):
    l = int(len(seq)/3)
    new_seq = seq[l*2:] + seq[:l] + seq[l:l*2]
    return(new_seq)




# Write tests for each of the functions above
if __name__ == "__main__":
    a_string = "this is a string"
    a_tuple = (3, 45, 11, 19, 50, 23)
    a_array = [1, 2, 3, 4, 5]

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (3, 45, 11, 19, 50, 23)
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