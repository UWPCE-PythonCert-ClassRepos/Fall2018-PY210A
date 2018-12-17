#1/usr/bin/env python3

import sys

from donor_models import DB, Donor


donors_db = DB()


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == 'exit menu':
            break

def quit():
    print('Quitting this menu now')
    return'exit menu'

#------------------------------------------------------


def thank_you():
    menu_selection(sub_prompt, sub_dispatch)

def find_donor():
    name = input('Enter a donor fullname or add a new one:')



def print_donors():
    print('Printing donors list...\n')
    print(donors_db.list_donors)

def add_donor():
    '''Get name and donation amount to add to DONORS'''
    name = input("Create a donor(fullname): ")
    donation = int(input('Donation amount: '))
    return donors_db.add_donor(name , donation)

def add_donation():
    name = input("Enter the donor's fullname: ")
    if donors_db.find_donor(name) == None:
        print('Donor was not found')
        add_donor()
    else:
        amount = int(input('Enter the amount of recent donation: '))
        donors_db.update_donor(name, amount)


def gen_letter():
    name = input("Enter donor's name:")
    donor = Donor(name)
    print(donor.gen_letter)

def report():
    print(donors_db.report)

def save_letters():
    return donors_db.save_data()


#----------------------------------------
# Dispatch Dictionaries
#----------------------------------------

main_dispatch = {'1': thank_you,
                 '2': report,
                 '3': save_letters,
                 '4': quit
                 }

sub_dispatch = {'1': print_donors,
                '2': add_donor,
                '3': add_donation,
                '4': gen_letter,
                '5': quit
                }

#----------------------------------------
# Prompts
#----------------------------------------

main_prompt = ('\nYou are in the main menu now!!\n'
               '1 - Send a Thank You to a single donor\n'
               '2 - Create a Report\n'
               '3 - Save letters\n'
               '4 - Quit\n'
               )

sub_prompt = ('\nYou are in the "Thank You"-menu now!!\n'
                    'What do you want to do?\n'
                    '1 - List all existing donors\n'
                    '2 - Add donor\n'
                    '3 - Update donor\n'
                    '4 - Generate a thank you letter\n'
                    '5 - Quit\n'
                    )




if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)