#!/usr/bin/env Python3

"""
Date: November 20th, 2018
Created by: Carol Farris
Purpose: Mailroom 4
Goal: Test All Code using a full suite of tests.

Strategy: for all things that "print", create a "print to screen function"
All others return the value.

prepare to write to disk --> search online to figure out how to write to disk.
send file to disk --> search online

Re-factoring oppertunities:
thankyou()--
--divide in half 
--first, get Donor should be its own function def getDonor():
it will return the Donor specified.
--


user input:
getDonation()--


"""

import sys
import os
from textwrap import dedent

OUT_PATH = "thank_you_letters"

donor_db = {"William Gates III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "John Galt": [25.00, 9038.01, 0.01]
            }


def prepare_to_write_to_disk():
    """
    Check OUT_PATH specified is a directory, if not, it will make it
    This is to run once at the start of the application.
    :Param: none
    :Return: none. Creates specified folder in CWD if not already created.
    """
    if not os.path.isdir(OUT_PATH):
        os.mkdir(OUT_PATH)


def send_file_to_disk(person, donorLetter):
    """
    Accepts "Thank You" donor Letter and writes to disk.
    :param (person): Name of person, will be used in file name
    :param (donorLetter): Thank you letter to donor
    :return: none. Will send file to directory set in outpath.
    """
    filename = person.replace(' ', '_') + '.txt'
    filename = os.path.join(OUT_PATH, filename)
    open(filename, 'w').write(donorLetter)


def assemble_thank_you(getPerson, getDonation):
    """
    assembles a thank you letter
    :param(getPerson):
    :param(getDonation):
    :return: assembled text file with persons full name.txt
    """
    return dedent(
        '''\tDear {},
        Thank you for your generous donation of ${} to our cause.
        
        Sincerely,
        The Team'''.format(getPerson, getDonation))


def getDonation(getDonation=''):
    """
    Asks user to specify donation amount and will error out if 
    User specifies other than an int amount.
    This could be modified in next version so entry can include 2 decimal places.
    :Param: none
    returns: donation retrieved from user
    """
    while not type(getDonation) is int:
        try:
            getDonation = int(input("Please enter donation amount:"
                                    "==>"))
        except ValueError:
                print('Sorry, that isn\'t a valid integer. Please retry')
    return getDonation


def thankyou():
    """
    This function calls 4 other functions that will obtain donor, donation, 
    then print to screen.
    :param:
    :returns: None. It prints to screen
    """
    getPerson = getDonor()
    donation = getDonation()
    add_Donor_Donation(getPerson, donation)
    printThankYou(getPerson, donation)


def add_Donor_Donation(getPerson, donation, updated_db = False):
    """
    Checks if donor is in donor database, adds donor and donation into donor_db
    :param (getPerson): 
    :return: updated donor_db for unit testing if updated_db = true
    """
    try:
        donor_db[getPerson].append(donation)
        print("The amount of ${} was added to {}'s profile".format(donation, getPerson))
    except KeyError:
        print("This new person will be added to the dictionary.")
        donor_db[getPerson] = [donation]
    finally:
        if updated_db == True:
            return donor_db


def getDonor():
    """
    Asks user for donor
    :param: none
    :returns: getDonor (donor name)
    """
    getDonor = ''
    while getDonor not in donor_db:
        getDonor = input('Please type the donors first and last name or '
                          'type list to get donor list ==>')
        getDonor = getDonor.strip().lower().title()
        if getDonor == 'List':
            for donor in donor_db:
                print(donor)
        elif getDonor == 'x':
            exitout()
        else:
            return getDonor

def alldonors():
    """
    Print thank you letters to all donors.
    first retrieve donor list, print to last donation and collective donations.
    will have to pass the person and the donation amount to "print thank you"
    """
    print("###############################################################")
    print("Printing to file thank you letters to all donors in database...")
    print("###############################################################")
    for key, value in donor_db.items():
        sumDonations = round(float(sum(value)), 2)  # total Given
        donorLetter = assemble_thank_you(key, sumDonations)
        send_file_to_disk(key, donorLetter)


def printThankYou(getPerson, getDonation):
    """
    prints thank you letter for person and donation specified
    :param: User provided person and donation amount
    :returns: none 
    """
    print(assemble_thank_you(getPerson, getDonation))


def makereport(return_Report=False):
    """
    Calculates values to put into report
    :param:
    :return:
    """
    donorReport = [[round(float(sum(value)), 2), key, len(value),
                    round(float(sum(value) / len(value)), 2)]
                    for key, value in donor_db.items()]
    sortedReport = sorted(donorReport)
    ascendingReport = sortedReport[::-1]
    print(ascendingReport)
    printReport(ascendingReport)
    if return_Report == True:
        return ascendingReport


def printReport(ascendingReport):
    """
    print report using f.strings
    :param (name): sorted list in ascending order that
                   contains required information
                   for each donor
    :return: It prints, neet to put into a return statement####
    """
    for donor in ascendingReport:
        print('{:<20}'.format(donor[1]), '{:<15,}'.format(donor[0]),
              '{:>5}'.format(donor[2]), '{:>25,}'.format(donor[3]))


def exitout():
    """
    produces a clean exit from the program
    """
    print("Exiting program...\n")
    sys.exit()


def main():
    print("Welcome to the Mailroom!")
    answer = ""
    while answer != 'x' or 'r' or 't' or 'a':
        try:
            print("\n\nPlease select from the following:")
            print("x - Exit\nt - Thank you letter\n" +
                  "a - send thank you letters to all donors\n" +
                  "r - Create a Report\n")
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
    user_choices = {'t': thankyou,
                    'r': makereport,
                    'x': exitout,
                    'a': alldonors}


    prepare_to_write_to_disk()

    main()


