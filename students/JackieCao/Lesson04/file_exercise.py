#!/usr/bin/env python3
"""
File Exercise
"""

import os
from os import listdir

# Write a program which prints the full path for all files in the current directory, one per line
files = [f for f in os.listdir('.') if os.path.isfile(f)]

for i in files:
    print(i)

# Write a program which copies a file from a source, to a destination

def read_file(in_file, chunk_size = 1000):
    with open(in_file, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

def copy_file(in_file):
    with open('copy_'+in_file, 'ab') as f:
        for i in read_file(in_file):
            f.write(i)
copy_file('sherlock_small.txt')
copy_file('binary.dat')

# File reading and parsing

students = open('students.txt').readlines()

del students[0]

lan = [line.split(":")[1] for line in students]        
lan = [line.strip() for line in lan]

lan = [line for line in lan if line]
l = []
for i in lan:
    i = i.split(', ')
    l = l+i
l = [line.strip() for line in l]
l = [line for line in l if line]
l.remove('nothing')
l.remove('Chuck c++')
l = list(set(l))
print(l)

























