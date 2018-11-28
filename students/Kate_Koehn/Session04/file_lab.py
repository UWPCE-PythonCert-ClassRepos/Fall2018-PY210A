#!/usr/bin/env python3

"""
File Exercise
"""

import os

#print the full path for all files in the current directory
for root, directory, files in os.walk('.'):
    for file in files:
        pwd = os.path.join(root, file)
        print(pwd)
        print(os.path.abspath(pwd))


with open("new_file", "wb+") as output, open('/Users/monster/Fall2018-PY210A/students/Kate_Koehn/Session04/sherlock.txt', 'rb') as input:
    contents = input.read()
    output.write(contents)



###go to the File Exercise assignment to download students.txt, Write a little script that reads that file, and generates a list of all the languages that have been used.

###What might be the best data structure to use to keep track of bunch of values without duplication?