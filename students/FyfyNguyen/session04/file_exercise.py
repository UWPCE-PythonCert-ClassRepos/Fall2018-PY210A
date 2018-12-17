#!/usr/bin/env python3

"""
File Exercise
"""

# Print the full path for all files in the cwd, one per line
import os
import pathlib

for filename in os.listdir(os.curdir):
    print(os.path.abspath(filename))

# Copy a file from a source to a destination (without using shutil,
# or the OS copy command)
with open(source, 'rb') as source_file, open(dest, 'wb') as dest_file:
    dest_file.write(source_file.read())

# Make it work for any size file: i.e. don't read the entire
# contents of the file into memory at once, break in chunks
CHUNKSIZE = 1000
with open(source, 'rb') as source_file, open(dest, 'wb') as dest_file:
    while True:
        data = source_file.read(CHUNKSIZE)
        if not data:
            break
        dest_file.write(data)

# Write script to generate list of languages students know
languages = set()
filename = "students.txt"
with open(filename, 'r') as f:
    f.readline()
    for line in f:
        langs = line.split(':')[1]
        langs = langs.replace(',', '')
        langs = langs.split()
        for lang in langs:
            if lang[0].isupper():
                continue
            lang = lang.strip().capitalize()
            if lang:
                languages.add(lang)
print(languages)
