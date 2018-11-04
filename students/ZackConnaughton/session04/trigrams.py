#!/usr/bin/env python

"""
trigrams!
"""
import random
from string import punctuation

def strip_punct(s):
    if '--' in s:
        return s.replace('--', ' ')
    return s


words = 'I wish I may I wish I might'

def make_trigrams(words):
    tris = {}
    just_words = strip_punct(words)
    words_list = just_words.split()
    for i in range(len(words_list) - 2):
        w1 = words_list[i]
        w2 = words_list[i + 1]
        w3 = words_list[i + 2]
        pair = (w1, w2)
        if pair in tris:
            if not tris[pair] == list(w3):
                tris[pair].append(w3)
        else:
            tris[pair] = [w3]
    return tris

def long_file(file):
    f = open(file, 'r')
    output_tris = make_trigrams(f.read())
    f.close()
    return output_tris


def output_next(dict):
    pass


tris = make_trigrams(words)
long_tris = long_file('sherlock_small.txt')


if __name__ == '__main__':
    make_trigrams(words)
    print(long_file('sherlock_small.txt'))
