#function exchange the first and last index
#string and tuple

def exchange_first_last (seq):
		if type(seq) == tuple:
			first = (seq[0], )
			last = (seq[-1], )
			seq = last + seq[1:-1] + first
			return seq
		elif type(seq) == str:			
			first_str = seq[0]
			last_str = seq[len(seq)-1]
			seq = last_str + first_str.join(seq[1:len(seq)].split(seq[len(seq)-1]))
			return seq

if __name__ == "__main__":

 	a_string = "this is a string"
 	print(exchange_first_last(a_string))
 	a_tuple = (2, 54, 13, 12, 5, 32)
 	print (exchange_first_last(a_tuple))
 	assert exchange_first_last(a_string) == "ghis is a strint"
 	assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)