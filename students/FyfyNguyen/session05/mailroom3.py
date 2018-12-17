#!/usr/bin/env python3

"""
Mailroom 2
"""

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
    """
    Prints a list of exiting donors in donor_db
    """
    for donor in donor_db:
        print(donor)


def find_donor(name_entered):
    """
    Lookup donor in donor_db

    :param: the name of the donor
    :returns: the donor data structure -- None if donor not found in donor_db
    """
    donor_key = name_entered.strip().title()
    return donor_db.get(donor_key)


def add_donor(name_entered):
    """
    Add a new donor to donor_db

    :param: the name of the donor
    :returns: the new donor data structure
    """
    donor = (name_entered, [])
    donor_db[name_entered.title()] = []
    print("Successfully added new donor to database.")
    add_donation(name_entered)


def add_donation(name_entered):
    """
    Ask the user for donation amount and add it to donor_db

    :param: the name of the donor
    """
    donation = float(input("Enter donation amount >>> "))
    donor_db.setdefault(name_entered.title(), []).append(donation)
    print("Successfully updated donation amount.")
    send_thank_you(name_entered, donation)


def confirm_donor(name_entered):
    """
    Confirm the user wants to add a new donor to donor_db

    :param: the name of the donor
    """
    response = input(f"Donor does not exist. Add {name_entered.title()} to "
                     "database? [y/n?] >>> ")
    if response.strip() == 'y':
        add_donor(name_entered)
    else:
        main_menu()


def send_thank_you(name_entered, donation):
    """
    Generate a thank you letter to the donor

    :param: the name of the donor
    :param: the donation amount
    :returns:string with letter
    """
    return dedent("""Dear {},

            Your generous ${:,.2f} donation just made our day!

                Thank you!
                -Our Charity
        """.format(name_entered.title(), donation))


def thank_you():
    """
    Execute the logic to record a donation and generate a thank you message
    """
    while True:
        name_entered = input("Enter the name of a donor or 'list' to view "
                             "donors >>> ").lower().strip()
        if name_entered.strip() == "list":
            print_donors()
        else:
            break

    donor = find_donor(name_entered)
    if donor is None:
        confirm_donor(name_entered)
    else:
        add_donation(name_entered)


def thank_you_all():
    """
    Generate a letter for each donor and save it to temporary directory
    """
    for donor in donor_db:
        letters = send_thank_you(donor, donor_db[donor][-1])
        file_path = file_dir / (donor.replace(" ", "_") + ".txt")
        with open(file_path, 'w') as f:
            f.write(letters)
    print(f'Files downloaded to: {file_dir}')


def sort_key(donor):
    return donor


def create_report():
    """
    Generate report of donors and the amounts donated

    :returns: the donor report as a string
    """
    report_rows = []
    for name, donations in donor_db.items():
        total_given = sum(donations)
        num_gifts = len(donations)
        avg_gifts = total_given / num_gifts
        report_rows.append((name, num_gifts, num_gifts, avg_gifts))

    report_rows.sort(key=sort_key)
    report = []
    report.append("{:30s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                            "Total Given",
                                                            "Num Gifts",
                                                            "Average Gift"
                                                            ))
    report.append("-" * 72)
    for row in report_rows:
        report.append("{:30s} | {:11d} | {:9d} | ${:12,.2f}".format(*row))
    return "\n".join(report)


def print_report():
    print(create_report())


def exit_program():
    """
    Quit the program
    """
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
    menu_selections = {"1": print_report,
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
