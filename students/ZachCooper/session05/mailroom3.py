#!usr/bin/env python3

from textwrap import dedent
import math
import os


# Name letters will be under in disk
OUT_PATH = "thank_you_letters"


# Creates path to open cwd for letters
def prepare_to_run():
    if not os.path.isdir(OUT_PATH):
        os.mkdir(OUT_PATH)


# Donors db which is changed to a dict in main
def disney_donor_db():
    return {'yosemite sam': ("Yosemite Sam", [100.56, 200.23, 300]),
            'yogi bear': ("Yogi Bear", [2000.33, 4000, 1000]),
            'daffey duck': ("Daffey Duck", [5000.24, 10000.34, 30000]),
            'wile e. coyote': ("Wile E. Coyote", [300.40, 1000, 750.17]),
            'bugs bunny': ("Bugs Bunny", [100000.87, 50000, 100]),
            'mickey mouse': ("Mickey Mouse", [1345.67, 345.78, 1.23]),
            }


# Runs main menu function
def menu_selection(prompt, dispatch_dict):
    # Really like the menu dict option using switches
    while True:
        response = input(prompt)
        response = response[:1].lower()
        if dispatch_dict.get(response, unknown)() == "exit menu":
            break


# First item function in menu
def thank_you():
    while True:
        name = input("Enter a donor's name or 'list' to see all donors or "
                     "'menu' to exit to main menu\n").strip()
        if name == "list":
            print(donor_names())
        elif name == "menu":
            return
        else:
            take_donation(name)


def sort_key(item):
    return item[1]


# Second item function in menu
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


def find_donor(name):
    # Strip and lower to counter users entry errors
    key = name.strip().lower()
    return donors.get(key)


# Third item in menu that returns donor names
def print_donors_donations():
    print("Donor name list and donations:\n")
    # Return donor name along with donation history
    for donor, value in donors.items():
        print(value)


def donor_names():
    print("Donor Name:")
    # Returns only donor names
    for donor in donors:
        print(donor)


# Use to see if donor exists in dictionary
def donor_in_dict():
    don_name = input("Enter a name to see if it exits in donor dictionary:")
    if don_name.lower() in donors:
        print("{} is a current donor\n".format(don_name))
    else:
        if don_name not in donors:
            print("{} is not a current donor, please return to menu to start donation"
                  " process as new donor\n".format(don_name))
        return


# Possible menu selection
# Currently being used in another function
def new_donor(name):
        name = name.strip()
        donor = (name, [])
        donors[name] = donor  
        return donor


def take_donation(name):
    while True:
        donation = input("Enter a donation amount (or 'menu' to exit)> ").strip()
        if donation == "menu":
            return
        # Make sure amount is a valid amount
        try:
            amount = float(donation)
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                raise ValueError
        # raise and exception for amount if it doesnt pass
        except ValueError:
            print("error: donation amount is invalid\n")
        else:
            break

    # If donor is not recurring, create new donor
    donor = find_donor(name)
    if donor is None:
        donor = new_donor(name)

    # Append the donation
    donor[1].append(amount)
    # Send a thank you letter for the donation to the donor
    print(send_letter(donor))


def send_letter(donor):
    # Use format to add donor name and donated amount into letter
    # Original thank you letter script
    return dedent('''Dear {0:s},

              Thank you for your very kind donation of ${1:.2f}.
              It will be put to very good use.

                             Sincerely,
                                -The Team\n
              '''.format(donor[0], donor[1][-1]))
    # Use comprehension to shorten???
    # d = {'d_name': donor[0], 'd_dollar': donor[1][-1]}
    # return ("Dear {d_name},\n\n    Thank you for your very kind "
    #        "donation of ${d_dollar}.\n    It will be put to very good use.\n\nSincerely,\n-The Team".format(**d))


def sub_menu():
    menu_selection(sub_prompt, sub_dispatch)


def send_letters_to_disk():
    """
    make a letter for each donor, and save it to disk.
    """
    for donor in donors.values():
        letter = send_letter(donor)
        filename = donor[0].replace(" ", "_") + ".txt"
        print("writing letter to:", donor[0])
        filename = os.path.join(OUT_PATH, filename)
        open(filename, 'w').write(letter)


main_prompt = ("Welcome to Zach's MailRoom!\n"
               
               "What would you like to do:\n"
               "'t' - Send a Thank You\n"
               "'r' - Create a Donor Report\n"
               "'f' - Find a donor\n"
               "'d' - List of donors and donations\n"
               "'s' - Send letters to every donor\n"
               #"ln' - List of just donor names\n"
               #"'n' - Add new donor\n" 
               #"'m' - Make another donation\n" 
               "'b' - Enter into Sub Menu selections\n"
               "'q' - Quit\n"
               "=>")

main_dispatch = {"t": thank_you,
                 "r": donor_report,
                 "f": donor_in_dict,
                 "d": print_donors_donations,
                 "s": send_letters_to_disk,
                 #"ln": donor_names,
                 #"n": new_donor,
                 #"m": take_donation,
                 "b": sub_menu,
                 "q": func_q
                }

def func_q():
    print("Quitting the menu now.")
    return "exit menu"


def unknown():
    print("that was not a valid response")
    return None


# Modify this into a sub menu similar to main prompt
sub_prompt = ("\nYou are in a sub-menu now\n"
              "What do you want to do?\n"
              "Type t, r, d, main for main menu, or q to exit >>"
              )

sub_dispatch = {"t": thank_you,
                "r": donor_report,
                "f": donor_in_dict,
                "d": print_donors_donations,
                "q": func_q,
                "main": main_prompt
        }


if __name__ == "__main__":

    donors = disney_donor_db()

    menu_selection(main_prompt, main_dispatch)
    print(donors)
