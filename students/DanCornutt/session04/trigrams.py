#!/usr/bin/env python3
"""
trigrams
read file from source by line, remove characters: - , ( ) and save text as _edit
take edited text, create trigram
"""

RM_CHAR = {'(': '', ')': '', ',': '', '--': ' '}

def cp_f(source):
    """
    read txt file from source
    call clean_txt function
    write txt file to destination
    """
    with open(source, 'r') as f_in, open(source + "_edit", 'w') as f_out:
        while True:
            next_ln = f_in.readline()
            if not next_ln:
                break
            f_out.write(clean_txt(next_ln, RM_CHAR))
        f_in.closed, f_out.closed


def clean_txt(ln, del_lst):
    for k, v in del_lst.items():
        print(k, v)
        print(ln)
        ln = ln.replace(k, v)
        print(ln)
    return ln

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
