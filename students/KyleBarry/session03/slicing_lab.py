def first_last_ex(seq):
	""" 
	Return a sequence with the first and last values swapped.
	You need colons for each slicingoperator or else tuples and lists 
	can't be concatenated
	""" 
	return seq[-1:] + seq[1:-1] + seq[0:1]

def every_other_freckle(seq):
	"""
	Every other freckle is just the name of a song I like.
	Return a sequence with every other value removed.
	"""
	return seq[::2]

def just_the_middle(seq):
	""""
	Return a sequence with the first four and last four values removed
	"""
	return seq[4:-4]

def reverse(seq):
	"""
	Return a sequence in reverse
	"""
	return seq[-1::-1]

def thirds(seq):
	"""
	Return a sequence with the last third first, then the first third, then the
	middle third
	"""
	th = len(seq)//3

	return seq[-th:] + seq[:th] + seq[th:-th]

if __name__=='__main__':
	assert first_last_ex([1,2,3,4,5]) == [5,2,3,4,1]
	assert first_last_ex('flippyfloppy') == 'ylippyfloppf'

	assert every_other_freckle((10,20,30,40,50)) == (10,30,50)
	assert every_other_freckle('toh;i6s') == 'this'

	assert just_the_middle('gonenotgonegone') == 'notgone'

	assert reverse([-87, -56, -2, 91, 1245]) == [1245, 91, -2, -56, -87]
	assert reverse(('last', 'middle', 'first')) == ('first', 'middle', 'last')

	assert thirds('dingdangdong') == 'dongdingdang'
	assert thirds('') == ''
	assert thirds((5,6,7,8,9,10,11,12,1,2,3,4)) == (1,2,3,4,5,6,7,8,9,10,11,12)
	print('All assertions passed')







