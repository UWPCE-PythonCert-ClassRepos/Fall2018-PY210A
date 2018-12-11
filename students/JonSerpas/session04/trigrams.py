'''
trigrams
'''
import random


words = "I wish I may I wish I might".split()

infile = open("sherlock.txt", "r")
textfile = infile.readlines()
infile.close()
textfile = [i.split() for i in textfile]
textfile = [i for item in textfile for i in item]


def build_trigrams(words):
    trigrams = {}
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if pair in trigrams:
            trigrams[(pair)].append(follower)
        else:
            trigrams[(pair)] = [follower]
    return(trigrams)


def story_builder(tris, max_words=32):
    new_text = []
    starting_index = random.choice(list(tris.keys()))
    new_text.extend([starting_index[0], starting_index[1],
                     random.choice(tris[starting_index])])
    print(' '.join(new_text))
    # now we have our first 3 words; let's generate the rest of the text

    while len(new_text) != random.randrange(2, max_words):
        new_word = tuple(new_text[-2:])
        if new_word in list(tris.keys()):
            type(random.choice(tris[new_word]))  # stuck here. no clue
            new_text.append(random.choice(tris[new_word]))
        else:
            print(new_word, "not in tris")
            new_text.extend(random.choice(list(tris.keys())))

    print(' '.join(new_text))


if __name__ == '__main__':
    tris = build_trigrams(textfile)

    story_builder(tris, 3000)
