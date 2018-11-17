#!/usr/bin python3
import os
import sys
import math

from textwrap import dedent

donors_info = {"Bill Gates": [3500, 5500, 7500],
               "Paul Alen": [3000, 3700, 3900],
               "Jeff Benzo": [3300, 5000, 7500],
               "Mark Zuckerberg": [33565.37, 465.37, 545.37, 7506],
               "Warren Buffett": [3303.17, 334.17, 5080, 7500]
               }

prompt = "\n".join(("\n Choose an action:",
                    " 1 - Send a Thank You to a single donor",
                    " 2 - Create a Report",
                    " 3 - Send letters to all donors",
                    " 4 - Quit\n"
                    " >>> "))

OUT_PATH = "thank_you_letters"

def send_thankyou():
    """print email to the terminal,\n
    prompt for list show a list of the donor names and re-prompt"""

    d_name = input("Enter donor name Or \nType \'list' if you don't know donor name?: ")
    if d_name in "list":
        for donor in donors_info:
            print(f"- {donor}")
        d_name = input("Enter a donor name?: ")
       
    if d_name not in donors_info:
        donors_info[d_name] = []
    
    contribution = float(input(f"Enter {d_name} contribution :? "))
    donors_info[d_name].append(contribution)
    print()
    print(
"""
Dear {},
   \nThank you for your generous donation ${:,.2f}.
""".format(d_name, contribution))
    print("Best regards,\nYour Youth and Seniors Foundation \n")


def create_report():
    """prints list of donors, sorted by total historical donation amount."""
    print()
    print("{:<20}| {:<10} | {:<10} | {:<12}".format("Donor Name", "Total Given", " Num Gifts", "Average Gift"))
    print("-" * 60)
    for name,contributions in donors_info.items():
        print("{:<21} ${:<15.2f} {:<10} ${:<12.2f}".format(
            name, sum(contributions), len(contributions), sum(contributions) / len(contributions)))


def exit_program():
    """quit current task and return to the original prompt"""
    print("Bye!")
    sys.exit()


menu_switcher = {
    "1": send_thankyou,
    "2": create_report,
    #"3": save_letter_todisk,
    "4": exit_program
}

def main():
    while True:
        response = input(prompt)
        menu_switcher[response]()
        
if __name__ == '__main__':
    main()
