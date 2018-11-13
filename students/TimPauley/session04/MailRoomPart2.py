#Tim Pauley
#Python 201a HW3
#Date Nov 5 2018
#Mail Room Part 2


#This is the update from Part 2
#Update using Dictionaries
#1. See if you can use a dict to switch between the user’s selections.
#2. See if you can use a dict to switch between the users selections. 
#3. see Using a Dictionary to switch for what this means.
#4. Convert your main donor data structure to be a dict.
#5. Try to use a dict and the .format() method to produce the letter as one 
#big template, rather than building up a big string that produces the letter in parts.

import sys
import math 

# this creates better printing
from textwrap import dedent

#Get Donors
def get_donor_db():
    return {'william gates iii': ("William Gates III", [653772.32, 12.17]),
            'jeff bezos': ("Jeff Bezos", [877.33]),
            'paul allen': ("Paul Allen", [663.23, 43.87, 1.32]),
            'mark zuckerberg': ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            }

#List out donors
def list_donors():
    listing = ["Donor list:"]
    for donor in donor_db.values():
        listing.append(donor[0])
    return "\n".join

# this fuction finds a donors name
def find_donor_Name():
    name = name.strip()
    donor = (name, [])
    donor_db[name.lower()] = donor
    return donor
    
def main_menu_selection():
    action = input(dedent('''
        Choose an action:
        1 - Send a Thank You
        2 - Create a Report
        3 - Send letters to everyone
        4 - Quit
        > '''))
    return action.strip()

def gen_letter(donor):
    return dedent('''Hey {0:s},
          Thanks for yur donation of ${1:.2f}.
          It will help with our mission.
                         Thanks,
                            -The Dream Team
          '''.format(donor[0], donor[1][-1]))

#1 - Send Thank-you card
def send_thank_you():
    while True:
        name = input("Enter a donor's name (Enter 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            print(list_donors())
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
        #Eception Handling: check to see if value is numeric
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                raise ValueError
        except ValueError:
                print("error: donation amount is invalid\n")
        else:
            break
            donor = find_donor(name)
        if donor is None:
            donor = add_donor(name)
    donor[1].append(amount)
    print(gen_letter(donor))


def sort_key(item):
    return item[1]


def generate_donor_report():
    report_rows = []
    for (name, gifts) in donor_db.values():
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    # sort the report data
    report_rows.sort(key=sort_key)
    report = []
    report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                            "Total Given",
                                                            "Num Gifts",
                                                            "Average Gift"))
    report.append("-" * 66)
    for row in report_rows:
        report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
    return "\n".join(report)

#3 - Save letters to local
def save_letters_to_disk():
    for donor in donor_db.values():
        letter = gen_letter(donor)
        filename = donor[0].replace(" ", "_") + ".txt"
        open(filename, 'w').write(letter)

#2 - Print Donor Report
def print_donor_report():
    print(generate_donor_report())

#4 - Quit Program
def quit():
    sys.exit(0)

#Main Method run program
if __name__ == "__main__":
    donor_db = get_donor_db()
    running = True
    selection_dict = {"1": send_thank_you,
                      "2": print_donor_report,
                      "3": save_letters_to_disk,                      
                      "4": quit}

    while True:
        selection = main_menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: your menu selection is wrong")
#End Program