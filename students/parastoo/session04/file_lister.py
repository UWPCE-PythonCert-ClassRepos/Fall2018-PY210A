#!/usr/bin/env python3


'''Write a program which prints the full path for all files in the
current directory, one per line'''

import os
import pathlib


print('\n'.join([os.path.abspath(f) for f in os.listdir(os.curdir)]))

'''Write a program which copies a file from a source, to a destination
(without using shutil, or the OS copy command)'''

def copy_file(sourceFileName, destFileName):
    #open file 'SourceFileName' for reading as binary
    sourceFile = open(sourceFileName, 'rb')
    data = sourceFile.read(1000)
    sourceFile.close()

    #create file destFileName for the writing as binary
    destFile = open(destFileName, 'wb')
    destFile.write(data)
    destFile.close()
    print('Done')

################
'''Write a little script that reads that file, and genrates a list of all
the languages that have been used'''

with open('students.txt', 'r') as infile:
    with open('STU02', 'w') as outfile:
        header = infile.readlines(1)
        del header
        lines = infile.readlines()
        s = set()
        for line in lines:
            lan = line.strip().split(': ')[1]
            item_lan = lan.split(', ')
            for item in lan:
                s.add(item)
        outfile.write('\n'.join(s))






#if __name__ == '__main__':

    #copy_file('dict_lab.txt', 'test.txt')




