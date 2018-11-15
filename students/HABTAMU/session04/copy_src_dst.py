#!/usr/bin/env python3

# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).

def copy_src2dst():
    with open('my_src.txt', 'rb') as infile, open('my_dest.txt', 'wb') as outfile:
        outfile.write(infile.read())

copy_src2dst()