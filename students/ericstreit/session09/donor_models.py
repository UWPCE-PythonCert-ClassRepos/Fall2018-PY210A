#Lesson09
#Objected Oriented Mailroom Exercise 09 - Classes
#
#!/usr/bin/env python3
from textwrap import dedent
from pathlib import Path
from sys import exit
import os

#define classes and functions
class Donors():
    def __init__(self, name):
        self.name = name
        self.donations = []

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
    Menu class containg name and pointer to dictionary containing functions
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
        self.safe_input()



    def safe_input(self):
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





#for testing
if __name__=="__main__":
    pass
