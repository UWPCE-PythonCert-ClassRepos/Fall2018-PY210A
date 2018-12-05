#Lesson03
#Mailroom Project that includes the Exceptions Lab (using a safe_input function)
#
#!/usr/bin/env python3
#import libraries
from textwrap import dedent
from pathlib import Path
from sys import exit
import os

#define variables -
global choice
choice = ""
#data_folder = Path("C:\pythonuw\Fall2018-PY210A\students\ericstreit\files")
data_folder = r'C:\pythonuw\Fall2018-PY210A\students\ericstreit\files'

# create donor list
donors = {"Anna Fang": [23.53, 5000],
          "Tom Natsworthy": [99, 783, 3],
          "Hester Shaw": [5, 92, 101.23],
          "Hester Shaw": [5, 92, 101.23],
          "Katherine Valentine": [1000, 2000, 3000],
          "Grike": [1]}


# create menu dictionaries ARE BOTTOM OF THE PAGE

#define functions
def safe_input():
    """ input with built in try function to handle error handling """
    try:
        global choice
        choice = input(": ")
        #removes any spaces in the choice
        choice = choice.strip()
        #takes the first letter of the choice and makes it lower case
        choice = choice[0:1].lower()
    #except KeyboardInterrupt as the_error:
        #print("I believe that is an error")
        #print(the_error)
    except IOError:
        print("error")
    except KeyboardInterrupt:
        quit()

def thank_you():
    """This is the thank you menu that routes to the listuser or donor_update function"""
    print("Type 'thank' to send a Thank you to a single donor, 'all' to send a thank you to all donors or 'list' to list current donors.")
    safe_input()
    menu_choice(thankyou_dict, choice)

def bad_choice():
    """ returns if a valid menu input is not given"""
    print("I did not understand, please try again!")

def send_all():
    """ sends a thank you to all donors """
    print("sending a 'Thank You' to all donors!")
    for donor in donors:
        amount = sum(donors.get(donor))
        file_write(donor, amount)
        #print(compose_email(donor, amount))


def send_one():
    """ creates a single thank you, generating a printed email on screen """
    name = input("Enter name of the donor to thank: ")
    money = float(input("Enter how much money they donated: "))
    if donor_find(name) != True:
        donor_add(name, money)
    else:
        donor_contribute(name, money)
    print(compose_email(name, money))

def donor_contribute(name, money):
    """ updates the db with money the donor contributed """
    money_list = [money]
    money_update = donors.get(name) + money_list
    donors[name] = money_update

def list_donors():
    """A simple function that lists donor names"""
    print("\nDonors\n", "{:-<60}".format(""))
    for donor in donors:
        print(donor)

def compose_email(name, amount):
    """This function composes the thank you email txt"""
    return dedent('''
    \n\nEMAIL SENT:\n
    Dear {},
    Thank you for your generous contribution of ${:.2f}! We will be sure to ask you for more money again soon.

    Sincerely,
    Donations, Inc'''.format(name, amount))

def file_write(donor, amount):
    """This function will call upon the compose_email function and then write the contents to a file with the donors name"""
    #replaces whitespace with underscores and add the .txt extension to the end. Stolen from teacher :)
    filename = donor.replace(" ", "_") + ".txt"
    data_file = os.path.join(data_folder, filename)
    with open(data_file, 'w') as outfile:
        outfile.write(compose_email(donor, amount))
    outfile.close

def donor_find(name):
    """This function will search for a donor in the db and return True if found """
    if name in donors:
        return True

def donor_add(name, money):
    """This function simply adds a donor to the db and the amount of money donated"""
    donors[name] = [money]

def report():
    """This is the reporting function"""
    print("\n", "\n", "{:<25}{:5}{:5}{}".format("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"))
    print("{:-<80}".format(""))
    for donor in donors:
        print("{:<26} ${:<11.2f} {:<11} ${:.2f}".format(donor, sum(donors[donor]), len(donors[donor]), sum(donors[donor]) / len(donors[donor])))

def menu_choice(dict, choice):
    """ function that calls the menu an choice """
    try:
        dict.get(choice)()
    except TypeError:
        print("That is not a valid selection!")

def mainmenu():
    """This is the main menu of the mailroom project part 1"""
    print(" \n\nHello and Welcome to MAILROOM!\n",
          "{:-<30}".format("-"))
    while choice != "q":
        print("\n\nWould you like to (S)end a Thank You, Run a (R)eport or (Q)uit?")
        #choice = safe_input(": ")
        safe_input()
        menu_choice(menu_dict, choice)

def quit():
    """function to quit the program"""
    print("Goodbye!")
    exit()


#define dictionaries
#note must have this AFTER the mainmenu function otherwise generates an error since the functions havne't been made yet
menu_dict = {'s':thank_you,'r':report,'q':quit}
thankyou_dict = {'l':list_donors, 'a':send_all, 't': send_one, 'q':quit}

#for testing
if __name__=="__main__":
    #report()
    mainmenu()
    #listusers()
