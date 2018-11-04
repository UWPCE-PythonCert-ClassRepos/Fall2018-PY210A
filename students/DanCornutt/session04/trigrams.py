#!/usr/bin/env python3

import random


"""
trigrams
read file from source by line, remove characters: - , ( ) and save text as _edit
take edited text, create trigram
"""

RM_CHAR = {'(': '', ')': '', ',': '', '--': ' '}

def cp_f(source, chars):
    """Reads file, removes unwanted characters, saves to new
    "_edit" file, returns new file path.

    Keyword arguments:
    source -- relative filepath of file to be processed
    chars -- dict where k: characters to remove & v: change k to
    """

    destination = "{}_edit{}".format(source[:-4], source[-4:])
    with open(source, 'r') as f_in, open(destination, 'w') as f_out:
        while True:
            next_ln = f_in.readline()
            if not next_ln:
                break
            f_out.write(clean_txt(next_ln, RM_CHAR))
    f_in.closed, f_out.closed
    return destination


def clean_txt(ln, del_lst):
    for k, v in del_lst.items():
        ln = ln.replace(k, v)
    return ln

def find_next():
    pass


def make_trigrams(source):
    with open(source) as f_in:
        text = f_in.read().split()
        word_count = len(text)
        f_in.close()
        tris = {}
        for w1, w2, w3 in zip(text[:-2], text[1:-1], text[2:]):
            # print(w1, w2, w3)
            pair = (w1, w2)
            if pair in tris:
                tris[pair].append(w3)
            else:
                tris[(w1, w2)] = [w3]
    f_in.closed


    last_key = random.choice(list(tris.keys()))
    new_text = (last_key[0].title() + " " + last_key[1])
    print(new_text)
    for x in range(word_count):
        next_key = (last_key[1], random.choice(tris.setdefault(last_key, text)))
        new_text += " " + str(next_key[1])
        last_key = next_key
        print("finished loop {}".format(x))
        print(new_text)

    return tris



if __name__ == "__main__":
    f_nm = "sherlock_small.txt"
    f_edit = cp_f("./" + f_nm, RM_CHAR)
    new_book = make_trigrams(f_edit)
