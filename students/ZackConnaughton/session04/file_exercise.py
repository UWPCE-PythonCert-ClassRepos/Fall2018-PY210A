#!/user/bin/env python
import os

def copy_file(file):
    outfile = open('destination/' + file, 'wb')
    for line in open('source/' + file, 'rb'):
        outfile.write(line)
    outfile.close()

def file_ex():
    print(os.listdir())
    copy_file('document.txt')
    copy_file('pic.jpg')
    copy_file('mp.jpg')


def reset_destination():
    files = ('document.txt', 'pic.jpg', 'mp.jpg')
    for f in files:
        if os.path.exists('destination/' + f):
            os.remove('destination/' + f)


def file_parse():
    students = open('students.txt')
    print(students[0])
    for line in students:
        pass
        #print(line.split(':')[1].strip('\n').split(','))


if __name__ == '__main__':
    file_ex()
    file_parse()
