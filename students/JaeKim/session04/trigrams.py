import sys

# python trigrams.py c:\wish.txt

# wish.txt content:
#
# I wish I may I wish I might
#

def build_trigrams(words):
    tris = {}

    for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
        print(w1, w2, w3)

        pair = (w1, w2)

        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[(w1, w2)] = [w3]

    return tris


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    with open(filename, 'r') as myfile:
        data = myfile.read().split()

    print(build_trigrams(data))