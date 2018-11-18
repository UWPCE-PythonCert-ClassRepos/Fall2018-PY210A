#!/usr/bin/env python3
from collections import Counter
"""
Find a list of names and programming languages they have used in the past.
Arguments:
    reads the file, 
Return:
    generates a list of all the languages that have been used.

Name: Nickname, languages
Swift, Taylor: python, java, perl
Swift, Samuel: Sam
Brooks, Garth: fortran, java, matlab, bash
"""

# all_langs = set()
# students_file = "students.txt"
# with open(students_file) as students:
#     students.readline()
#     for line in students:
#         langs = line.split(':')[1]
#         langs = langs.replace(',', ' ').replace('and', ' ').split()
#         # langs = langs.replace('and', ' ')
#         # langs = langs.split()
#         for lang in langs:
#             lang = lang.strip().capitalize()
#             if lang:
#                 all_langs.add(lang)
# for lang in all_langs:
#     print(lang)


all_langs = Counter()
infilename = "students.txt"
with open(infilename) as f:
    f.readline()  # read and toss the header

    for line in f:
        langs = line.partition(':')[2]  # get just what's after the colon
        # a bit of cleanup:
        langs = langs.replace(',', ' ').replace('and', ' ')
        langs = langs.split()  # separate the languages
        for lang in langs:
            if lang[0].isupper():  # there are some names in there!
                continue
            lang = lang.strip().capitalize()  # clean them up -- and make case the same
            if lang:  # don't want empty strings
                    all_langs[lang] += 1

print("And now the counted version")
for lang, count in all_langs.items():
    print(lang, ":", count)
