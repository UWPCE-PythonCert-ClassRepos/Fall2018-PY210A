#!/usr/bin/env Python3

"""Date: November 6, 2018
   Created by: Carol Farris
   Name: File lab
   Goal: Learn file handling with Python
   Remaining work:
      manipulate the content in the file:
      take in one line at a time as a long string
      split the file in two by colons
      make everything lowercase
      next, split the sub string by tabs
"""
import os
OUT_PATH = "practice_file_writing"


def send_file_to_disk(myfile):
    """
    Accepts test file and writes to disk
    :param (myfile):
    :return: none. Will send file to directory set in outpath.
    """
    prepare_to_write_to_disk()
    os.chdir(OUT_PATH)
    with open('practiceFile.txt', 'w') as outfile:
        outfile.write(myfile)


def prepare_to_write_to_disk():
    """
    Check OUT_PATH specified is a directory, if not, it will make it

    """
    if not os.path.isdir(OUT_PATH):
        os.mkdir(OUT_PATH)


def sendtoconsole(newdoc):
    """
    accepts a text document and prints to console
    :param: newdoc -- text document to print
    :return: none
    """
    print("from newdoc")
    print(newdoc)


def examinefile(myfile):
    """
    Opens up file and prints each line to terminal
    :param: myfile  -- file to open
    :return: newdoc variable containing text content sent
             to sendtoconsole(newdoc)
    """
    newdoc = ""
    with open('students.txt', 'r') as f:
        while True:
            eachLine = f.readline()
            if not eachLine:  # if there is no line
                break
            newdoc += eachLine
            # print(eachLine)
    f.closed
    send_file_to_disk(newdoc)
    return sendtoconsole(newdoc)


if __name__ == '__main__':
    newdoc = ''
    examinefile('students.txt')
    #  sendtoconsole(newdoc)
