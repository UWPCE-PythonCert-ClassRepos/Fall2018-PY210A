#!/usr/bin/env python3
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


def generates_letter(donor, contribution):
    # Generate a thank you letter template for each donors
        print(
            """

Dear {},
    
    Thank you for your generous donation ${:,.2f}.

Best regards,
Your Youth and Seniors Foundation

        """.format(donor, contribution))


def send_thankyou(*donor):
    # """Send the actual thank you letter.
    # Arg:
    #    optional argument, tooks user input.
    # Return:
    #    generat a thank you letter
    #    """
    d_name = input(
        "Enter donor name Or \nType \'list' if you don't know donor name?: ")
    if d_name in "list":
        # list comprehension here
        [print(f"-{donor}") for donor in donors_info]
        d_name = input("Enter a donor name?: ")


    if d_name not in donors_info:
        donors_info[d_name] = []

    contribution = float(input(f"Enter {d_name} contribution :? "))
    donors_info[d_name].append(contribution)
    generates_letter(d_name, contribution)


def create_report():
    # create a report for donors contribution as a table formate.
    """prints list of donors, sorted by total historical donation amount."""
    print("{:<20}| {:<10} | {:<10} | {:<12}".format("Donor Name", "Total Given", " Num Gifts", "Average Gift"))
    print("-" * 60)
    # list comprehension here
    [print("{:<21} ${:<15.2f} {:<10} ${:<12.2f}".format(
        name, sum(contributions), len(contributions), sum(contributions) / len(contributions))) for name, contributions in donors_info.items()]


def save_letter_todisk():
    """ Save generates thank you letter, 
       and writes each letter to disk as a text file. 
    """
    for donor,contributions in donors_info.items():
        with open(f"{donor.replace(' ', '_')}.txt","w") as output:
            output.write(
                """
Dear {},

    Thank you for your generous donation ${:,.2f}.

Best regards,
Your Youth and Seniors Foundation
                """.format(donor, sum(contributions))
            )
        print(f"Created thank you file for {donor}.")

def exit_program():
    """quit current task and return to the original prompt"""
    print("See you around!")
    sys.exit()


menu_switcher = {
    "1": send_thankyou,
    "2": create_report,
    "3": save_letter_todisk,
    "4": exit_program
}

def main():
    while True:
        try:
            response = input(prompt)
            menu_switcher[response]()
        except (KeyError, KeyboardInterrupt) as key_err:
            print("\nPls select only from the choice, you entered {} ".format(str(key_err)))
            pass
        
if __name__ == '__main__':
    main()
