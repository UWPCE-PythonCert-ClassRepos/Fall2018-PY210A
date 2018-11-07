'''
trigrams
'''

words = "I wish I may I wish I might".split()

print(words)

def make_trigrams(words):
	tris = {}
	#for i in range(len(words)): #lookup itertools islice
	for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
		print(w1, w2, w3)

make_trigrams(words)

