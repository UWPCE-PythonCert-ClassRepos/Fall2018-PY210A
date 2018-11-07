#!/user/bin/env python
import os

def copy_file(file):
    outfile = open('destination/' + file, 'wb')
    x = 1
    for line in open('source/' + file, 'rb'):
        print(x)
        x += 1
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
    program_dict = {}
    program_set = set()
    for line in students:
        for record in line.split(':')[1].strip('\n').split(','):
            if record and record == record.lower() and not record.strip() == 'languages':
                program_value = record.strip()
                if program_value in program_set:
                    program_dict[program_value] += 1
                else:
                    program_dict[program_value] = 1
                    program_set.add(program_value)
    for p in program_set:
        print(p + " " + str(program_dict[p]))


if __name__ == '__main__':
    file_ex()
    file_parse()
