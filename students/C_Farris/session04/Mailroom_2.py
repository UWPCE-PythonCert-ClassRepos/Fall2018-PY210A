#!/usr/bin/env Python3

"""
Date: November 6th, 2018
Created by: Carol Farris
Purpose: Mailroom 2
Goal: Use Anaconda linter to write PEP8 Python code
    Comment functions correctly
    Use dict to switch between users selections (completed),
    write thank you letter to the file,
    try to use the dict and .format() to produce the template
    rather than using one big string.
Note: not all Pep8 fixes were completed. Minor fixes remain
      Will work on those in Mailroom_3.       
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


def thankyou():
    """
    :param:
    :returns:
    """
    getPerson = ''
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
            #   In next version, input needs to be checked to ensure entry is numeric and sensible.
            getDonation = int(input("Please enter donation amount:"
                                "==>"))
            if getPerson in donor_db:
                donor_db[getPerson].append(getDonation)
            else:
                donor_db[getPerson] = [getDonation]
            printThankYou(getPerson, getDonation)


def alldonors():
    """
    Print thank you letters to all donors.
    first retrieve donor list, print to last donation and collective donations.
    will have to pass the person and the donation amount to "print thank you"
    """
    for key, value in donor_db.items():
        sumDonations = round(float(sum(value)), 2)  # total Given
        #printThankYou(key, sumDonations) for printing to screen
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
        print('{:<20}'.format(donor[1]), '{:<15}'.format(donor[0]),
              '{:>5}'.format(donor[2]), '{:>25}'.format(donor[3]))


def exitout():
    print("Exiting program...\n")
    sys.exit()


def main():
    print("Welcome to the Mailroom!")
    answer = ""
    while answer != 'x':
        print("\n\nPlease select from the following:")
        print("x - Exit\nt - Thank you letter\n" +
              "a - send thank you letters to all donors\n" +
              "r - Create a Report\n")
        answer = input(' ==> ')
        answer = answer.strip()   #Strip any whitespace
        answer = answer[0:1].lower()   # this allows you to always make sure you get the first letter only. 
        user_choices.get(answer, retry)()


def retry():
    """
    will prompt user to retry selection to make it valid
    :param: none
    :return: none
    """
    print("Please use the actual choices!")
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