#!/usr/bin/env python3

"""
PY210A-Session04
Cheng Liu
Trigrams
"""

if __name__ == "__main__":
    try:
        filename = 'sherlock_small.txt'
        file = open(filename, 'r')
    except IOError:
        print("Can not read file: ", filename)
    with open(filename, 'r'):
        lines = file.read()
        words = lines.split()
    for i in words:
        if i in ('-', ',', '.'):
            i = ''
# print(words)


def make_trigrams(words):
    tris = {}
    for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
        print(w1, w2, w3)
        pair = (w1, w2)
        if pair in tris:  # 'in' checks the key
            tris[pair].append(w3)
        else:
            tris[pair] = [w3]

    return tris


tris = make_trigrams(words)
