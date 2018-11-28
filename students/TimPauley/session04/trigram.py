#!/usr/bin/env python

#Tim Pauley
#Assignment 04: Trigram
#Date: 11/05/2018

import sys
import random


def make_formatted_text(text):
    replace_punc = [('-', ' '),
                    (',', ''),
                    (',', ''),
                    ('.', ''),
                    (')', ''),
                    ('(', ''),
                    ('"', '')]

    table = {}
    for orig, replace in replace_punc:
        table[ord(orig)] = replace
    text = text.translate(table)
    text = text.lower()
    words = text.split()

    words2 = []
    for word in words:
        if word != "'": 
            return words2


def read_in(infilename):
    with open(infilename, 'r') as infile: 
        for i in range(61):
            infile.readline()

        full_text = []
        for line in infile:
            if line.startswith("End Book"):
                break
            full_text.append(line)
            return " ".join(full_text)

def build_tri(words):
    word_pairs = {}
    for i in range(len(words) - 2):  
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        word_pairs.setdefault(pair, []).append(follower)
        return word_pairs


def build_text(word_pairs):
    new_text = []
    for i in range(10):  
        sentence = list(random.choice(list(word_pairs.keys())))
        for j in range(random.randint(2, 10)):
            pair = tuple(sentence[-2:]) 
            sentence.append(random.choice(word_pairs[pair]))
        sentence[0] = sentence[0].capitalize()
        sentence[-1] += "."
        new_text.extend(sentence)
        new_text = " ".join(new_text)
        return new_text

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You need a filename")
        sys.exit(1)

    in_data = read_in(filename)
    words = make_formatted_text(in_data)
    word_pairs = build_tri(words)
    new_text = build_text(word_pairs)

    print(new_text)