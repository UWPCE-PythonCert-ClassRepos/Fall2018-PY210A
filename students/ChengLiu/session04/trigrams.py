#!/usr/bin/env python3

"""
PY210A-Session04
Cheng Liu
Trigrams
"""


def readfile(filename):
    """ Read the file and return strings """
    with open(filename, 'r') as contents:
        # removing the first 61 lines - header/table of contents, etc.
        for i in range(61):
            contents.readline()

        file_string = []
        for line in contents:
            # identifying the end of the book contents
            if line.startswith("End of the Project Gutenberg EBook"):
                break
            file_string.append(line)
    # print(file_string)
    return " ".join(file_string)


def cleanwords(file):
    """remove punctuations and non-contents from the file"""
    punc_list = ["-", ",", ".", "=", "?"]
    for punc in punc_list:
        file = file.replace(punc, "")

    words = file.lower().split()
    words2 = []
    for word in words:
        if words != "'":
            words2.append("I" if word == 'i' else word)
    # print(word)
    return words2


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


if __name__ == "__main__":
    try:
        filename = 'sherlock.txt'
        file = readfile(filename)
    except IOError:
        print("Can not read file: ", filename)

    # print(file)
    words = cleanwords(file)
    # print(words)
    tris = make_trigrams(words)
