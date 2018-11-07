"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
Mailroom Assignment - week 1 / session 03 
"""

import sys


donors = [("Javier Bardem", [1000, 800, 4000]),
          ("Pino Aprile", [200, 400, 1000]),
          ("Oprah Winfrey", [10000, 20000, ]),
          ("Peter Voss", [3000, 200, 15000]),
          ("Luciano Pavarotti", [2000, 750, 3000])]


#this is the main function that drives the program
def main():
    print("\nWelcome to the Mailroom\n", "{:_<20}".format("_"))
    #donors = ""
    running = True
    while running:
        print("\nMailroom Main Menu - Please respond by typing 1, 2, or 3, then press enter\n")
        print("1) Send a Thank You Email")
        print("2) Create a Donor Report")
        print("3) Send letters to all donors")
        print("4) Quit")
        option = input("> ")
        if option == "1":
            thank_you()
        elif option == "2":
            donor_report()
        elif option == "3":
            letter_to_all_donors()
        elif option == "4":
            exit_program()


def thank_you():
    print("Select '1' view complete donor list")
    print("Select '2' add new donor to list of donors")
    print("Select '3' send Thank You Email")
    user_selection = input("> ")
    if user_selection == "1":
        donor_list()
    elif user_selection == "2":
        add_new_donor()
    elif user_selection == "3":
        send_thank_you_email()


def donor_list():
    print("-- Donors --")
    for i in donors:
        print(i[0])


def add_new_donor():
    new_donor = input("Enter the name of a new donor: ").title()
    donors.append(new_donor)
    #print(donors)
    donation_amount = input("Please enter the donation amount of the new donor: ")
    donors.append([donation_amount])
    print(donors)


def send_thank_you_email():
    name = ""
    while name == "" or name == "L" or name == "E":
        name = input("Please enter the donor's full name, "
                     "type L to see a list of previous donors, "
                     "or type E to exit to main menu: ").title()
        # Exit if the user types "E"
        if name == "E":
            return
        # If user types "L" show them a list of the donor names
        elif name == "L":
            for x in donors:
                print(x[0])
    donation = 0
    while donation <= 0:
        donation = input("Please enter the donation amount or type E to exit: ")
        if donation[0].capitalize() == "E":
            return
        else:
            donation = float(donation)
    # Set default for new_donor to True
    new_donor = True
    for i in range(len(donors)):
        if donors[i][0] == name:
            donors[i][1].append(donation)
            new_donor = False
            break
    if new_donor:
        donors.append((name, [donation]))
    print(print_thank_you_email(name, donation)) #print thank you email


def print_thank_you_email(name, donation):
    print()
    print(f"Dear {name}:")
    print(f"\nThank you for the donation of ${donation:,.2f}.")
    print("\nRegards,")


def donor_report(): # this works without adding any donors
    donor_summary = []
    for person in donors:
        name = person[0]
        total_given = sum(person[1])
        times_donated = len(person[1])
        avg_gift = total_given / times_donated
        donor_summary.append([name, total_given, times_donated, avg_gift])
    headers = ["Donor Name", "Total Given", "Times Donated", "Average Gift"]
    print()
    print("{:17} | {:>20} | {:>15} | {:>19}".format(headers[0], headers[1], headers[2], headers[3]))
    print("-" * 80)
    for x in donor_summary:
        print("{:17} |  ${:>18,.2f} | {:>15} |  ${:>17,.2f}".format(x[0], x[1], x[2], x[3]))






def letter_to_all_donors():
    pass
    # iterate over each donor and create a thank you email for a single donor(as in def print thank you email)
    # convert the program output to a text file
    # do this for each donor








def exit_program():
    print("The program is over, thank you.")
    sys.exit()


if __name__ == "__main__":
    main()