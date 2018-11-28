#!/usr/env/bin python3

# Excercise 3 Slicing Lab

# Exchange first and last items
def exchange_first_last(seq):
	return (seq[-1:] + seq[1:-1] + seq[:1])

# Every other item removed startin with the first item
def delete_every_other_item(seq):
	return seq[::2]

# Delete every other item starting with second item
def delete_every_other_item2(seq):
	return seq[1::2]
	
# First 4 and Last 4 removed using just slicing
def remove_first_last(seq):
	return seq[4:-4]

# Elements reversed with just slicing
def reverse(seq):
	return seq[::-1]

# Slicing in thirds
def slice_seq_thirds(seq):
	len_seq = len(seq)
    len_split= (len_seq // 3)
	"""Had to look some things up for this one. A little more challenging"""
    return "{} {} {}".format(seq[(len_split * 2)::], seq[0:len_split], seq[len_split:(len_split*2)])



# Main function
if __name__=="__main__":
# My sequences
a_string = "Are the Seahawks good this year"
a_tuple = (2, 54, 13, 12, 5, 32, 7)

# Call fist last function
exchange_first_last(a_string)
exchange_first_last(a_tuple)
# Call every other item function
delete_every_other_item(a_string)
delete_every_other_item(a_tuple)
# Call first 4 and last 4 removed function
remove_first_last(a_string)
remove_first_last(a_tuple)
# Call elements reversed function 
reverse(a_string)
reverse(a_tuple)
# Call thirds function
slice_seq_thirds(a_string)
slice_seq_thirds(a_tuple)

# Use Assertions to check validity of function output
assert exchange_first_last(a_string) == "rre the Seahawks good this yeaA"
assert exchange_first_last(a_tuple) == (43, 54, 13, 12, 5, 32, 7, 2)

assert delete_every_other_item(a_string) == AeteSaak odti er
assert delete_every_other_item(a_tuple) == (2, 13, 5, 7)

assert remove_first_last(a_string) == "the Seahawks good this "
assert remvove_first_last(a_tuple) == ()

assert reverse(a_string) == "raey siht doog skwahaeS eht erA"
assert revers(a_tuple) == (7, 32, 5, 12, 13, 54, 2)

assert slice_seq_thirds(a_string) == d this year Are the Se ahawks goo
assert slice_seq_thirds(a_tuple) == (5, 32, 7) (2, 54) (13, 12)

