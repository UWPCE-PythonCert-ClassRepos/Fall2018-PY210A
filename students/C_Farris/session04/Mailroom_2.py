#!/usr/bin/env Python3

"""
Date: November 6th, 2018
Created by: Carol Farris
Purpose: Mailroom 2
Goal: Use dict to switch between users selections (completed),
    write thank you letter to the file, 
    try to use the dict and .format() to produce the template
    rather than using one big string.
"""

import sys
     

#Part 1 of Thank You letter. Gets information from user and stores it.
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
            getDonation = int(input("Please enter donation amount:"
                                "==>"))
            print("the type of getDonation is...")
            print(type(getDonation))
            if getPerson in donor_db:
                donor_db[getPerson].append(getDonation)
            else:    
                donor_db[getPerson] =  [getDonation] 
            printThankYou(getPerson,getDonation)                 

#Part 2 of thank you letter. Prints the letter using string formatting.
def printThankYou(getPerson, getDonation):                                           
    print("\n\nDear {},\n\n".format(getPerson))  #add dear and , to dictionary
    print("Thank you for your generous donation of ${} to our cause".format(getDonation))
    print("Because of donors like you, we are able to execute our mission to support \n" #add to above dictionary
        "at risk youth in achieving academic success. Your contribution also ensures\n"
        "we will have the funds to develop new programs to reach those most vulnerable.\n\n" #Lump together in one value
        "Sincerely,\n\n"  #Add as separate value
        "Team Umizoomi\n") #add as separate value

#Part 1 of make Report. Calculates values to be put into report 	    
def makereport():
    donorReport = []
    #count = 0
    for key, value in donor_db.items()  :
        #count +=1
        sumDonations = round(float(sum(value)),2) #total Given
        numDonations = len(value)
        avgDonations = round(float(sum(value)/len(value)),2)
        donorReport.append([sumDonations, key, numDonations,avgDonations ])
    sortedReport = sorted(donorReport)
    ascendingReport = sortedReport[::-1]
    printReport(ascendingReport)

#Part 2 of Make report. Prints the calculated values to the console
def printReport(ascendingReport):
    for donor in ascendingReport:
        print('{:<20}'.format(donor[1]),'{:<15}'.format(donor[0]),
              '{:>5}'.format(donor[2]),'{:>25}'.format(donor[3]))    

#generate a clean exit when user specifies an 'x'
def exitout():
    print("Exiting program...\n")
    sys.exit()	


def main():
    print("Welcome to the Mailroom!")
    answer = ""
    while answer != 'x':
        print("\n\nPlease select from the following:")
        print("x - Exit\nt - Thank you letter\n"
             "r - Create a Report\n")
        answer = input(' ==> ')
        answer = answer.strip() #Strip any whitespace
        answer = answer[0:1].lower() # this allows you to always make sure you get the first letter only. 
        user_choices.get(answer)()     
        

if __name__ == '__main__' :
    user_choices = {'t': thankyou, 'r': makereport, 'x': exitout}

    donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "John Galt": [25.00, 9038.01, 0.01]
            } 

    main()










