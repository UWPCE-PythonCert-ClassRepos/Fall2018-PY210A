# Lesson 04 Exercise: File Exercise

# File reading and parsing
# Write a program that takes a student list and returns a list of all the programming languages used
# Keep track of how many students specified each language
# It has a header line and the rest of the lines are: Last, First: Nicknames, languages


def get_lines(my_file):
    """
    Returns formatted lines using a text file
    :param my_file: a text file
    :return: list of lines with endings stripped, commas replaced with empty strings, and header removed
    """
    with open(my_file, "r") as infile:
        lines = infile.readlines()
        strip_lines = [l.strip() for l in lines]
        words = [l.replace(",", "") for l in strip_lines]
        del words[0]
    return words


def stuff_after_colon(lines):
    """
    Returns a list of split lines
    :param lines: list of formatted lines that contain a colon
    :return: list of lines with only the text after the colon
    """
    stuff = []

    for x in lines:
        try:
            langs = x.split(": ")[1]
            stuff.append(langs)
        except IndexError:
            pass
    return stuff


def print_dictionary(my_dict):
    """
    Prints the dictionary contents using a formatted string
    :param my_dict: dictionary with language as the key and number of students as the value
    :return: an alphabetized, formatted list of computer languages and number of students
    """
    print("Computer Languages Used by Students")

    for key in sorted(my_dict.keys()):
        print("{}: {}".format(key.capitalize(), my_dict[key]))


def get_languages(filename):
    languages = {}

    strip_lines = get_lines(filename)
    stuff = stuff_after_colon(strip_lines)

    for lines in stuff:
        for item in lines.split():
            if item == "nothing" or item[0].isupper():
                continue
            else:
                if item in languages:
                    languages[item] += 1
                else:
                    languages[item] = 1

    print_dictionary(languages)


if __name__ == "__main__":
    get_languages("students.txt")
