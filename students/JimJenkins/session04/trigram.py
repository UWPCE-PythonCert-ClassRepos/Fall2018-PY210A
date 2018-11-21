#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr)
Date: 11/05/2018

"""


words = "I wish I may I wish I might".split()
print(words)

def make_trigrams(words):
	tris = {}
	for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
		print(w1, w2, w3)
		pair = (w1, w2)
		if pair in tris:
			tris[pair].append(w3)
		else:
			tris[(w1, w2)] = []
		return tris

	#for i in range(len(words)):

from itertools import islice

for w1, w2, w3, in zip(islice(word_list, 0, None),
					   islice(word_list, 1, None),
					   islice(word_list, 2, None)):
	print(w1, w2, w3)
