import sys
import random


def build_trigrams(words):
    tris = {}

    for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
        # print(w1, w2, w3)

        pair = (w1, w2)

        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[(w1, w2)] = [w3]

    # print(tris)
    return tris


def use_trigrams(words):

    return_ouput = []

    for x in range(30):

        build_output = list(random.choice(list(words.keys())))

        for y in range(4, 10):
            next_pair = tuple(build_output[-2:])
            # print(f'next pair {next_pair}')

            if next_pair in words:
                build_output.append(random.choice(words[next_pair]))
            else:
                build_output.append(".")

                next_pair2 = list(random.choice(list(words.keys())))
                build_output.append(random.choice(words[next_pair2]))

        build_output[-1] += '.'
        build_output[0] = build_output[0].capitalize()

        return_ouput.extend(build_output)

    return " ".join(return_ouput)


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


if __name__ == "__main__":

    file_contents = []

    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    with open(filename, 'r') as myfile:
        data2 = myfile.read().split()

    # create trigams
    trigrams_output = build_trigrams(data2)

    # print output of use_trigrams
    print(use_trigrams(trigrams_output))