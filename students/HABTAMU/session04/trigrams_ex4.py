#!/usr/bin/env python3

import random
import sys

f_name = "sherlock_small.txt"

def read_in_data(f_name):
    """
    read the contents of a project Gutenberg book
    returns it as one big string
    """
    with open(f_name) as f:
        content = f.readlines()
        content = [strip_punc(line) for line in content]
        words = []
        for line in content:
            line = line.split()
            words.extend(line) 
    return words


def build_trigrams(words):
    """build a trigram dict from the passed-in list of words"""

    trigrams = {}
    for i in range(len(words) - 2):
        pair = tuple(words[i:i+2])
        follower = words[i + 2]
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]

    return trigrams


def strip_punc(my_punc):
    """We need to strip out those punctuation or replace the following list of punctuation with an empity space """

    punc = [',', '--', '(', ')', '.']
    for p in punc:
        my_punc = my_punc.replace(p, ' ')
    return my_punc.strip()


def build_txt(trigrams):
    """
    Build up some new “fake” text and one big string sentence , first pick a random key pair to start with from a dict trigrams.
    arguments:
        dict_key from trigrams
    return:
        list: fake_txt[]
        sent_str:
    """

    fake_txt = []
    # pair_txt = random.choice(list(trigrams.keys()))
    # fake_txt.extend(pair_txt)

    while len(fake_txt) < 50:
        pair = tuple(fake_txt[-2:])
        try:
            followers = trigrams[pair]
        except KeyError:
            print(" this pair is not there", pair)
            pair = random.choice(list(trigrams.keys()))
            followers = trigrams[pair]

        one_word = random.choice(followers)
        fake_txt.append(one_word)

    # concatenate list item into strings
    sent_str = " ".join(fake_txt)
    print(sent_str)


if __name__ == "__main__":
    #get the filename from the command line
    try:
        f_name = sys.argv[1]
    except IndexError:
        print("Youn must pass in a filename")
        sys.exit(1)
    words = read_in_data(f_name)
    trigrams = build_trigrams(words)
    new_txt = build_txt(trigrams)
    #print(new_txt)
