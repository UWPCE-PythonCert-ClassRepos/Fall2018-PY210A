#!/usr/bin/env python3

"""
trigrams
"""

import string
import random


def file_to_word_list(input_file):
    """#function to open any file, convert it to a list and break up"""
    with open(input_file) as f:
        file_without_header = advance_past_header(f)
        word_list = []
        for line in file_without_header.readlines():
            dirty_words = [dirty_word.lower() for dirty_word in line.split()]
            clean_words = [remove_punctuation(dirty_word) for dirty_word in dirty_words]
            word_list.extend(clean_words)
        return word_list


def remove_punctuation(dirty_word):
    #import pdb;pdb.set_trace()
    chars_ = list(string.punctuation)
    cleaner_word = dirty_word #re-aliasing for readability
    for char_ in chars_:
        cleaner_word = cleaner_word.replace(char_, '')
    return cleaner_word



def advance_past_header(file_object):
    end_of_header = "*** START OF THIS PROJECT"
    for line in file_object:
        if end_of_header in line:
            return file_object
    else:
        ValueError("Header not found in file.")



def make_trigrams_dict(word_list):
    """create dictionary of words from file_to_word_list()"""
    tris = {}
    for w1, w2, w3 in zip(word_list[:-2], word_list[1:-1], word_list[2:]):
        pair = (w1, w2)
        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[pair] = [w3]

    return tris



def trigrams_to_new_text(tris):
    """create a new body of text using random keys and values from the trigrams_dict (tris)"""
    new_text_list = []
    target_length = 50
    current_key = random.choice(list(tris.keys()))
    new_text_list.extend(current_key)
    while len(new_text_list) < target_length:
        list_of_candidates = tris[current_key]
        third_word = random.choice(list_of_candidates)
        current_key = current_key[1], third_word
        new_text_list.append(third_word)
    return " ".join(new_text_list)




if __name__ == "__main__":
    word_list = file_to_word_list('sherlock.txt')
    tris = make_trigrams_dict(word_list)
    print(trigrams_to_new_text(tris))




