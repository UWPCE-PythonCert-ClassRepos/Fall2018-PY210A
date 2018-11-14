#!/usr/bin/env python3
import os
import pathlib
import collections


def main():
    pth = pathlib.Path('./')
    for f in pth.iterdir():
        print(f.absolute())

def cp_f(source, destination):
    #read file from source
    with open(source, 'rb') as f_source:
        read_data = f_source.read()
        f_source.closed
    print(read_data)
    #write file to destination
    with open(destination, 'wb') as f_out:
        f_out.write(read_data)
        f_out.closed
    #tackle memory buffer issues

def students():
    stu_data = set()
    d_stu = {}
    with open("./students.txt", 'r') as f_stu:
        stu_line = f_stu.readline().split()
        while True:
            stu_line = f_stu.readline().split()
            # stu_list = stu_line.split()
            if not stu_line:
                break
            for item in stu_line:
                if item.islower():
                    if "," in item:
                        item = item.replace(",", "")
                    if ":" in item:
                        item = item.replace(":", "")
                    if item in d_stu:
                        d_stu[item] = d_stu[item] + 1
                    else:
                        d_stu[item] = 1

            f_stu.closed
    print("Languages and count are the following:")
    for k, v in d_stu.items():
        print(k, v)


if __name__ == "__main__":
    #main()
    #cp_f("./source/copy_this.txt", "./destination/copied_file.txt")
    students()
