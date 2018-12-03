import random
import requests
from bs4 import BeautifulSoup


def get_text(url):
    """
    Get text data from url of gutenberg project so as to not have it within
    code
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    text = soup.find_all("p")
    texter = [i.text for i in text]
    words = "".join(texter).split()
    # Pass parsed words of book in list form to trigram dictionary maker
    make_trigrams(words)


def make_trigrams(words):
    """
    Build trigrams, keys as two words and values as possible next words
    """
    tris = {}
    for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
        if (w1, w2) not in tris:
            tris[(w1, w2)] = [w3]
        else:
            tris[(w1, w2)].append(w3)
    # Pass tris dictionary and words list to random text generator
    random_text(tris, words)


def random_text(tris, words):
    """
    Select tris dictionary key to start sequence if first letter is
    capitalized.
    Iterate for approximate length of text and create tuples of last two words.
    Add values of tuples that are in tris dictionary, otherwise append random
    word.
    """
    while True:
        new_text = list(random.choice(list(tris.keys())))
        if new_text[0][0].isupper():
            break
        else:
            continue
    # Add random choice to the new text from list of tuple pair in dictionary
    # If exact match doesn't exist in dictionary, take second word and add
    # random choice from list of value with second tuple value
    for i in range(len(words)-2):
        last_two = tuple(new_text[-2:])
        try:
            new_text.append(random.choice(tris[last_two]))
        except KeyError:
            for i in tris:
                if last_two[1] == i[1]:
                    new_text.append(random.choice(tris[i]))
                else:
                    new_text.append(random.choice(new_text))

    print(" ".join(new_text))


if __name__ == "__main__":
    get_text("https://www.gutenberg.org/files/1497/1497-h/1497-h.htm")
