#!/usr/bin/env python3
'''
Trigrams
Trigrams can be used to mutate text into new, surreal, forms. \
But what heuristics do we apply to get a reasonable result?
'''
import random
import os
#TEST_STRING = 'I wish I may I wish I might'
def build_data(string):
    '''
    Trigram analysis is very simple. Look at each set of three adjacent words \
    in a document. Use the first two words of the set as a key, and remember \
    the fact that the third word followed that key.
    '''
    words = string.split()
    build_dict = {}
    for i in range(len(words)-2):
        first = words[i]
        second = words[i+1]
        third = words[i+2]
        pair = first+' '+second
        build_dict.setdefault(pair, [])
        build_dict[pair].append(third)
    return build_dict

#TEST_DICT = build_data(TEST_STRING)

def build_new(data_dict, num_of_words=10):
    '''
    To generate new text from this analysis, choose an arbitrary word pair as a \
    starting point. Use these to look up a random next word (using the table above) \
    and append this new word to the text so far.
    '''
    build_new_string = ''
    build_new_string = random.choice([k+' '+random.choice(v)+' ' \
    for k, v in data_dict.items()])
    #print(build_new_string)
    for _ in range(num_of_words):
        try:
            pair = ' '.join(build_new_string.split()[-2:])
            next_string = random.choice(data_dict[pair])+' '
            build_new_string += next_string
            #print('pair: ', pair, 'next_string: ', next_string, \
            #'build_new_string: ', build_new_string)
        except KeyError:
            continue
    return build_new_string

#NEW_STRING = build_new(TEST_DICT)

def load_file(system_file):
    '''
    Load file of text from system_file
    '''
    big_dict = {}
    with open(system_file, 'r') as infile:
        for line in infile:
            big_dict.update(build_data(line))
    return big_dict

if __name__ == '__main__':
    FILE_LIST = [file for file in os.listdir()]
    RESPONSE = ''
    for file in enumerate(FILE_LIST):
        print(file)
    RESPONSE = int(input('Please select from the files listed above: '))
    RESPONSE_SELECTION = FILE_LIST[RESPONSE]
    RESPONSE_2 = int(input('How many words would you like in the new string?: '))
    NEW_BOOK = build_new(load_file(RESPONSE_SELECTION), num_of_words=RESPONSE_2)
    print(NEW_BOOK)