"""
trigrams

Objectives: punctuation, paragraphs, 
*** START OF THIS PROJECT GUTENBERG EBOOK
"""
import sys
import string
import random

#words = "I wish I may I wish I might".split()

#Output
#['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']

def make_trigram(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """

    tris = {}
    for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
        print(w1, w2, w3)
        pair = (w1, w2)
        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[pair] = [w3]

    return tris

#tris = make_trigrams(words)


def read_in_data(f_txt):
	"""
    Open txt file and read each line and parse in to words
    Read and ignore 20 lines above the headeri
	Read and ignore 

	params: take text file name
    returns a list of all the words    
    """

	wd_list = []
	#read and igmore 20 lines in the file
	try:
		with open (f_txt) as f_in:
			# for line in range (20):
		    #f_in.readline()
			for line in f_in:
				wd_list.extend(line.split())
		f_in.close()
	except IOError:
		print("Cannot find file {}".format(f_txt))


	return wd_list

#make words - avoid punctuation andcapitol, 
def make_words(d1):
	pnc = set(string.punctuation)

    #replace punctuation to empty 
	for x in range (len(d1)):
		if d1[x] != 'I':
			d1[x] = d1[x].lower()
		for w1 in pnc:
			d1[x] = d1[x].replace(w1, '')
	return d1

    
def build_text(wd):

	a_li
	st = wd
	print(len(wd))
    random.randint(1, 2)
    random.choice(a_list)


if __name__ == "__main__":
	#get the filename from the command line
	try:
		filename = sys.argv[1]
	except IndexError:
		print("You must pass in the filename")
		sys.exit(1)

	in_data = read_in_data(filename)
	words = make_words(in_data)
	word_pairs = make_trigram(words)
	new_text = build_text(word_pairs)

	#print(new_text)
