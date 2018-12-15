#!/usr/bin/env Python3

########
#Created by: Carol Farris
#Date: 12/11/18
#Purpose: Remake Mailroom in OO fashion
#CLi_main is to store all the UI and print statements
#Progress: Worked on Thank you. need to add to donor collection:
# def return_sum_donations given a donor key
# def return_last_donations given a donor key
# def return_num_donations given a donor key
#The above 2 will be for thank you as well as all above for report.
#Then make a test suite out of them. 
#if stuck:
#I changed method names to make them more pythonic. ex. thankyou to thank_you
#changed exit from x to 1 to make it cleaner looking
#I will only import modules as I need them. Do I still need OS and dedent?
########

import sys

from OO_Mailroom import Donor, DonorCollection


def thank_you():
    """Returns a user selected Donor thank you letter for either
       the sum of the donations or their last donation."""
    getPerson = get_donor()
    donationType = ''
    while donationType !='Done':
        print("What type of donation do you want to reference in your Thank You letter?")
        print("(1) To Exit\n(2) Add a new donation amount\n(3) To reference the"
              " last donation\n(4) To reference the sum of all donations\n")
        donationType = input(str('>>>'))
        donationType = donationType.strip()
        donationType = donationType[0:1].lower()
        try:    
            donation, donationType = donation_choices.get(donationType)(getPerson, donationType)
            print("donationType", donationType)
        except TypeError:
            retry()
    print(assemble_thank_you(getPerson, donation)) #oritional thank you printed to console. 


def get_donor():
    """Prompts user to provide donor name and returns name if found or adds to collection"""
    haveDonor = False
    donor = ''
    while dc.donor_in_dictionary(donor) == False:
        donor = input('\nPlease enter the donors first and last name,  '
                      'type List to get donor list or 1 to exit ==>')
        donor = donor.strip().lower().title()

        if donor == str(1):
            exit_out()

        if donor == 'List':
            print(dc.list_donors())

        if dc.donor_in_dictionary(donor):
            print("donor found in collection: ")#####debuggin
            dc.addDonor(donor, Donor(donor))
            haveDonor = True
            return donor

        if not donor == 1 and not donor == "List":
                print("\n>>>>>Donor specified not found in collection.<<<<<<<\n")
                repeat = input(("Do you wish to add person? Type: Y \nType: 1 to exit\nPress any other key to retry...\n "))
                repeat = repeat.strip().lower().title()

                if repeat == 'Y':
                    print("Will add ", donor, " to the database.") ###debugging
                    dc.addDonor(donor, Donor(donor))
                    haveDonor = True
                    return donor
                if repeat == 1:
                    exit_out()

def get_new_Donation(getPerson, donationType):
    """
    Asks user to specify donation amount and will error out if 
    User specifies other than a float amount.
    :Param: none
    returns: donation retrieved from user
    """
    getDonation = input()
    while not type(getDonation) is float:
        try:
            getDonation = float(input("Please enter donation amount:"
                                    "==>"))
            dc.add_donor_donation(getPerson,getDonation)
            print("New donation of ", getDonation, " was added to "+ getPerson +"\'s file.")
            donationType = 'Done'
        except ValueError:
                print('Sorry, that isn\'t a valid dollar amount. Please retry')
    return getDonation, donationType


def get_last_donation(getPerson, getDonation=''):
    print("you want to get the last donation. Under Construction.")
    donationType = 'Done'
    #get last donation here
    return donationType

def get_sum_donations(getPerson, getDonation=''):
    print("you want to get sum of the donations. Under Construction.")   
    donationType = 'Done'
    #get sum donations here
    return donationType


def assemble_thank_you(getPerson, donation):
    print("you are in assemble thank you, WIP") 

def make_report():
    print("you selected to make a report, WIP")


def all_donors():
    print("you selected to send thank you to all donors")
    print("first call list, for each key, print the thank you.")


def exit_out():
    """
    produces a clean exit from the program
    """
    print("Exiting program...\n")
    sys.exit()


def main():
    """Prompts user for action selection and directs to the relevant action."""
    print("Welcome to the Mailroom!")
    answer = ""
    while answer != '1' or '2' or '3' or '4':
        try:
            print("\n\nPlease select from the following:\n")
            print("(1) - Exit\n" +
                  "(2) - Create a Report\n" +
                  "(3) - Thank you letter\n" +
                  "(4) - send thank you letters to all donors\n")
            answer = input(' ==> ')
            answer = answer.strip()
            answer = answer[0:1].lower()
            user_choices.get(answer)()
        except TypeError:
            retry()


def retry():
    """
    will prompt user to retry selection to make it valid
    :param: none
    :return: none
    """
    print("\n\n\n##########_ERROR_##############")
    print("Please use the actual choices!")
    print("###############################\n\n\n")
    return None


if __name__ == '__main__':
    donor_mock = [Donor("William Gates III", [653772.32, 12.17]),
                Donor("Jeff Bezos", [877.33]),
                Donor("Paul Allen", [663.23, 43.87, 1.32]),
                Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
                Donor("John Galt", [25.00, 9038.01, 0.01])]

    user_choices = {'3': thank_you,
                    '2': make_report,
                    '1': exit_out,
                    '4': all_donors}

    donation_choices = {'1': exit_out,
                        '2': get_new_Donation,
                        '3': get_last_donation,
                        '4': get_sum_donations
                         }


    dc = DonorCollection(donor_mock)
    print(dc.list_donors())# how you list donors.              
    main()
    
