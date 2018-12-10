#Lesson09
#Objected Oriented Mailroom Exercise 09 - Classes
#
#!/usr/bin/env python3
from textwrap import dedent
from pathlib import Path
from sys import exit
import os


# define any global variables or datasets
donor_list = ["hestershaw"]

#define classes and functions

class Donors():
    def __init__(self, name):
        self.name = name
        self.donations = []
        #master_list = []

    def __str__(self):
        return "Donor, {}, with a total donation amount of: ${}".format(self.name, self.sum_donations)

    def add_donations(self, new_donation):
        self.donations.append(new_donation)
        return self.donations

    def sum_donations(self):
        return sum(self.donations)

    def avg_donations(self):
        return self.sum_donations() / len(self.donations)

    def thank_you(self):
        """This function composes the thank you email txt"""
        return dedent('''
        \n\nEMAIL SENT:\n
        Dear {},\n
           Thank you for your generous contributions totalling ${:.2f}! We will be sure to ask you for more money again soon.

        Sincerely,
        Donations, Inc'''.format(self.name, self.sum_donations()))


class Menu():
    """
    Root Menu class containg display name and pointers to dictionary containing functions.
    """
    def __init__(self, name):
        self.menu_name = name
        self.menu_options = {}
        self.dict = {}

    def menu(self):
        """ Takes no arguments. This is the menu screen that folks see. It calls upon the menu class object
        which in turn displays the menu choices available and then calls the safe
        input function to take the choice """

        print("\n{}\n".format(self.menu_name))
        print("-------------------------------------------\n")
        print("\nPlease select from the following choices\n")
        print("-------------------------------------------\n")
        for option in self.menu_options:
            print(option)
        #use the safe input function here
        self.menu_input()
        #self.menu_choice(choice)


    def menu_input(self):
        """ Takes no arguments. Menu choice input with built in try function to handle error handlingself.
        Formats the choice to a single lower case letter and passes that letter to the
        menus dictionary which should contain a matching key with a corresponding
        function to call as a value """
        try:
            #the formmating could be made as its own function?
            choice = input(": ")
            #removes any spaces in the choice
            choice = choice.strip()
            #takes the first letter of the choice and makes it lower case
            choice = choice[0:1].lower()
            #except KeyboardInterrupt as the_error:
                #print("I believe that is an error")
                #print(the_error)
            self.menu_choice(choice)
            #return choice
        except IOError:
            print("error")
        except KeyboardInterrupt:
            quit()


    def menu_choice(self, choice):
        """ function that calls the menu an choice """
        try:
            self.dict.get(choice)()
        except TypeError:
            print("That is not a valid selection!")
            self.menu()


    def quit(self):
        """Takes no arguments. Function to quit the program, self explanatory"""
        print("Goodbye!")
        exit()

    def new_donation(self):
        """ this calls the donor input function """
        print("Enter the donors name")
        display_name = self.name_input()
        print("This is the Display name: {}".format(display_name))
        format_name = self.donor_name_format(display_name)
        print("Formatted name is: {}".format(format_name))
        if not self.donor_exists(format_name):
            self.donor_add(format_name, display_name)
        print(donor_list)
        print("Please enter the amount the donor donated")
        money = self.donation_input()
        self.add_donation_to_donor(format_name, money)
        #input here to take the integer for donation ammount, pass to the add_donations function below
        #format_name.add_donations()
        #check if the name exists if donor_exists == True then go to the add sum
        #check if the name already exists, if so skip to the function that adds donations to the donors list
        #if name does not exist append the string to the master donor list

        #create the class object using the formatted string and pass the original input as an argument

        #send to a new input function (pass the formatted donor name ) which will add the amount to the donors lists
        #using the self.add_donations function
        x = input("Press any key to continue")

    def name_input(self):
        name = input(": ")
        if name != "":
            return name
        else:
            print("Nothing entered, back to main menu!")
            self.menu()
        #self.donor_name_format(name)

    def donation_input(self):
        try:
            money = int(input(": "))
        except:
            print("Please enter a valid ammount (ie $100, or $99.99)")
            donation_input()
        return money


    def donor_name_format(self, name):
        #format the name so that it is all one lowercase string without spaces. return this value
        name = name.lower()
        name = name.replace(" ", "")
        return name

    def donor_exists(self, format_name):
        #global donor_list
        return format_name in donor_list

    def donor_add(self, format_name, display_name):
        donor_list.append(format_name)
        format_name = Donors(display_name)

    def add_donation_to_donor(self, donor, money):
        donor.add_donations(money)
        print(donor.donations)


class ThankYou(Menu):

    def donor_report(self):
        print("just testing this")





class Report(Menu):

    def donor_report(self):
        print("just testing this")














#sending thank yous
#for all donors (easy) just loop through the master list and call the self function
#but you need to create the file writing piece for That

#reporting part
#for all donors loop through the master list and return the self functions



#for testing
if __name__=="__main__":
    pass
