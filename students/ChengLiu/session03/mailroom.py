#!/usr/bin/env python3

"""
PY210A-Session03
Cheng Liu
Mailroom Part 1
"""

import os


OUT_PATH = "thank_you_letters"


def prepare_to_run():
    if not os.path.isdir():
        os.mkdir(OUT_PATH)


donors = [("Fred Jones", [100, 200, 300]), ("Amy Shume", [2000, 1000, 3000])]


def find_donor(name):
    """
    finds if a donor is in the donor db
    :param name: name of donor to find
    : returns: the donor tuple if found, or None if not
    """
    for donor in donors:
        if name.lower() == donor[0].lower():
            return donor
    return None


def thank_you():
    print("Do the Tahnk_you function here")

    filename = os.path.join("folders", filename)



def report():
    print("Do the report function here")


def menu_selection(prompt, dispatch_dict):



def main():
    print("Welcome to Mailroom!")
    answer = ""
    while answer != "q":
        print("Please select from the following:")
        print("Quit: 'q'"
              "\nThank you: 't'"
              "\nReport: 'r'"
              )
        answer = input("=> ")
        answer = answer.strip()  # in case entering the space at the beginning
        answer = answer[0:1].lower()  # in case only enter key, no values
        if answer == "t":
            thank_you()
        elif answer == "r":
            report()


if __name__ == "__main__":
    # main()
    prepare_to_run()
    assert find_donor("Fred Jones") is not None
    assert find_donor("Bob Jones") is not None
    assert find_donor("Fred jones") is not None
