import os
def print_path():
    cwd = os.getcwd()

    for file in os.listdir(cwd):
        print(os.path.abspath(file))

def copy_file(src,dst,buffer_size=1024*1024):
    'copy file buffer by buffer'
    while True:
        buff = src.read(buffer_size)
        if not buff:
            break
        dst.write(buff)

def student():
    lan_set = set()
    with open('students.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines.pop(0)
    for line in lines:
        lan_set.update(line.split(':')[1].split(','))
    lan_set.remove('')
    return lan_set

def main():
    filename = input("filename for move: ")
    src = open(filename, 'rb')
    destination = input("destination for move: ")
    dst = open(destination, 'wb')

    print_path()
    copy_file(src,dst)
    src.close()
    dst.close()
    print(student())

if __name__ == "__main__":
    main()
