#!/usr/bin/env python3


"""
This program contains all of the user input and print statements that accompany the donor_modules.py program as part of the mailroom_oo python package.
"""

# import relevant dictionaries
import os
import sys
import math
from textwrap import dedent


# name of folder in which to store thank you letters to donors
OUT_PATH = "thank_you_letters"


def prepare_to_run():
    """checks if folder in which to store thank you letter files exists, if not, creates new folder"""
    if not os.path.isdir(OUT_PATH):
        os.mkdir(OUT_PATH)


def quit():
    """quits the program"""
    sys.exit(0)



def menu_selection():
    '''main function to run the menus from'''
    user_selection = input(dedent('''
          Hello! Please tell us what you'd like to do:
          1 - Send a Thank You
          2 - Create a Report
          3 - Send Letters to All Donors
          4 - Quit
          > '''))
    return user_selection.strip()


def create_report():
    """creates a report of all previous donors and their donations"""
    report = []
    report.append("{:<20}{:5}{:5}{}".format("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"))
    report.append("{:-<60}".format(""))
    for donor_name, gifts in donors.items():
        total = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total / num_gifts
        report.append("{:<22} ${:<13.2f} {:<10} ${:.2f}".format(donor_name, total, num_gifts, avg_gift))
    return "\n".join(report)


def email(donor_name, donation_amount):
    """creates individual thank-you email for a new donation"""
    message = ("\n\nDear {},"
               "\n\nThanks for your money! Your donation of ${:.2f} will be summarily used to buy me beer.\n\n"
               "Kind regards,\nKate Koehn").format(donor_name, donation_amount)
    file_name = "{}.txt".format(donor_name)
    with open(file_name, "w") as f:
        f.write(message)


def generate_letter(donor_name, donation_amount):
    """generates a thank you letter for the donation made"""
    return dedent('''Dear {!s:s},

    Thank you for your crappy donation of ${:.2f}. It will be used to buy the cheapest beer possible, because you couldn't donate enough for us to buy anything decent. We'll be lucky if we get Natty Ice.

    Cheers,
        Kate Koehn
    '''.format(donor_name, donation_amount))



def record_new_donation(donor_name):
    """prompts user for a new donation amount and store it in the donor dict"""
    while True:
        donation = input("Please enter the donation amount or type 'menu' to return to the main menu: ").strip()

        if donation == "menu":
            return
        try:
            donation = check_donation(donation)
        except ValueError:
            print("You have tried to donate an invalid amount. Please try again.\n")
        else:
            break

    # check if donor already exists in donors dict, if not, append name and donation
    add_new_donor(donor_name)
    add_donation_to_donor(donor_name, donation)
    email(donor_name, donation)



def thanks():
    """sub-menu to record a new donation and thank the user for their donation"""
    while True:
        print("\n\n~ Thanking Your Donors ~\n")
        donor_name = input("Enter a donor's name or 'list' to see all donors or 'menu' to exit to main menu: ").strip()

        if donor_name == "list":
            for name in donors:
                print(name)
        elif donor_name == "menu":
            return
        else:
            record_new_donation(donor_name)


def write_letters_to_disk():
    """make a letter for each donor, and save it to disk."""
    for donor, donations in donors.items():
        letter = generate_letter(donor, sum(donations))
        filename = donor.replace(" ", "_") + ".txt"
        print("Your letter has been written to:", donor)
        filename = os.path.join(OUT_PATH, filename)
        open(filename, 'w').write(letter)




if __name__ == "__main__":

    donors = get_sample_donors()

    prepare_to_run()

    selection_dict = {"1": thanks,
                      "2": create_report,
                      "3": write_letters_to_disk,
                      "4": quit}
    while True:
        selection = menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("The selection you have made is not valid. You are the worst.")
