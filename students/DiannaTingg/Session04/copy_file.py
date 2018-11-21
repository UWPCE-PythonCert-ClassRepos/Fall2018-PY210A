# Lesson 04 Exercise: File Exercise

import sys

# File Processing
# Write a program that copies a file from a source to a destination (without using shutil, or the OS copy command)
# Make it work for any size file and for any kind of file (use binary mode)


def copy_file(original_file, new_file):
    buffer = 500
    with open(original_file, "rb") as infile, open(new_file, "wb") as outfile:
        while True:
            data = infile.read(buffer)
            if not data:
                break
            else:
                outfile.write(data)


if __name__ == "__main__":
    try:
        original = sys.argv[1]
        new = sys.argv[2]
        copy_file(original, new)

    except IndexError:
        print("You enter a source filename and a destination filename.")
        sys.exit(1)
