#!/usr/bin/env python 3
import random


def replace_punc(my_punc):

    punc = [',', '--', '(', ')', '.']
    for p in punc:
        my_punc = my_punc.replace(p, ' ')
    return my_punc.strip()



def read_in_words(filename):
    text = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):

            if lines[i].startswith("*** START OF THIS PROJECT"):
                del lines[:i+1]
                break

        for i in range(len(lines)-1, 0, -1):
            if lines[i].startswith("*** END OF THIS PROJECT GUTENBERG EBOOK"):
                del lines[i:]
                break
        words = []
        for line in lines:
            line = line.strip()
            line = line.strip('\n')
            line = replace_punc(line)
            line = line.split(' ')
            words.extend(line)

    return words


def build_trigrams(words):
    '''build up the trigram dict from the list of words
    returns a dict with
    keys: word pairs
    values:list of followers
    '''
    tris = {}
     #build up the dict here
    for i in range(len(words_list)-2):
        pair = ' '.join(words_list[i:i + 2]) # how can you make a valid key out of it
        follower = words_list[i+2]

        #if pair already in the dict, then add the follower

        if pair in trigrams:
            trigrams[pair].append(follower)


        #if pair not in the dict

        else:
            trigrams[pair] = [follower]

        return tris

def build_text(tris)
    start_key = random.choice(list(tris.keys()))
    new_text_list = list(start_key)
    new_text.extend(start_key)
    while len(new_text_list) < 50:
        third_word = random.choice(tris[start_key])
        new_text_list.append(third_word)
        start_key = tuple(new_text[-2:])

    new_text = " ".join(new_text_list)

    return new_text + '.'








if __name__ == '__main__':

    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    words = read_in_words(filename)
    tris = build_trigram(words)
    new_text = build_text(tris)

    print(new_text)

