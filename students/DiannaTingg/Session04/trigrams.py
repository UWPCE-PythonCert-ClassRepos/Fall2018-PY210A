# Lesson 04 Exercise: Trigrams

import sys
import random


# Make a dictionary with the first two words as the key and the third word as the value
def make_trigrams(words):
    tris = {}

    for i in range(len(words)-2):
        pair = tuple(words[i:i+2])
        follower = words[i+2]

        # If pair in dictionary, append value, otherwise add it
        if pair in tris:
            tris[pair].append(follower)
        else:
            tris[pair] = [follower]
    return tris


# Get random capitalized pair from dictionary
def get_random_pair(d):
    while True:
        pair = random.choice(list(d.keys()))
        if pair[0].isupper():
            return pair


# Use dictionary to build new text
def use_trigrams(d):
    start = get_random_pair(d)

    text_words = list(start)

    while len(text_words) < 500:
        pair = tuple(text_words[-2:])

        if pair in d:
            text_words.append(random.choice(d[pair]))
        else:
            text_words[-1] += "."
            alternate_pair = get_random_pair(d)
            text_words.extend(list(alternate_pair))

    final_text = "TRIGRAMS SHORT STORY\n\n" + " ".join(text_words) + "! \n\nTHE END"
    return final_text


# Open text file and read in contents
def read_file(file):
    with open(file, "r") as f:
        text = []
        lines = f.readlines()

        # Remove headers at beginning of file
        for i in range(len(lines)):
            if lines[i].startswith("*** START OF THIS PROJECT GUTENBERG EBOOK"):
                del lines[:i+1]
                break

        # Remove footers at end of file (loop backwards)
        for i in range(len(lines)-1, 0, -1):
            if lines[i].startswith("*** END OF THIS PROJECT GUTENBERG EBOOK"):
                del lines[i:]
                break

        # Clean up remaining lines
        for l in lines:
            # Skip empty lines
            if l == "\n":
                continue
            else:
                # Remove whitespace at start and end of line
                strip_line = l.strip()

                # Split line based on spaces and add words to text list
                text.extend(strip_line.split())

    return text


if __name__ == "__main__":

    # Get filename from user at command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    # Process file into words
    in_data = read_file(filename)

    # Use those words to build a trigrams dictionary
    in_words = make_trigrams(in_data)

    # Use dictionary to make new text
    new_text = use_trigrams(in_words)

    # Print new text
    print(new_text)
