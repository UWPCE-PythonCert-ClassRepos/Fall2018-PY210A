#!/usr/bin/env python3
"""
trigrams
"""

words = "I wish I might I wish I might".split()

print(words)

def make_trigrams(words):
    tris = {}
    for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
        print(w1, w2, w3)
        pair = (w1, w2)
        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[(w1, w2)] = [w3]
    return tris
tris = make_trigrams(words)


if __name__ == "__main__":
    make_trigrams(words)
