#!/usr/bin/env python3

import random
import sys


"""
trigrams hw session 4
Read file from source by line, remove unwanted characters, save text as _edit,
take edited text, create trigram
"""

RM_CHAR = {'(': '', ')': '', ',': '', '--': ' ', "'": "", '"': ''}

def cp_f(source, chars):
    """Read file then save to new "_edit" file.

    Keyword arguments:
    source -- relative filepath of file to be processed
    chars -- dict where k: characters to remove & v: change k to
    returns relative path to new text file
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
    """Remove unwanted characters from string.

    Keyword arguments:
    ln -- imput string of text
    del_lst -- dictionary of characters to remove and replcement values
    returns edited string
    """

    for k, v in del_lst.items():
        ln = ln.replace(k, v)
    return ln


def make_trigrams(source):
    """Create trigram, return made trigram

    Keyword arguments:
    source -- relative path of input txt file
    returns string of new trigram
    """


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
    for x in range(word_count):
        next_key = (last_key[1], random.choice(tris.setdefault(last_key, text)))
        new_text += " " + str(next_key[1])
        last_key = next_key
    new_text += "."
    return new_text

def create_book(frm):
    f_nm = frm
    f_edit = cp_f("./" + f_nm, RM_CHAR)
    return make_trigrams(f_edit)


if __name__ == "__main__":
    try:
        f_name = sys.argv[1]
    except IndexError:
        print("You must pass in a filename!")
        sys.exit(1)

    new_book = create_book(f_name)
    print(new_book)
