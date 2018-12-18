#!/usr/bin/env python
import cli_main
import sys
from mail5 import Donor, DonorCollection



donor_dict = { "William Gates, III": [653772.32, 12.17],
             "Jeff Bezos": [877.33],
             "Paul Allen": [663.23, 43.87, 1.32],
             "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]
            }

#menu display from the selection
prompt = "\n".join(("Please choose from below options:",
          "1 - Send a Thank You to a single donor",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - Quit ",
          ">>> "))

donor_db =  DonorCollection(donor_dict)

def send_thankyou():
    """
    This method is prompting enter to enter donor name, list from database, or return to menu

    params:  none - continue prompt user enter data from menu 
    It generate letter when user input amount of donation.
    """

    while True: 
    
        name = input(">Enter first and last name \n >"
            " or 'list' to see all donors name  \n >"
            " or 'menu' return to menu > ")
 
        if (name.lower() == 'list'):            
            donor_db.exist_list()
        elif (name.lower() == 'menu'):
         	return
        else:
            donor = Donor(name)
            ck_name = donor.validate_name()
            if ck_name is False:
                print ("Invalid Entry - Please re-enter first and last name")
            elif ck_name is True:
                donor_db.add_donor(donor)
                # amount = input ("\n Enter amount you want to donate > :")                
                # dollar_amount = donor._ck_dollar(amount) 
                
                donor.add_donations(1231)
                print (donor.donations, "easdfads")
                donor.generate_letter(donor.donations)
                    
  
               
        break


def send_all_letter():
    donor_db.ss_letterall()

def create_report():
    donor_db.create_report()


def quit_program():
    print("Good Bye!")
    sys.exit()  # exit the interactive script

def default():
	print("Invalid options")


#switch to execute function
switch_fnc_dict = {
	                '1': send_thankyou,
	                '2': create_report,
	                '3': send_all_letter,
	                '4': quit_program,	                
                }


def main():
    """
    Start main program to prompt user select from main menu
    Continue prompt user until decide to quit program 
    from switch function dictionary
    returns None
    """
    print("Welcome to mailroom")
    
    while True:
        try:
            response = input(prompt) 
            switch_fnc_dict.get(response, default)()
        except NameError:
            print ("Must enter number from 1-4 from the menu")

if __name__ == "__main__":
    cli_main.main()
