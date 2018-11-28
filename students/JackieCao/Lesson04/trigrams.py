#!/usr/bin/env python3
"""
Trigrams
"""
import random
import sys

def read_book(filename):
    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def make_words(book, stat_line, end_line):
    # specify the start and ending line (exclusive)
    n = [i for i,x in enumerate(book) if x == start_line] 
    N = [i for i,x in enumerate(book) if x == end_line]
    text = list()
    for i in range(n[0]+1,N[0]):
        if book[i] != '':
            add_word = book[i].split()
            text = text + add_word
    return text
 
def make_trigrams(words):
    tris = {}
    for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
        pair = (w1, w2)
        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[pair] = [w3]
    return tris

def build_text(trigrams):
    start_key = random.choice(list(trigrams.keys()))
    l = list(start_key)
    while True:
        # tell the loop when to stop
        if len(l) == len(words):
            break
        elif start_key in trigrams:
            the_third = random.choice(trigrams[start_key])
            l.append(the_third)
            # re-define the start_key
            start_key = tuple(l[-2:])
        else:
            start_key = random.choice(list(trigrams.keys()))
    new_text = " ".join(l)
    if new_text[-1].isalpha:
        new_text = new_text + '.'
    else:
        new_text[-1] = '.'
    return new_text

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("--start_line", default = 'ADVENTURE I. A SCANDAL IN BOHEMIA', help = "which line to start")
    parser.add_argument("--end_line", default = 'End of the Project Gutenberg EBook of The Adventures of Sherlock Holmes, by ', help = "which line to end")

    args = parser.parse_args()

    filename = args.filename
    book = read_book(filename)
    start_line = args.start_line
    end_line = args.end_line
    words = make_words(book, start_line, end_line)

    trigrams = make_trigrams(words)
    new_text = build_text(trigrams)
    print(new_text)


