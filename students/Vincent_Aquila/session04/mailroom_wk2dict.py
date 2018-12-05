"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
Mailroom Assignment - week 2 / session 04 - with dictionary - not finished yet
"""


 #import sys - was used in previous program, but not needed here since def menu_selection contains a break statement


donors = {"Javier Bardem" : [1000, 800, 4000],
          "Pino Aprile" : [200, 400, 1000],
          "Oprah Winfrey" : [10000, 20000],
          "Peter Voss" : [3000, 200, 15000],
          "Luciano Pavarotti" : [2000, 750, 3000]
          }


print("\nWelcome to the Mailroom\n", "{:_<20}".format("_"))


#this is the main function that drives the program
def menu_selection(prompt, menu_dict):
    while True:
        response = input(prompt)
        if menu_dict[response]() == "exit menu":
            break


def donor_list():
    print("-- Donors --")
    for k in donors: 
        print(k)   

def add_new_donor():
    pass

def thank_you():
    print("This will send a Thank You Email.")


def donor_report(): #needs formatting, but prints the dictionary
    print("This will create a donor report.")
    print("-- Donors --")
    for k, v in donors.items(): 
        print("%s: %s" % (k,v))    

def exit_program():
    print("The program is over, thank you.")
    #sys.exit() - not needed in this program because the import sys is removed, since def menu_selection contains a break statement 
    return "exit menu"

def sub_menu():
    menu_selection(sub_prompt, sub_dispatch)

def send_thank_you_email():
    pass

def letter_to_all_donors():
    pass
    # iterate over each donor and create a thank you email for a single donor(as in def print thank you email)
    # convert the program output to a text file
    # do this for each donor


main_prompt = ("\nYou are in the main menu now.\n"
               "\nPress 1 for list of donors, add a new donor, or send a thank you email.\n"
               "Press 2 for a donor report.\n"
               "Press 3 to send a thank you letter to all donors.\n"
               "Press e to exit the program."
               )


main_menu_dict = {"1" : sub_menu,
                  "2" : donor_report,
                  "3" : letter_to_all_donors,
                  "e" : exit_program
                  }


sub_prompt = ("\nYou are in a sub menu now.\n"
              "\nPress 1 for a list of donors.\n"
              "Press 2 to add a new donor.\n" 
              "Press 3 to send a thank you email to a single donor.\n"
              #"Press q to return to the main menu.\n"
              "Press e at any time to return to the main menu."
              )


sub_dispatch = {"1" : donor_list,
                "2" : add_new_donor,
                "3" : send_thank_you_email,
                #"q" : 
                "e" : exit_program
                }

"""
#from previous program

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
"""

if __name__ == "__main__":
    menu_selection(main_prompt, main_menu_dict)