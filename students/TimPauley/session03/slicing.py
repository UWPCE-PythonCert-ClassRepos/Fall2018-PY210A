#!/usr/bin/env python3

#Tim Pauley
#Assignment 03
#Date Oct 27 2018


#Write some functions that takes a sequence as an argument
#, and returns a copy of that sequence:

#1 the first and last items exchanged.
def swap(seq):
	return seq[-1:] + seq[1:-1] + seq[:1]

#2 every other item removed.
def remove(seq):
    return seq[::2]

#3 the first 4 and the last 4 items removed
def middle(seq):
	return seq[4:-4]

#4 the elements reversed (just with slicing).
def reverse(seq):
	return seq[-1::-1]

#5 the last third, then first third, then the middle third in the new order.
def thirds(seq):
	th = len(seq)//3
	return seq[-th:] + seq[:th] + seq[th:-th]

#test
if __name__=='__main__':
	assert swap('LibTechBirdman') == 'nibTechBirdmaL'

	assert remove('LibTechBirdman') == 'Lbehida'

	assert middle('LibTechBirdman') == 'echBir'

	assert reverse('LibTechBirdman') == 'namdriBhceTbiL'

	assert thirds('LibTechBirdman') == 'dmanLibTechBir'
	
	print('All assertions passed with flying colors!')





   
