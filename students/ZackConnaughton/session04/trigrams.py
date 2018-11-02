#!/usr/bin/env python

"""
trigrams!
"""

words = 'I wish I may I wish I might'

def make_trigrams(words):
    tris = {}
    words_list = words.split()
    for i in range(len(words_list) - 2):
        w1 = words_list[i]
        w2 = words_list[i + 1]
        w3 = words_list[i + 2]
        pair = (w1, w2)
        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[pair] = [w3]
    return tris

#set default


tris = make_trigrams(words)


if __name__ == '__main__':
    make_trigrams(words)
