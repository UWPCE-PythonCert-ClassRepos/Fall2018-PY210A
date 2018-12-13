#!/usr/bin/env python3
"""
command line interface
"""
from donor_models import *

def thank_to_all():
    dc.send_thank_to_all()
    list_of_donors = dc.list_donors
    print(f"The thank you letters for {list_of_donors} have been sent")

def make_report():
    data = dc.report_data
    # sort the data
    data.sort(key=lambda tup: tup[0])
    # format
    print("{:15s} | {:11s} | {:9s} | {:12s}".format(
          "Donor's Name", "Total Donated", "Number of Donations", "Average$"))
    for row in data:
        print("{:15s}   {:11.2f}   {:9d}   {:18.2f}".format(*row))

def thank_you():
    # ask user for donor's name
    while True:
        # add exception
        try:
            name = input("Enter a donor's name "
                        "(or 'list' to see all donors or 'menu' to exit)>")
        except (KeyboardInterrupt, EOFError):
            return None
        if name == "list":
            print(dc.list_donors)
        elif name == "menu":
            return
        else:
            break

    # ask user for donation amount
    while True:
        # add exception
        try:
            dollar = input("Enter a donation amount (or 'menu' to exit)>")
        except (KeyboardInterrupt, EOFError):
            return None
        if dollar == "menu":
            return
        # add exception
        try:
            dollar = float(dollar)
        except ValueError:
            print("Input must be a number")
        else:
            break

    donor = Donor(name)
    donor.add_donation(dollar)

    # add new name and donation amount to the donors history
    dc.add_donor(donor.name, donor.donations)
    # print the thank you letter
    d = donor.thank_you_data

    print("Dear {d_name},\n\n    Thank you for your donation of ${d_dollar}.\n\nBest,\nDonation Group".format(**d))

def main():
    print("hello")
    answer = ""
    while answer != "q":
        print("Please select from the following")
        print("Quit: 'q',\nSend a Thank You to a single donor : 't',\nReport: 'r',\nSend letters to all donors: 's'")
        try:
            answer = input(" => ")
        except (KeyboardInterrupt, EOFError):
            return None
        answer = answer.strip()
        answer = answer[:1].lower()
        if answer == 't':
            thank_you()
        elif answer == 'r':
            make_report()
        elif answer == 's':
            thank_to_all()

donors = {"Fred Jones":[100, 200, 300],
    "Amy Shumer": [10, 20],
    "Bean Shing": [20, 400],
    "Ann Shaw": [100, 400],
    "King May": [200, 400, 100, 100]
    }

if __name__ == "__main__":

    dc = DonorCollection()
    dc.add_old_donors(donors)
    main()

