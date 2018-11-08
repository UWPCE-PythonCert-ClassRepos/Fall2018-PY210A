#!/usr/bin/env python3

"""
Mailroom Exercise -- as of Session 3 -- no dictionaries
#NOTE# significant volume of code utilized from 
Fall2018-PY210A/solutions/Lesson03/mailroom.py ##

"""

from textwrap import dedent
import math

donor_db = [("Jim Rockford", [325, 300, 125]),
            ("Jed Clampet", [1555, 2000, 1200]),
            ("Tony Nelson", [75, 100, 105]),
            ("Marcia Brady", [15, 10]),
            ("Samantha Stevens", [105, 100, 200]),
            ]

#
# function to scan donor list and print donor Name (0th elem in list)
#
def print_donors():
    print("\n")
    print("{:^35s} ".format("Our Honorable Donors:\n"))
    for donor in donor_db:
        print("{:|^35s} ".format(donor[0]))

#
# function to find a donor name in database
#

def find_donor(name):
    for donor in donor_db:
        if name.strip().lower() == donor[0].lower():
            return donor
    return None

#
# function for main menu choices
#    

def main_menu():
    user_inp = input(dedent('''

      Please enter action from selection below:
          
      't' - Send a Thank You
      'r' - Create a Report
      'q' - Quit

      > '''))
    return user_inp.strip().lower()

#
# Function to generate a thank you letter for the donor
#

def gen_letter(donor):
    return dedent('''
          Dear {}

          Thank you for your very kind donation of ${:.2f}.
          The first recipients will see a grant for their UW Certificate
          Courses in Python.

                         Sincerely,
                            -The Pythonic Team
          '''.format(donor[0], donor[1][-1]))

#
# Function to generate thank you message and record donation 
# Additional logic to allow user to define addional commands
#

def send_thank_you():
    while True:
        name = input("\nEnter a donor's name "
                     "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            print_donors()
        elif name == "menu":
            return
        else:
            break

    # Now prompt the user for a donation amount to apply. Since this is
    # also an exit point to the main menu, we want to make sure this is
    # done before mutating the donors list object.

    while True:
        
        amount_str = input("Enter a donation amount (or 'm' for menu to exit):  > \n").strip()
        if amount_str[0].lower() == "m": # just test for first letter 
            return
        # Make sure amount is a valid amount before leaving the input loop
        # Added try:except to advise user to stay numeric
        try:
            amount = float(amount_str)
            
            # NOTE: this is getting a bit carried away...
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                print("Please review your entry. There is an error! Donation amount is invalid\n")
                continue  # not really needed, but makes it more clear
            elif amount < 0:
                print("Sorry...we are looking for donators...not recipients.")
            else:
                break
        except ValueError:
            print("Sorry. Did not understand. Please enter a numeric donation.")

    # If this is a new user, ensure that the database has the necessary data structure.
    donor = find_donor(name)
    if donor is None:
        donor = (name, [])
        donor_db.append(donor)

    # Record the donation
    # Note-> donor object can be manipulated while it is in the donors list!
    donor[1].append(amount)

    print(gen_letter(donor))

#
#

def sort_key(item):
    return item[1]


#
# Generate report of donors and donations
#

def print_donor_report():

    report_rows = []
    for (name, gifts) in donor_db:
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    # sort the report data
    report_rows.sort(key=sort_key)
    # print it out in with a nice format.
    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 66)
    for row in report_rows:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))

if __name__ == "__main__":
    running = True
    while running:
        selection = main_menu()
        if selection == "t":
            send_thank_you()
        elif selection == "r":
            print_donor_report()
        elif selection == "q":
            running = False
        else:
            print("error: menu selection is invalid!")
