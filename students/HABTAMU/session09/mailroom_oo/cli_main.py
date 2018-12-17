#!/usr/bin/env python3
"""responsible for main program flow (CLI - Command Line Interface) """
# import sys
# from os.path import dirname, realpath
# sys.path.insert(0, dirname(realpath(__file__)))

import sys

# To run the test_mailroom_oo package before module name donor_models as
# from mailroom_oo.donor_models import DonorCollection
from donor_models import DonorCollection

class CLI:
    prompt = "\n".join(("\n Choose an action:",
                        " 1 - Send a Thank You to a single donor",
                        " 2 - Create a Report",
                        " 3 - Send letters to all donors",
                        " 4 - Quit\n"
                        " >>> "))

    # Initialize DonorCollection class for usability its donor_info db and all its attribute and methods here.
    ledger = DonorCollection()

    def send_thankyou(self):
        """Generate thank you message. """ 
        d_name = input(
            "Enter donor name Or \nType \'list' if you don't know donor name?: ")
        if d_name == "list":
            print(self.ledger.list_donors())
            d_name = input("Enter a donor name?: ")

        # check if the input string (donor name) contains a number
        if any(char.isdigit() for char in d_name) :
            sys.exit("\nValueError: Name shouldn't contian digit charcters.\n")
        
        # catch ValueError if input for donation  is string character
        try:
            contribution = float(input(f"Enter {d_name} contribution :? "))
            print(self.ledger.add_donation(d_name,contribution))
        except ValueError:
            print("\nValueError: Contribution shouldn't be character\n")

            
    def save_letter_todisk(self):
        print(self.ledger.save_letter_todisk())

    def create_report(self):
        print(self.ledger.create_report())

    def exit_program(self):
        """quit current task and return to the original prompt"""
        print("See you around!")
        sys.exit()

    menu_switcher = {
        "1": send_thankyou,
        "2": create_report,
        "3": save_letter_todisk,
        "4": exit_program
    }
    def main(self):
        while True:
            try:
                response = input(self.prompt)
                self.menu_switcher[response](self)
            except (KeyError, KeyboardInterrupt) as key_err:
                print("\nPls select only from the choice, you entered {} ".format(str(key_err)))
                pass
            

if __name__ == '__main__':
    try:
        CLI().main()
    except KeyboardInterrupt:
        sys.exit(130)
