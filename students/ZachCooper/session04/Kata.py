#!/usr/bin/env python3

# Write in the file as txt
import re


def open_text():
    #with open("C:\Users\Zach\UWPYTHON\Fall2018-PY210A\students\ZachCooper\session04\sherlock_small.txt") as f:
    #infle = f.readlines()
    #for line in f:
        #print(line)

    with open("./land_time_forgot.txt", "r") as f:
        full_lines = f.readlines()

    list_of_words = []

    for l in full_lines:
        line = re.sub('\s\s+', ' ', re.sub('[^a-zA-Z]', ' ', l))
        list_of_words.extend(line.split())
    return list_of_words


    #with open("./sherlock_small.txt") as f:
    #   for lines in f:
    #        new_lines = lines.strip("\n""[]")
    #
    #        print(new_lines)"""



def make_trigrams(list_of_words):
    tris = {}
    """for i in range(len(words)):"""
    for w1, w2, w3 in zip(list_of_words[:-2], list_of_words[1:-1], list_of_words[2:]):
        print(w1, w2, w3)
        pair = (w1, w2)
        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[pair] = [w3]

    return tris


if __name__ == "__main__":

    list_of_words = open_text()
    tris = make_trigrams(list_of_words)



