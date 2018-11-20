#!/usr/bin/env python3
import sys
import random

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words
	    return the a dict with:
	        keys: word pairs
	        values: list of followers
    """
    trigrams = {}
    for i in range(len(words)-2):
        pair = words[i:i+2]
        followers = words[i+2]
        if tuple(pair) in trigrams.keys():
            trigrams[tuple(pair)].append(followers)
        else:
            trigrams[tuple(pair)] = [followers]
    return trigrams

def read_in_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()[61:]

    end_sentence = [line for line in lines if line.startswith("End of the Project Gutenberg EBook")]
    index = lines.index(end_sentence[0])
    text = [x.rstrip() for x in lines if (lines.index(x) < index and x !='\n')]
    return " ".join(text)


def make_words(in_data):
    return in_data.split()

def build_text(word_pairs):
    new_text = list(random.choice(list(word_pairs)))
    for j in range(250):
        pair = tuple(new_text[-2:])
        new_text.append(random.choice(word_pairs[pair]))
    new_text[0] = new_text[0].capitalize()
    return new_text
	
if __name__ == "__main__":
    try:
    	filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    words_pairs = build_trigrams(words)
    new_text = build_text(words_pairs)

    print(' '.join(new_text))
