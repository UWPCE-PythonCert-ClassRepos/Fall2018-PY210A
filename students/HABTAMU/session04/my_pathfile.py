#!/usr/bin/env python3

# Write a program which prints the full path for all files in the current directory, one per line
import os
import pathlib

def my_path():
    my_pth = pathlib.Path('./')
    my_dir = os.getcwd()
    for my_file in my_pth.iterdir():
        print(os.path.join(my_dir,my_file))
my_path()
