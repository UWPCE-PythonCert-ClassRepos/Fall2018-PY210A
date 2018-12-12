#!/usr/bin/env python3

"""
Mailroom 2
"""
import os
import sys
import tempfile
import pathlib
from textwrap import dedent

donor_db = {"Robyn Rihanna": [100, 200, 300],
            "Ariana Grande": [2250, 4000, 1000],
            "Beyonce Carter-Knowles": [150000, 3500, 25000],
            "Aubrey Drake Graham": [15000, 5500.25, 1200],
            "Justin Bieber": [2500, 250, 750.50]
            }

file_dir = pathlib.Path(tempfile.gettempdir())


def print_donors():
    for donor in donor_db:
        print(donor)


def find_donor(name_entered):
    donor_key = name_entered.strip().title()
    return donor_db.get(donor_key)


def add_donor(name_entered):
    donor = (name_entered.title(), [])
    donor_db[name_entered.title()] = donor
    print("Successfully added new donor to database.")
    add_donation(name_entered)
    return donor

def add_donation(name_entered):
    donation = float(input("Enter donation amount >>> "))
    donor = (name_entered.title(), [])
    donor[1].append(donation)
    print("Successfully updated donation amount.")

    send_thank_you(name_entered, donation)


def confirm_donor(name_entered):
    response = input(f"Donor does not exist. Add {name_entered.title()} to "
                     "database? [y/n?] >>> ")
    if response == 'y':
        add_donor(name_entered)
    else:
        main_menu()


def send_thank_you(name_entered, donation):
    print(dedent("""
        Dear {},

            Your generous ${:,.2f} donation just made our day!

                Thank you!
                -The Charity""".format(name_entered.title(), donation)
                 ))


def thank_you():
    while True:
        name_entered = input("Enter the name of a donor or 'list' to view "
                             "donors >>> ").lower().strip()
        if name_entered == "list":
            print_donors()
        else:
            break

    donor = find_donor(name_entered)
    if donor is None:
        confirm_donor(name_entered)
    else:
        get_donor(name_entered)


def thank_you_all():
    pass


def sort_key(donors):
    return donor_db[1]


def create_report():
    print("{:30s} | {:11s} | {:9s} | {:12s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 72)
    donors.sort(key=sort_key, reverse=True)
    for donor in donors:
        print("{:30s}  $ {:11,.2f}  {:9d}  $ {:12,.2f}".format(
              donor[0], sum(donor[1]), len(donor[1]),
              sum(donor[1]) / len(donor[1])))


def exit_program():
    print("Exiting Program. Goodbye!")
    sys.exit()


def main_menu():
    selection = input(dedent("""
        Welcome to Mailroom!

        Select an option:

        1 - Create a Report
        2 - Send Thank You to a single donor
        3 - Send Thank You to all donors
        4 - Quit

        >>> """))
    return selection.strip()


def main():
    menu_selections = {"1": create_report,
                       "2": thank_you,
                       "3": thank_you_all,
                       "4": exit_program}

    while True:
        user_selection = main_menu()
        try:
            menu_selections[user_selection]()
        except KeyError:
            print("Error: Invalid Selection. Select from the main menu.")

if __name__ == "__main__":
    main()
