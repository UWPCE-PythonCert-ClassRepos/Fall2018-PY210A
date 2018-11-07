#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr)
Date: 11/05/2018

    Write a program which prints the full path for all files in the current directory, one per line
    Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
        Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
        This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb')
        (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for
        binary files.
        Test it with both text and binary files (maybe jpeg or something of your choosing).

"""

import os

#list full path name for files in the cwd
cwd = os.getcwd()
files = os.listdir(cwd)

for file in files:
    print(cwd + '\\' + file)


#copy file
ori_file = 'students.txt'
src_file = open(ori_file, 'r')
lines = src_file.readlines()

fin_file = 'students_copy.txt'
des_file = open(fin_file, 'w')
for line in lines:
    #line = line.strip()
    des_file.write(line)

des_file.close()


ori_file = 'students.txt'
src_file = open(ori_file, 'r')
lines = src_file.readori_file = 'students.txt'
src_file = open(ori_file, 'r')
lines = src_file.readlines()

counts = dict()
for line in lines:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

for key, val in counts.items():
    print(key, val)

#todo need to determine how to remove the names and nicknames