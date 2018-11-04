#!/usr/bin/env python3
"""
trigrams
read file from source by line, remove characters: - , ( ) and save text as _edit
take edited text, create trigram
"""

words = "I wish I might I wish I might".split()

def cp_f(source):
    #read file from source
    with open(source, 'r') as f_in, open(source + "_edit", 'w') as f_out:
        while True:
            ln = f_in.readline()
            if not ln:
                break
            f_out.write(clean_txt(ln))
        f_in.closed
        f_out.closed


def clean_txt(string):
    new_string = string.replace('--', ' ')
    return new_string

def make_trigrams(source):
    cp_f(source)

    # tris = {}
    # for w1, w2, w3 in zip(text[:-2], text[1:-1], text[2:]):
    #     # print(w1, w2, w3)
    #     pair = (w1, w2)
    #     if pair in tris:
    #         tris[pair].append(w3)
    #     else:
    #         tris[(w1, w2)] = [w3]
    # return tris





if __name__ == "__main__":
    make_trigrams("./sherlock_small.txt")
