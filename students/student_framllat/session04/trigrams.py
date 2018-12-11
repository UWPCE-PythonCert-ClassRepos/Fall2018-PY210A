#!/usr/bin/env python3

import re
import os
import string

"""
trigrams
"""

# import file into a list
with open('./four_sc.txt') as f:
    #word_list = ()
    word_list = []
    lines = f.readlines()
    for l in lines:
        l = re.sub(r'["|,|-|?|$|.|!]',r'', l)
        l = l.replace("\n","")
        word_list.append(l.split(" "))

#t_word_list = tuple(word_list)

def make_trigrams(word_list):
    tris = {}
    for w1, w2, w3 in zip(word_list[:-2], word_list[1:-1], word_list[2:]):
        print(w1, w2, w3)
        pair = (w1, w2)
        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[pair] = [w3]

    return tris

print(word_list)
#print(len(word_list))
#t_word_list = tuple(word_list)
tris = make_trigrams(word_list)
