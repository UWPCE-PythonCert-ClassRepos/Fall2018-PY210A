"""
trigrams
"""
import random
import pathlib
import string

words = "I wish I may I wish I might".split()
punctuations = set(['.', '?', '!', ',', '\n', '"', '(', ')'])
ending_punctuations = set(['.', '?', '!'])

def make_trigrams(words):
    tris = {}
    for i in range(len(words) - 2):
        tris.setdefault((words[i], words[i + 1]), []).append(words[i + 2])
    return tris

def build_text(word_pairs):
    iterations = 0
    current = None
    has_punctuation = 0
    max_sentences_per_paragraph = 5
    max_iterations = 500
    #Only start paragraphs with items that don't have punctuation
    keys_choice = [key for key in word_pairs if set(key).isdisjoint(punctuations)]
    output = []
    while iterations < max_iterations:
        iterations += 1
        
        if has_punctuation > max_sentences_per_paragraph or current not in word_pairs:
            #start a new pararaph if there are no third words or max sentences reached
            if current is not None:
                output.append('\n\n')
                has_punctuation = 0
            current = random.choice(keys_choice)
            output.extend([current[0].capitalize(), current[1]])
        
        output.append(random.choice(word_pairs[current]))
        current = tuple(output[-2:])
        if current[1] in ending_punctuations:
            has_punctuation += 1
    
    text = ' '.join(output)
    #remove space before punctuations
    for punctuation in punctuations:
        text = text.replace(f" {punctuation}", punctuation)
    return text

def read_file(path):
    text = []
    with open(path, 'r') as f:
        for line in f:
            text.append(line.replace('\r', ''))
    return text

def process_text(text_list):
    processed = []
    process = False
    for line in text_list:
        if process is True and 'End of the Project Gutenberg EBook' in line:
            break
        if process is False and '*** START OF THIS PROJECT GUTENBERG EBOOK' in line:
            process = True
            continue
        if len(line) == 0 or line.isupper():
            continue        
        processed.append(line)

    text = ' '.join(processed)
    for punctuation in punctuations:
        text = text.replace(punctuation, f" {punctuation}")
    return text.split()

if __name__ == '__main__':
    directory = pathlib.Path("/uw/python/projects/IntroToPython/files/").absolute()
    text_list = read_file(directory / "sherlock.txt")
    text = process_text(text_list)
    trigrams = make_trigrams(text)
    print(build_text(trigrams))
