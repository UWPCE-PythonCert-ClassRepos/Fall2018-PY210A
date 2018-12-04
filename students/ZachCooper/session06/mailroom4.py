#!/usr/bin/env python3

import os
import math
from textwrap import dedent

# Name letters will be under in disk
OUT_PATH = "thank_you_letters"


# Creates path to open cwd for letters
def prepare_to_run():
    if not os.path.isdir(OUT_PATH):
        os.mkdir(OUT_PATH)


# Donor and donations zipped into a dict
def disney_donor_db():
    donor_name = ["Yosemite Sam", "Yogi Bear", "Daffey Duck",
                  "Wile E. Coyote", "Bugs Bunny", "Mickey Mouse"]
    donation = [[100.56, 200.23, 300], [2000.33, 4000, 1000],
                [5000.24, 10000.34, 30000], [300.40, 1000, 750.17],
                [100000.87, 50000, 100], [1345.67, 345.78, 1.23]]
    return dict(zip(donor_name, donation))


# Function triggers main dispatch dict that
def menu_selection(prompt, dispatch_dict):
    # Really like the menu dict option using switches
    while True:
        response = input(prompt)
        response = response[:1].lower()
        if dispatch_dict.get(response, unknown)() == "exit menu":
            break


def list_donors():
    donor_names = list(donors)
    donor_names.insert(0, "Donor List:")
    return "\n".join(donor_names)


# Returns list_donors function above
def print_list_donors():
    print(list_donors())


def donor_donations():
    print("Donor name list and donations:\n")
    # Return donor name along with donation history
    for donor, value in donors.items():
        print(donor, value)


def get_donor_key(donor_name):
    """looks up key in donor dict"""
    donor_key = donor_name.strip()
    for key in donors.keys():
        if donor_key == key:
            return True
    return False


def add_new_donor(donor_name):
    name = donor_name.strip()
    if name not in donors.keys():
        donors[name] = []
    return donor_name


def add_donation_to_donor(donor_name, donation):
    donors[donor_name].append(donation)


def donor_in_dict():
    don_name = input("Enter a name to see if it exits in donor dictionary:")
    if don_name in donors:
        print("{} is a current donor\n".format(don_name))
    else:
        if don_name not in donors:
            print("{} is not a current donor,"
                  "please return to menu to start donation"
                  " process as new donor\n".format(don_name))
        return

# when a name is called in donor_in_dict,
# what happens if it is entered in lower case


def check_donation(donation):
    donation = float(donation)
    if math.isnan(donation) or math.isinf(donation) or round(donation, 2) <= 0.00:
        raise ValueError
    return donation


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

    # check if donor already exists in donors dict,
    # if not, append name and donation
    add_new_donor(donor_name)
    add_donation_to_donor(donor_name, donation)
    # email(donor_name, donation)
    print(send_letter(donor_name, donation))


def thank_you():
    while True:
        donor_name = input("Enter a donor's name or 'list' to see all donors or "
                           "'menu' to exit to main menu\n").strip()
        if donor_name == "list":
            for name in donors:
                print(name)
        elif donor_name == "menu":
            return
        else:
            record_new_donation(donor_name)


def sort_key(item):
    return item[1]


def donor_report():
    """Create donor report"""
    report_rows = []
    for (name, gifts) in donors.items():
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    report_rows.sort(key=sort_key)
    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 66)
    for row in report_rows:
        print("{:25s}   ${:11.2f}   {:9d}   ${:12.2f}".format(*row))


def send_letter(donor_name, donation):
    # Use format to add donor name and donated amount into letter
    # Original thank you letter script
    return dedent('''Dear {0:s},

              Thank you for your very kind donation of ${1:.2f}.
              It will be put to very good use.

                             Sincerely,
                                -The Team\n
              '''.format(donor_name, donation))


def send_letters_to_disk():
    """
    make a letter for each donor, and save it to disk.
    """
    for donor, donations in donors.items():
        letter = send_letter(donor, sum(donations))
        filename = donor.replace(" ", "_") + ".txt"
        print("Your letter has been written to:", donor)
        filename = os.path.join(OUT_PATH, filename)
        open(filename, 'w').write(letter)


main_prompt = ("Welcome to Zach's MailRoom!\n"

               "What would you like to do:\n"
               "'1' - Send a Thank You\n"
               "'2' - Create a Donor Report\n"
               "'3' - Find a donor\n"
               "'4' - List of donors and donations\n"
               "'5' - Send letters to every donor\n"
               "'6' - List of donor names\n"
               # "'7' - Add new donor\n" 
               # "'8' - Make another donation\n" 
               "'7' - Enter into Sub Menu selections\n"
               "'q' - Quit\n"
               "=>")


def end_program():
    print("Quitting the menu now.")
    return "exit menu"


def sub_menu():
    menu_selection(sub_prompt, sub_dispatch)


def unknown():
    print("that was not a valid response")
    return None


main_dispatch = {"1": thank_you,
                 "2": donor_report,
                 "3": donor_in_dict,
                 "4": donor_donations,
                 "5": send_letters_to_disk,
                 "6": print_list_donors,
                 # "7": new_donor,
                 # "8": take_donation,
                 "q": end_program,
                 "7": sub_menu,
                 }


# Modify this into a sub menu similar to main prompt
sub_prompt = ("\nYou are in a sub-menu now\n"
              "What do you want to do?\n"
              "'1' - Send a Thank You\n"
               "'2' - Create a Donor Report\n"
               "'3' - Find a donor\n"
               "'4' - List of donors and donations\n"
               "'5' - List of donor names\n"
               "'q'- Exit and Return to Main Menu\n"
              )

sub_dispatch = {"1": thank_you,
                "2": donor_report,
                "3": donor_in_dict,
                "4": donor_donations,
                "5": print_list_donors,
                "q": end_program,
                "main": menu_selection,
                }


if __name__ == "__main__":
    donors = disney_donor_db()

    menu_selection(main_prompt, main_dispatch)