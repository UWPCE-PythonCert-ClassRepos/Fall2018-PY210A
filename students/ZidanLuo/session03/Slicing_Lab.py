def exchange_first_last (seq):
	new_seq = seq[-1:] + seq[1:-1] + seq[:1]
	return new_seq


def rm_everyother_item (seq):
	return seq[::2]


def first_4_rm_seq (seq):
	result = seq[4:-4]
	return result[::2]

def reversed_elements(seq):
	return seq[::-1]


def last_third(seq):
	return seq[-3:] + seq[:3] + seq[3:-3]


if __name__ == "__main__":
	assert exchange_first_last([0, 1, 2, 3]) == [3, 1, 2, 0]
	assert exchange_first_last((23, 3, 15, 4)) == (4, 3, 15, 23)
	assert exchange_first_last("hello world!") == "!ello worldh"
	assert exchange_first_last(["do", "not", "forget", "to", "test"]) == ["test", "not", "forget", "to", "do"]
	print("exchange_first_last is valid!")

	#Test rm_everyother_item function
	assert rm_everyother_item([0, 1, 2, 3, 4]) == [0, 2, 4]
	assert rm_everyother_item(('item', 'to', 'be', 'removed')) == ('item', 'be')
	assert rm_everyother_item("hello world!") == "hlowrd"
	print("rm_everyother_item is valid")

	#Test the first 4 and last 4 items removed, and then every other item in the remaining sequence
	assert first_4_rm_seq((0, 2, 4, 5, 6, 7, 3, 4, 6, 5, 6,)) == (6, 3)
	assert first_4_rm_seq(["This", "is", "just", "a", "test", "for", "function", "three", "!"]) == ["test"]
	assert first_4_rm_seq("hello world!") == "ow"
	print("first_4_rm_seq is valid")

	#Test for sequences with elements reversed
	assert reversed_elements((0, 1, 2, 3, 4)) == (4, 3, 2, 1, 0)
	assert reversed_elements("hello world!") == "!dlrow olleh"
	assert reversed_elements(["this", "is", "a", "list"]) == ["list", "a", "is", "this"]
	print("reversed_elements is valid")

	#Test for sequences with the last theird, first third, and middle third in new order
	assert last_third((1, 2, 3, 4, 5, 6, 7, 8, 9)) == (7, 8, 9, 1, 2, 3, 4, 5, 6)
	assert last_third(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']) == ['g', 'h', 
						'i', 'a', 'b', 'c', 'd', 'e', 'f']
	assert last_third("abcdefghi") == "ghiabcdef"
	print("last_third is valid")