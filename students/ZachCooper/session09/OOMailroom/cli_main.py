#!/usr/bin/env python3

from donor_models import *



# Function triggers main dispatch dict that

def menu_selection(prompt, dispatch_dict):
    # Really like the menu dict option using switches
    while True:
        response = input(prompt)
        response = response[:1].lower()
        if dispatch_dict.get(response, unknown)() == "exit menu":
            break


def unknown():
    print("that was not a valid response")
    return None

# Main prompt user interacts with
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

# Dispatch that call the functionality
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


# Send a thank you to donor after asking for donation amoung
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
