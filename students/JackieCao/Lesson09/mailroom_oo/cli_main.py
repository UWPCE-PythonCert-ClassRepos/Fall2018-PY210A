#!/usr/bin/env python
"""
Command line interface for mailroom
"""

import sys
import math

from donor_models import Donor, DonorDB, get_sample_data

db = DonorDB(get_sample_data())

def print_donor_report():
    print(db.generate_donor_report())

def send_thank_you():
    while True:
        name = input("Enter a donor's name"
                     "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            print(db.list_donors())
        elif name == "menu":
            return
        else:
            break

    while True:
        amount_str = input("Enter a donation amount (or 'menu' to exit)> ").strip()
        if amount_str == "menu":
            return
        try:
            amount = float(amount_str)
        except ValueError:
            print("error: donation amount is invalid\n")
        else:
            break

    donor = db.add_donor(name)
    donor.add_donation(amount)
    print(db.gen_letter(donor))

def quit():
    sys.exit(0)

def main():
    selection_dict = {"1": send_thank_you,
                      "2": print_donor_report,
                      "3": db.save_letters_to_disk,
                      "4": quit}

    while True:
        selection = input(f"Choose an action:\n1 - Send a Thank You\n2 - Create a Report\n3 - Send letters to everyone\n4 - Quit")
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")

if __name__ == "__main__":
    main()
