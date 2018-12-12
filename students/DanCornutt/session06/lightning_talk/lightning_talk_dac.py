#!usr/bin/env python3

import re

def find(pat, text):
    match = re.search(pat, text)
    if match:
        print(match.group())
    else:
        print("not found")

def find_all(pat, text):
    match = re.findall(pat, text)
    if match:
        print(match)
    else:
        print("not found")

def find_name():
    name = input("What name would you like to find? ").title()
    match = re.search(name, PAGE)
    print(match.group())
    print(match)

def read_f():
    with open('html2.txt', 'r') as f:
        page = f.read()
    f.closed
    # print(page)
    return page


def find_all_names(pat, PAGE):
    names = re.findall(r'center">[\w.]+</td>', PAGE)
    print(names.group())

PAGE = read_f()

if __name__ == "__main__":
    pass
    # read_f()
    # find_name()
