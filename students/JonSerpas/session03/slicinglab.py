a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

#replaces the first and last in a sequence
def exchange_first_last(seq):
	first = seq[:1]
	middle = seq[1:-1]
	last = seq[-1:]
	new_value = last + middle + first
	return(new_value)

	
#returns every other item in the sequence
def every_other(seq):
	return(seq[::2])
	print(seq)
#removes first and last four in the sequence and returns remainder
def first_and_last_four(seq):
	return(seq[4:-4])

#returns sequence in reverse order
def reverse(seq):
	return(seq[-1::-1])

#first, last, and middle third in new order
def thirds(seq):
	first_third = seq[:3]
	last_third = seq[-3:]
	middle_third = seq[3:-3]
	return(middle_third, last_third, first_third)	



assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert every_other(a_string) == "ti sasrn"
assert every_other(a_tuple) == (2, 13, 5)
assert first_and_last_four(a_string) == ' is a st'
first_and_last_four(a_tuple) #returns AssertionError - not enough items in Tuple
assert reverse(a_string) == 'gnirts a si siht'
assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
assert thirds(a_string) == 's is a str', 'ing', 'thi'
assert thirds(a_tuple) == (), (12, 5, 32), (2, 54, 13)