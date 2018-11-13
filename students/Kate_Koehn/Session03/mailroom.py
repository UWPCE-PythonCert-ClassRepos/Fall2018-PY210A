#!/usr/bin python3

"""
mailroom assignment
"""

# Mailroom Part 1

#List of previous donors names and their donation amounts
donors = [("Rick Sanchez", [3.00, 1.00]), ("Liz Lemon", [4000.00, 3000.00, 6000.00]), ("Andy Dwyer", [10.00]),
          ("Brendan Small", [3.00, 10.00]), ("Coach McGuirk", [2.00, 1.00])]


#menu to give user options to Create a Report, Send a Thank you, or Quit
def menu():

    response = ""

    #loop through menu options; exit program if user selects "3"
    while response != "3":
        print("\n~ Main Menu ~")
        print("Press 1 to Create a Report")
        print("Press 2 to Send a Thank You")
        print("Press 3 to Quit")

        response = input("\nPlease enter a command: ")
        if response == "3":
            break
        elif response == "1":
####need to create report function            
            pass
        elif response == "2":
            thanks()
        else:
            print("Incorrect entry! Please try again from the menu options.")


#Thank the user for their donation
def thanks():
    
    #initialize input
    donor_name = ""

    while donor_name == "" or donor_name == "exit" or donor_name == "list":
        print("\n~ Thanking Your Donors ~\n")
        donor_name = input("Please choose from your list of options:\n\n"
                     "To send a thank you to a new donor, please type the full name of the donor you would like to thank and press 'Enter'. \n"
                     "Type 'L' to see a list of previous donors. \n"
                     "Type 'E' to return to main menu. ").title()

        #return to main menu
        if donor_name == "E":
            return

        #return list of previous donor names
        elif donor_name == "L":
            for name in donors:
                print(name[0])

    #set initial donation amount to 0
    donation = 0

    while donation <= 0:
        donation = input("Please enter the donation amount or type 'E' to return to the main menu: ")
        if donation[0].upper() == "E":
            return
        else:
            donation = float(donation)

    #initialize new donor 
    new_donor = True

    #check if donor already exists in donors dict, if not, append name and donation
    for i in range(len(donors)):
        if donors[i][0] == donor_name:
            donors[i][1].append(donation)
            new_donor = False
            break
    if new_donor:
        donors.append((donor_name, [donation]))

    #call email function to print thank-you email
    email(donor_name, donation)


#function to print a thank-you email
def email(donor_name, donation):
     print("Dear {donor_name},\n",
     "\nThanks for your money! Your donation of ${donation:.2f} will be summarily used to buy me beer.\n",
     "\nKind regards,\n",
     "Kate Koehn".format())
    ######having issue with formatting - "donation" throws KeyError


#welcome screen function
def main():
    print("Welcome to the Mailroom, Part 1!")
    menu()
    print("Smell you later!")


if __name__ == "__main__":
    main()

