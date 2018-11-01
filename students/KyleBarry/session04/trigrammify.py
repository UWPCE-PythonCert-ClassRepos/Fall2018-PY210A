words = "I wish I may I wish I might"

words = words.split()

def make_trigrams(words):
    tris = {}
    #for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
        tris[(w1, w2)] = w3
