#!/usr/bin/env Python3

#Date: October 23, 2018
#Created by: Carol Farris
#Purpose: Mailroom 1/2
#Goal: Create rough framework for Mailroom 
#Notes: I did jump to using a dictionary to hold the donors, rather than a tuple/list

import sys

#use donors provided in Mailroom tutorial plus John Galt 
donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "John Galt": [25.00, 9038.01, 0.01]
            }      


def thankyou():
    getPerson = ''
    while getPerson not in donor_db :
        getPerson = input('Please type the donors first and last name or '
                       'type list to get donor list ==>')
        getPerson = getPerson.strip().lower().title()
    
        if getPerson == 'List' :
            for key in donor_db:
                print (key)
        elif getPerson == 'x':
            exitout()
        else:
            #In next version, input needs to be checked to ensure entry is numeric and sensible.
            getDonation = input("Please enter donation amount:"
                                "==>")
            if key in donor_db:
                donor_db[getPerson].append(getDonation)
            else:    
                donor_db[getPerson] =  getDonation      
                                           
    print("\n\nDear " + getPerson + ",\n\n"
        "Thank you for your generous donation of $"+ getDonation + " to our cause.\n"
        "Because of donors like you, we are able to execute our mission to support \n"
        "at risk youth in achieving academic success. Your contribution also ensures\n"
        "we will have the funds to develop new programs to reach those most vulnerable.\n\n"
        "Sincerely,\n\n"
        "Team Umizoomi\n")

#create a report of all donors and their contributions    	    
def makereport():
    print("reporting for duty!\n\n")
    donorReport = []
    count = 0
    for key, value in donor_db.items()  :
        count +=1
        name = key
        sumDonations = float(sum(value)) #total Given
        numDonations = len(value)
        avgDonations = float(sum(value)/len(value))
        #next add all the above (except count) to a list of donor reports
        #pass the donor reports to a print function
        print(count, "\t", name, "\t", sumDonations, "\t", numDonations, "\t", avgDonations)

def exitout():
    print("Exiting program...\n")
    sys.exit()	


def main():
    print("Welcome to the Mailroom!")
    answer = ""
    while answer != 'x':
        print("\n\nPlease select from the following:")
        print("Exit: x,\nThank you letter: 't',\n"
             "Create Report: r\n")
        answer = input(' ==> ')
        answer = answer.strip() #Strip any whitespace
        answer = answer[0:1].lower() # this allows you to always make sure you get the first letter only. 
        #important if somebody types the word quit rather than q. It also turns to lowercase.
        if answer == 't':
            thankyou()
        elif answer == 'r':
            makereport()
        elif answer == 'x':
            exitout() 
        else:
            print("Invalid choice!\n")


if __name__ == '__main__' :
    main()










