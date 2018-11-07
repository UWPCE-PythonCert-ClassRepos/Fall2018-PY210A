#!/usr/bin/env python3

def exchange_first_last(seq):
	"""
	:param: sequence 
	:return: sequence with first and last item exchanges and all other item remain same
	"""
	if len(seq) <= 1:
		return seq
	return seq[-1:] + seq[1:-1] + seq[:1]

def other_item_removed(seq):
	"""
	:param: sequence
	:return: sequence with every other item removed
	"""
	return seq[::2]

def remove_4(seq):
	"""
	:param: sequence
	:return: sequence with the first 4 and the last 4 items removed, 
	and then every other item in the remaining sequence.
	"""
	return seq[4:-4:2]

def reversed(seq):
	"""
	:param: sequence
	:return: sequence with the elements reversed
	"""
	return seq[::-1]	

def exchange_third(seq):
	"""
	:param: sequence
	:return: sequence with the last third, then first third, then 
	the middle third in the new order
	"""
	return seq[-(len(seq) // 3):] + seq[:(len(seq) // 3)] + seq[(len(seq) // 3):-(len(seq) // 3)] 

if __name__ == "__main__":
	# run tests

	# exchange_first_last tests
	assert exchange_first_last("this is a string") == "ghis is a strint"
	assert exchange_first_last((2, 54, 13, 12, 5, 32)) == (32, 54, 13, 12, 5, 2)
	assert exchange_first_last([2, 54, 13, 12, 5,32]) == [32, 54, 13, 12, 5, 2]
	assert exchange_first_last('') == ''
	assert exchange_first_last('a') == 'a' 

	# other_item_removed tests
	assert other_item_removed("this is a string") == "ti sasrn"
	assert other_item_removed((2, 54, 13, 12, 5, 32)) == (2, 13, 5)
	assert other_item_removed([2, 54, 13, 12, 5,32]) == [2, 13, 5]
	assert other_item_removed('') == ''
	assert other_item_removed('a') == 'a' 

	# remove_4 tests
	assert remove_4("this is a string") == " sas"
	assert remove_4((2, 54, 13, 12, 5, 32)) == ()
	assert remove_4([2, 54, 13, 12, 5,32]) == []
	assert remove_4('') == ''
	assert remove_4('a') == ''

	# reversed tests
	assert reversed("this is a string") == "gnirts a si siht"
	assert reversed((2, 54, 13, 12, 5, 32)) == (32, 5, 12, 13, 54, 2)
	assert reversed([2, 54, 13, 12, 5,32]) == [32, 5, 12, 13, 54, 2]
	assert reversed('') == ''
	assert reversed('a') == 'a' 

	# exchange_third tests
	assert exchange_third("this is a string") == "tringthis is a s"
	assert exchange_third((2, 54, 13, 12, 5, 32)) == (5, 32, 2, 54, 13, 12)
	assert exchange_third([2, 54, 13, 12, 5,32]) == [5, 32, 2, 54, 13, 12]
	assert exchange_third('') == ''
	assert exchange_third('a') == 'a'

	#if all tests pass then print 	  
	print("All Tests Passed")