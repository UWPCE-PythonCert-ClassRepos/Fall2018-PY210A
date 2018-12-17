#!/usr/bin/env python3

def copy_file():
    with open('students.txt', 'r') as infile:
        with open('STU02', 'w') as outfile:
            header_elimination(infile) #eliminates header
            lines = infile.readlines()
            s = set()
            for line in lines:
                ini_set = nickname_ini(line)
                lan = line.strip().split(': ')[1]
                item_lan = lan.split(', ')
                for item in lan:
                    if item in ini_set:
                        del item
                    else:
                        s.add(item)
            outfile.write('\n'.join(s))


def header_elimination(infile):
    header = infile.readlines(1)
    del header
    return infile


def nickname_ini(line):
    name_string = line.strip().split(': ')[0]
    first_name = name_string.split(', ')[1]
    nickname_ini = set()
    for item in first_name:
        nickname_ini.add(item[0:2])
    return nickname_ini

if __name__ == '__main__':

    copy_file()