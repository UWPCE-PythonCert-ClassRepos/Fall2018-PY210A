# Lesson 04 Exercise: Trigrams
import sys
import random


# Make a dictionary with the first two words as the key and the third word as the value
def make_trigrams(words):
    tris = {}

    for i in range(len(words)-2):
        pair = words[i:i+2]
        follower = words[i+2]

        # Convert to a tuple
        pair = (pair[0], pair[1])

        # If in dictionary, append value, otherwise add it
        if pair in tris:
            tris[pair].append(follower)
        else:
            tris[pair] = [follower]
    return tris


# Get random word from dictionary
def get_random_word(d):
    word = random.choice(list(d.keys()))
    return word


# Use dictionary to build new text
def use_trigrams(d):
    start = get_random_word(d)

    alternate_word = ""

    text_words = [start[0], start[1]]

    while len(text_words) < 250:
        pair = (text_words[-2], text_words[-1])

        if pair in d:
            text_words.append(random.choice(list(d[pair])))

        else:
            while pair not in d:
                alternate_word = get_random_word(d)

            text_words.append([alternate_word[0], [alternate_word[1]]])

    text_words[0] = text_words[0].capitalize()
    final_text = " ".join(text_words) + "!"
    return final_text


# Open text file and read in contents
def read_file(file):
    with open(file, "r") as f:
        text = []

        lines = f.readlines()

        for l in lines:
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

    use_trigrams(in_words)

    # Use dictionary to make new text
    new_text = use_trigrams(in_words)

    # Print new text
    print(new_text)
