"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
Mailroom Assignment - Session 3 / first draft - still more work to be done
"""

import sys

donors = [("Javier Bardem", [1000, 800, 4000]),
          ("Pino Aprile", [200, 400, 1000]),
          ("Oprah Winfrey", [10000, 20000, ]),
          ("Peter Voss", [3000, 200, 15000]),
          ("Luciano Pavarotti", [2000, 750, 3000])]

def donor_list():
    print("-- Donors --")
    for i in donors:
        print(i[0])

def add_new_donor():
    new_donor = input("Enter the name of a new donor: ").title()
    donors.append(new_donor)
    print(donors)
    donation_amount = input("Please enter the donation amount of the new donor: ") #format this using string formatting
    donors.append(donation_amount)
    print(donors)

def thank_you_email():
    print("\nEmail Sent:\nThank you for your donation")
    #use string formatting like Thank you {}, for your donation of ${}".format(link to name and amount)

def thank_you():
    #print("Thank You")
    print("Select '1' view complete donor list, or '2' enter a full name of an individual donor, or '3' send Thank You Email.")
    user_selection = input("> ")
    if user_selection == "1":
        donor_list()
    #elif user_selection == "2":
        #full_name == input("> ")
        #print(full_name)
    elif user_selection == "3":
        thank_you_email()
    else:
        add_new_donor() #this needs to go under item 2, where a donor report is created or modified

def donor_report():
    pass

def exit_program():
    print("The program is over, thank you.")
    sys.exit()

#this is the main function that drives the program
def main():
    print("\nWelcome to the Mailroom\n", "{:_<20}".format("_"))
    #donors = ""
    running = True
    while running:
        print("\nMailroom Options - Please respond by typing 1, 2, or 3, and press enter\n")
        print("1) Send a Thank You Email")
        print("2) Create a Donor Report")
        print("3) Quit")
        option = input("> ")
        if option == "1":
            thank_you()
        elif option == "2":
            donor_report()
        elif option == "3":
            exit_program()

if __name__ == "__main__":
    main()
