#!/usr/bin/env python3

"""
mailroom assignment
"""

# Mailroom Part 1

#List of previous donors names and their donation amounts
donors = {"Rick Sanchez": [3.00, 1.00],
          "Liz Lemon": [4000.00, 3000.00, 6000.00],
          "Andy Dwyer": [10.00],
          "Brendan Small": [3.00, 10.00],
          "Coach McGuirk": [2.00, 1.00]}


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
            create_report()
        elif response == "2":
            thanks()
        else:
            print("Incorrect entry! Please try again from the menu options.")


#Thank the user for their donation
def thanks():

    #initialize input
    donor_name = ""

    while donor_name == "" or donor_name == "E" or donor_name == "L":
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
                print(name)

    #set initial donation amount to 0
    donation = 0

    while donation <= 0:
        donation = input("Please enter the donation amount or type 'E' to return to the main menu: ")
        if donation[0].upper() == "E":
            return
        else:
            donation = float(donation)


    #check if donor already exists in donors dict, if not, append name and donation
    donations = donors.setdefault(donor_name, [])
    donations.append(donation)


    #call email function to print thank-you email
    email(donor_name, donation)


#function to print a thank-you email
def email(donor_name, donation):
    message = ("\n\nDear {},"
    "\n\nThanks for your money! Your donation of ${:.2f} will be summarily used to buy me beer.\n\n"
    "Kind regards,\nKate Koehn").format(donor_name, donation)
    file_name = "{}.txt".format(donor_name)
    with open(file_name, "w") as f:
        f.write(message)


#create a report of all previous donors and their donations
def create_report():
    print("\n", "\n", "{:<20}{:5}{:5}{}".format("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"))
    print("{:-<60}".format(""))
    for donor, gifts in donors.items():
        total = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total / num_gifts
        print("{:<22} ${:<13.2f} {:<10} ${:.2f}".format(donor, total, num_gifts, avg_gift))


#welcome screen function
def main():
    print("Welcome to the Mailroom, Parts 1 and 2!")
    menu()
    print("Thanks for the dough, Smell you later!")


if __name__ == "__main__":
    main()

