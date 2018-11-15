import pathlib
from collections import defaultdict

def print_paths():
    pth = pathlib.Path('./')
    for f in pth.iterdir():
        print(pth.absolute() / f)

def copy_file(source_path, destination_path):
    with open(source_path, 'rb') as source_f, open(destination_path, 'wb+') as dest_f:
        for line in source_f:
            dest_f.write(line)

def unique_lang(file_path):
    langs = defaultdict(int)
    with open(file_path, 'r') as f:
        for line in f:
            for lang in line.split(':')[1].split(','):
                if lang.islower():
                    langs[lang.strip()] += 1
    return dict(langs)

if __name__ == "__main__":
    print_paths()
    directory = pathlib.Path("/uw/python/projects/IntroToPython/files/").absolute()
    copy_file(directory / "source_doc.txt", directory / "destination_doc.txt")
    copy_file(directory / "source.jpg", directory / "destination.jpg")
    print(unique_lang(directory / "students.txt"))