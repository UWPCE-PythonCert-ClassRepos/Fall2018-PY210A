"""
trigrams
"""



#Import modules
from pathlib import Path
import random

#set folder paths
data_folder = Path("C:\pythonuw\Fall2018-PY210A\students\ericstreit\session04/")

# set the variables
small_file_to_open = data_folder / "sherlock_small.txt"
words = "I wish I may I wish I might".split()

#grab text from a file to be used for trigrams
with open(small_file_to_open, 'r') as infile:
    scrape = infile.read()
    infile.closed
collection = scrape.split()
print(collection)

def make_trigrams(words):
    tris = {}
    for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
        #print(w1, w2, w3)
        #print(w1)
        #print(w2)
        #print(w3)
        pair = (w1, w2)
        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[pair] = [w3]

    print("the dictonary contains {}".format(tris))
    return tris


def print_trigrams():
    sentence = ""
    #start off with a pair
    pair = ('I', 'was')
    #pair = ('wish', 'I')
    #while loop to check if the pair exists in the dictionary
    while pair in tris:
        #get the pair value of the pair
        pv = tris.get(pair)
        print()
        print('getting the pair values of {} which is {}'.format(pair,pv))
        print()
        #we want only one pair word value here so let's use random to decide which one to grab if there is more than one
        l = len(pv) - 1
        rand = random.randint(0,l)
        #print('the random number is {}'.format(rand))
        #print()
        pv_word = pv[rand]
        print('grabbing a random word of the pair {} which is {}'.format(pv,pv_word))
        print()
        #now we want to grab the second word in the pair and join it to the selected pair value to make a new tupple to search for
        #this next piece turns the pair into a list that has an index I know how to work with
        temp_list = list(pair)
        print('making an indexed list of the pair {} and it is now {}'.format(pair,temp_list))
        print()
        #grab the fist and second word in that pair list
        first_word = temp_list[0]
        second_word = temp_list[1]
        print('grabbing the second word from the temporary list which is {}'.format(second_word))
        print()
        #join together the two
        #print(second_word)
        #print(pv_word)
        #append what we have to the sentence string
        #this needs to be fixed, I think I really only want to append the new pv_word
        #sentence = sentence + " " + first_word + " " + second_word + " " + pv_word
        sentence = sentence + " " + pv_word
        #now join the pair's second word with the value word to create the new tupple to search for
        new_pair = (second_word, pv_word)
        print('creating a new tupple pair from "{}" and "{}" which creates {}'.format(second_word, pv_word,new_pair))
        print()
        #update the pair variable with the new pair to search for
        pair = new_pair
        #let's check our sentence so far
        print('the sentence so far is: {}' .format(sentence))
        print()
        #ok, what will we look for next?
        print('now go thru the beginning of the loop again looking for a key match using {}'.format(pair))
        print()
        #pause in case things break
        #pause = input('press a key')
    #the while loop has ended, let's show what we've found
    print("-" * 80)
    print('No more pairs were found! Here is the full sentence: ')
    print(sentence)




tris = make_trigrams(collection)
print_trigrams()
