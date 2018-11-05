#!/usr/bin/env python3

"""
trigrams
"""


#print(words)

def file_to_word_list():
    with open('sherlock.txt') as f:
        word_list = []
        for line in f.readlines():
            words = line.split()
            word_list.extend(words)
        return word_list


def make_trigrams(new_lines):
    tris = {}
    for w1, w2, w3 in zip(new_lines[:-2], new_lines[1:-1], new_lines[2:]):
        print(w1, w2, w3)
        pair = (w1, w2)
        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[pair] = [w3]

    return tris


if __name__ == "__main__":
    import pdb; pdb.set_trace()
    make_trigrams(file_to_word_list())


###next steps are running make_trigrams with the output of open_file as input - need to create a dict of the trigrams - see trigrams exercise for full instructions.
