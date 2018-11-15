#!/usr/bin/env Python3

"""
Date: November 13th, 2018
Created by: Carol Farris
Purpose: Mailroom 3
Goal: Add as many exception handlers as possible (added 3 for User input)
      Add comprehensions...need to complete
      update code to continue to keep clean PEP8 code (ongoing)
"""

import sys
import os
from textwrap import dedent

OUT_PATH = "thank_you_letters"


def prepare_to_write_to_disk():
    """
    Check OUT_PATH specified is a directory, if not, it will make it
    This is to run once at the start of the application.
    :Param: none
    :Return: none. Creates specified folder in CWD if not already created.
    """
    if not os.path.isdir(OUT_PATH):
        os.mkdir(OUT_PATH)


def send_file_to_disk(person, myfile):
    """
    Accepts test file and writes to disk
    :param (myfile):
    :return: none. Will send file to directory set in outpath.
    """
    filename = person.replace(' ', '_') + '.txt'
    filename = os.path.join(OUT_PATH, filename)
    open(filename, 'w').write(myfile)


def assemble_thank_you(getPerson='No_name_given',
                       getDonation='No cash specified'):
    """
    assembles a thank you letter
    :param(getPerson):
    :param(getDonation):
    :return: assembled text file with persons full name.txt
    """
    return dedent(
        '''\tDear {},
        Thank you for your generous donation of ${} to our cause
        Because of donors like you, we are able to execute our mission
        to support at risk youth in achieving academic success.
        Your contribution also ensures we will have the funds to develop
        new programs to reach those most vulnerable.
        
        Sincerely,
        Team Umizoomi'''.format(getPerson, getDonation))


def getDonation():
    """
    Asks user to specify donation amount and will error out if 
    User specifies other than an int amount.
    This could be modified in next version so entry can include 2 decimal places.
    :Param: none
    returns: donation retrieved from user
    """
    getDonation = ''
    while not type(getDonation) is int:
        try:
            getDonation = int(input("Please enter donation amount:"
                                    "==>"))
        except ValueError:
                print('Sorry, that isn\'t a valid integer. Please retry')
    return getDonation


def thankyou():
    """
    :param:
    :returns:
    """
    getPerson = ''
    donation = ''
    while getPerson not in donor_db:
        getPerson = input('Please type the donors first and last name or '
                          'type list to get donor list ==>')
        getPerson = getPerson.strip().lower().title()
        if getPerson == 'List':
            for key in donor_db:
                print(key)
        elif getPerson == 'x':
            exitout()
        else:
            try:
                print(donor_db[getPerson])
                donation = getDonation()
                donor_db[getPerson].append(donation)
            except KeyError:
                print("This new person will be added to the dictionary.")
                donation = getDonation()
                donor_db[getPerson] = [donation]
            finally:
                printThankYou(getPerson, donation)


def alldonors():
    """
    Print thank you letters to all donors.
    first retrieve donor list, print to last donation and collective donations.
    will have to pass the person and the donation amount to "print thank you"
    """
    print("Printing to file thank you letters to all donors in database...")
    for key, value in donor_db.items():
        sumDonations = round(float(sum(value)), 2)  # total Given
        donorLetter = assemble_thank_you(key, sumDonations)
        send_file_to_disk(key, donorLetter)


def printThankYou(getPerson, getDonation):
    """
    prints thank you letter for person and donation specified
    :param: User provided person and donation amount
    :returns: none (will return letter to save to disk shortly)
    """
    print(assemble_thank_you(getPerson, getDonation))


def makereport():
    """
    Calculates values to put into report
    :param:
    :return:
    """
    donorReport = []
    for key, value in donor_db.items():
        sumDonations = round(float(sum(value)), 2)  # total Given
        numDonations = len(value)
        avgDonations = round(float(sum(value) / len(value)), 2)
        donorReport.append([sumDonations, key, numDonations, avgDonations])
    sortedReport = sorted(donorReport)
    ascendingReport = sortedReport[::-1]
    printReport(ascendingReport)


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
    print("##########_ERROR_##############")
    print("Please use the actual choices!")
    print("##########________##############")
    return None


if __name__ == '__main__':
    user_choices = {'t': thankyou,
                    'r': makereport,
                    'x': exitout,
                    'a': alldonors}

    donor_db = {"William Gates III": [653772.32, 12.17],
                "Jeff Bezos": [877.33],
                "Paul Allen": [663.23, 43.87, 1.32],
                "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
                "John Galt": [25.00, 9038.01, 0.01]
                }
    prepare_to_write_to_disk()

    main()
