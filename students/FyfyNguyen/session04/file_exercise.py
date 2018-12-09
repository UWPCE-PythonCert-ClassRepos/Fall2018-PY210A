#!/usr/bin/env python3

"""
File Exercise
"""

# Print the full path for all files in the cwd, one per line
import os
import pathlib

for filename in os.listdir(os.curdir):
    print(os.path.abspath(filename))

# Copy a file from a source to a destination (without using shutil, or the OS copy command)
with open(source, 'rb') as infile, open(destination, 'wb') as outfile:
    outfile.write(infile.read())

# Make it work for any size file: i.e. don't read the entire
# contents of the file into memory at once


# Open files in binary mode:


# Test with both text and binary files
