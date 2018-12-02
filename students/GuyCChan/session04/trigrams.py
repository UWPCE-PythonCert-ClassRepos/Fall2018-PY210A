import string
import random

def read_in_data():
# Open text file and put file body in a list.
    with open('./sherlock_small.txt', 'rb') as file:
        file_body = file.readlines()
        allwords = []
        for line in file_body:
            line = line.strip()
            if line.endswith("in part my own."):
                break
            allwords.append(line)
# I'm doing it the beginner's way. Definitely not Pythonic.
        txt_words = ' '.join([str(word) for word in allwords])
        print(type(txt_words))
        # I struggled with this part for a long time, maybe a couple of days!.
        #NEED HELP HERE.
        # In line 16, txt_words is a str type. One line later, in line 21,
        # txt is a list! Why?
        txt = txt_words.lower().split(' ')
        print(type(txt), "here")
# Remove punctuations and make a long string of words from text.
        txt = txt.replace('"','')
        txt = txt.replace('--', ' ')
        txt = txt.replace(',', '')
        txt = txt.replace('\\n','')
        txt = txt.replace('(', '')
        txt = txt.replace(')', '')
        txt = txt.replace('.', '')
        txt = txt.replace('-', ' ')
        txt = txt.replace('\'', '')
        txt = txt.replace('[', '')
        txt = txt.replace(']', '')
        txt = txt.replace(' ', '')
        txt = txt.replace(' i ', ' I ')
        txt = txt.replace('holmes', 'Holmes')
        sp = " "
        full_txt = sp.join(txt)
        print(full_txt)
        return full_txt

def build_trigrams(full_txt):
# Make a dictionary using a for loop. This section is heavily Chris-"inspired".
# ipython sometimes would say "full_txt" is not defined. Why?
    full_txt = full_txt.split()
    word_pairs = {}
    for i in range(len(full_txt)-2):
        tw_wrds = tuple(full_txt[i:i + 2])
        thrd_wrd = full_txt[i + 2]
# Build a dictionary containing keys-tw_wrds, and values-thrd_wrd.
        if tw_wrds not in word_pairs:
            word_pairs[tw_wrds] = [thrd_wrd]
        else:
            word_pairs[tw_wrds].append(thrd_wrd)
    print(word_pairs)
    return word_pairs

def make_new_txt(word_pairs):
    # I outright plagiarized/stole from Chris for this section
    new_text = []
    for i in range(10):
        # I definitely can't write the next line so concisely.
        sentence = list(random.choice(list(word_pairs.keys())))
        # Add a random number of words to the sentence
        for j in range(random.randint(2, 12)):
            pair = tuple(sentence[-2:])  # the next word pair is the last two words
            sentence.append(random.choice(word_pairs[pair]))
        # Capitalize the first word:
        sentence[0] = sentence[0].capitalize()
        # Add the period
        sentence[-1] += "."
        new_text.extend(sentence)
        new_text = " ".join(new_text)
    print(new_text)
    return new_text


if __name__ == "__main__":
    full_txt = read_in_data()
    word_pairs = build_trigrams(full_txt)
    new_txt = make_new_txt(word_pairs)
