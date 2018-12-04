# Lesson 04 Exercise: File Exercise

# Paths
# Write a program that prints the full path for all files in the current directory, one per line
import os


def file_lister():
    # Current directory
    current_dir = os.getcwd()

    # Files in folder
    files = os.listdir(current_dir)

    # Join directory with filenames
    for file in files:
        print(os.path.join(current_dir, file))


file_lister()
