#!/usr/bin/env python3

# Write in the file as txt
import re # Will be used to help strip the text
import random # Will use random to pull random keys from trigrams


def open_text(filename):
    #with open("C:\Users\Zach\UWPYTHON\Fall2018-PY210A\students\ZachCooper\session04\sherlock_small.txt") as f:
    #infle = f.readlines()
    #for line in f:
        #print(line)

    with open(filename, "r") as f: # Pass in variable filename create in main
        full_lines = f.readlines()

    list_of_words = []

    for l in full_lines:
        # Nice little example we used in foundations to strip everything from f.readlines
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

def make_text(tris):
    """I was able to get everything until this point, used your outline and online examples to help me finish make_text function"""
    # Create new text list
    new_text = []

    for i in range(10): # Start with first 10 lines
        new_sentence = list(random.choice(list(tris.keys()))) # Pull random key to start with from tris
        for j in range(random.randint(2, 10)): # Random words added
            pair = tuple(new_sentence[-2:]) # Followed another word pair of two more words
            new_sentence.append(random.choice(tris[pair]))

        # First word capitalize
        new_sentence[0] = new_sentence[0].capitalize()

        # Add punctuation
        new_sentence[-1] += "."
        new_text.extend(new_sentence)
    # Join new sentence into sentence
    new_text = " ".join(new_text)

    return new_text



if __name__ == "__main__":      

    # Create variable with txt file location
    filename = r"C:\Users\Zach\UWPYTHON\Fall2018-PY210A\students\ZachCooper\session04\sherlock_small.txt"

    # Use a longer and more complex txt example, make sure to change filename variable in functions
    #filename2 = r"C:\Users\Zach\UWPYTHON\Fall2018-PY210A\students\ZachCooper\session04\land_time_forgot.txt"

    # Create list of words with reading filename function
    list_of_words = open_text(filename)

    # Create trigrams with function created in class with list passed in
    tris = make_trigrams(list_of_words)

    new_text = make_text(tris)
    print(new_text)


