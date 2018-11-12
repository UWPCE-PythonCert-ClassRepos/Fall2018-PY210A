#!/usr/bin/env python3

"""
mailroom assignment
"""

# Mailroom Part 3

# import relevant dictionaries
import os
import sys
import math
from textwrap import dedent


# Dictionary of previous donors names and their donation amounts
donors = {"Rick Sanchez": [3.00, 1.00],
          "Liz Lemon": [4000.00, 3000.00, 6000.00],
          "Andy Dwyer": [10.00],
          "Brendan Small": [3.00, 10.00],
          "Coach McGuirk": [2.00, 1.00]}


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
    print("\n", "\n", "{:<20}{:5}{:5}{}".format("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"))
    print("{:-<60}".format(""))
    for donor_name, gifts in donors.items():
        total = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total / num_gifts
        print("{:<22} ${:<13.2f} {:<10} ${:.2f}".format(donor_name, total, num_gifts, avg_gift))



def email(donor_name, donation):
    """creates individual thank-you email for a new donation"""
    message = ("\n\nDear {},"
    "\n\nThanks for your money! Your donation of ${:.2f} will be summarily used to buy me beer.\n\n"
    "Kind regards,\nKate Koehn").format(donor_name, donation)
    file_name = "{}.txt".format(donor_name)
    with open(file_name, "w") as f:
        f.write(message)



def generate_letter(donor_name, donation):
    """generates a thank you letter for the donation made"""
    return dedent('''Dear {!s:s},
    
    Thank you for your crappy donation of ${:.2f}. It will be used to buy the cheapest beer possible, because you couldn't donate enough for us to buy anything decent. We'll be lucky if we get Natty Ice.
    
    Cheers,
        Kate Koehn
    '''.format(donor_name, donation))



def get_donor_key(donor_name):
    """looks up key in donor dict"""
    donor_key = donor_name.strip()
    return donors.get(donor_key)



def record_new_donation(donor_name):
    """prompts user for a new donation amount and store it in the donor dict"""
    while True:
        donation = input("Please enter the donation amount or type 'menu' to return to the main menu: ").strip()
        if donation == "menu":
            return
        try:
            donation_amount = float(donation)
            if math.isnan(donation_amount) or math.isinf(donation_amount) or round(donation_amount, 2) == 0.00:
                raise ValueError
        except ValueError:
            print("You have tried to donate an invalid amount. Please try again.\n")
        else:
            break

    #check if donor already exists in donors dict, if not, append name and donation
    name = get_donor_key(donor_name)
    if name is None:
        name = donor_name.strip()
        donor_name = (name, [])
        donors[name] = donor_name
        return donor_name

    donor_name[1].append(donation_amount)
    print(email(donor_name), donation_amount)



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
