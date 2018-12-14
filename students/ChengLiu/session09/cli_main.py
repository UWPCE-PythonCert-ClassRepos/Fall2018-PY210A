#!/usr/bin/env python3

"""
Cheng Liu
Mail-room Final
"""


import sys
import math
import mailroom_final


def display_menu():
    print("\nWelcome to Mail-room!")
    print("Please select an option from the following:")
    print("1: Send Thank You"
          "\n2: Create Report"
          "\n3: Save to File"
          "\n4: Exit")
    selection = input("=> ")
    selection = selection.strip().lower()
    selection = selection[0:1]  # in case only enter key, no values
    return selection


def main():
    selection_dict = {"1": letter,
                 "2": report,
                 "3": send_letter_to_file,
                 "4": quit}

    while True:
        selection = display_menu()
        try:
            selection_dict[selection]()
        except KeyError:
            Print("Please select a valid option!")


if __name__ == "__main__":
    main()
