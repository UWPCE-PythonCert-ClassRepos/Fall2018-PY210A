#Lesson09
#Objected Oriented Mailroom Exercise 09 - Classes
#
#!/usr/bin/env python3
from textwrap import dedent
from pathlib import Path
from sys import exit
import os


# define any global variables or datasets
donor_dict = {}
data_folder = r'C:\pythonuw\Fall2018-PY210A\students\ericstreit\files'



# define classes and functions

class Donors():
    def __init__(self, name, donations=0):
        self.name = name
        self.donations = [donations]
        self.last_donation = 0

    def __str__(self):
        # format the name so that it is all one lowercase string without spaces.
        # return this value. Note to self, it seems like this could be used for
        # something useful but I'm not really taking advantage of it.
        return self.str_name(self.name)

    def __repr__(self):
        # omg I should have added this earlier!!! really killed some time trying
        # to troubleshoot something. Hey, now I know!
        return self.str_name(self.name)

    def str_name(self, name):
        # yeah, I could prob incorporate this all in the  __str__ function above couldn't I?
        # Also, I don't think I'm using this anymore......I think donor_name_format
        # replaced this. Why did I do that again?
        name = name.lower()
        name = name.replace(" ", "")
        return name

    # so some of these may be better as class methods? I don't 100% understand
    # those yet but this works for now.

    def add_donations(self, new_donation):
        self.donations.append(new_donation)
        self.last_donation = new_donation
        return self.donations

    def sum_donations(self):
        # yeah, this seems unneeded? Do I use it anywhere???
        return sum(self.donations)

    def avg_donations(self):
        return self.sum_donations() / len(self.donations)

    def thank_you(self):
        # generates the snarky thank you email text
        """This function composes the thank you email txt"""
        return dedent('''
        \n\nEMAIL SENT:\n
        Dear {},\n
           Thank you for your recent donation of ${:.2f}! We will be sure to ask you for more money again soon.

        Sincerely,
        Donations, Inc'''.format(self.name, self.last_donation))


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

        print("-------------------------------------------\n")
        print("\n{}\n".format(self.menu_name))
        print("\nPlease select from the following choices\n")
        print("-------------------------------------------\n")
        for option in self.menu_options:
            print(option)
        # use the safe input function here
        self.menu_input()


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
        """ function that calls the menu providing the argument choice which should
            correspond to a key/value pair in the menu dict"""
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
        #this function feels pretty long, I feel like I could clean up and make some of
        #this stuff additional functions?
        print("Enter the donors name")
        display_name = self.name_input()
        #pass the user imput to our formatter to make the string our standard
        #db naming convention
        format_name = self.donor_name_format(display_name)
        #now check to see if the donor exists in the db. If not, then pass to
        #the function that creates new donor objects
        if not self.donor_exists(format_name):
            self.donor_add(format_name, display_name)
        #now let's update that donor object with the amount they donated
        print("Please enter the amount the donor donated")
        money = self.donation_input()
        #ok now we need to convert that donor string to the instnace object
        obj_name = self.get_obj_name(format_name)
        #we can now pass that object as an argument to the next function which
        #will update the instance attribute list that contains donations
        obj_name.add_donations(money)
        self.menu()

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
            money = float(int(input(": ")))
        except ValueError:
            print("Please enter a valid ammount (ie $100, or $99.99)")
            self.menu()
        except:
            print("Please enter a valid ammount (ie $100, or $99.99)")
            self.menu()
        return money


    def donor_name_format(self, name):
        #format the name so that it is all one lowercase string without any spaces. return this value
        name = name.lower()
        name = name.replace(" ", "")
        return name

    def donor_exists(self, format_name):
        #return True or False if the argument (which should be the formatted
        #name of the donor) is in the donor_dict db as a key
        return format_name in donor_dict

    def donor_add(self, format_name, display_name):
        #take the formatted name value and create an instance of it
        format_name = Donors(display_name)
        #convert back that
        donor_dict[str(format_name)] = format_name

    def add_donations(self, obj_name, money):
        obj_name.add_donations(money)

    def get_obj_name(self, format_name):
        #the donor_dict db contains a key value of the donor. The key being the
        #formatted name 'johnsmith' (which is a string) and the value being the
        #object instance name johnsmith. This function is to basically convert
        #a variable string into the object. It does this by returning the value
        #(which is an object) of the key (which is the string)
        return donor_dict.get(format_name)

class ThankYou(Menu):

    def single_donor_thankyou(self):
        print("Please enter the name of the donor you would like to thank.")
        display_name = self.name_input()
        format_name = self.donor_name_format(display_name)
        if not self.donor_exists(format_name):
            print("I was not able to find that donor!")
            self.menu()
        obj_name = self.get_obj_name(format_name)
        self.file_write(format_name, obj_name)
        print("Thank you sent to {}!".format(format_name))
        self.menu()

    def all_donor_thankyou(self):
        for donor in donor_dict:
            obj_name = self.get_obj_name(donor)
            self.file_write(donor, obj_name)
            print("A Thank You email has been sent to all donors!")
        self.menu()


    def file_write(self, format_name, obj_name):
        """This function will call upon the compose_email function and then write
        the contents to a file with the donors name"""
        #replaces whitespace with underscores and add the .txt extension to the end. Stolen from teacher :)
        filename = format_name.replace(" ", "_") + ".txt"
        data_file = os.path.join(data_folder, filename)
        with open(data_file, 'w') as outfile:
            outfile.write(obj_name.thank_you())
        outfile.close


class Report(Menu):

    def full_donor_report(self):
        """ This menu function will print out an entire report consisting of all
        donors.
        """
        self.donor_report_header_display()
        for item in donor_dict:
            obj_name = self.get_obj_name(item)
            self.donor_report_detail(obj_name)
        self.menu()

    def single_donor_report(self):
        """ This menu function will print out a single report for a donor."""
        print("Please enter the name of the donor you are looking for")
        #grabs the
        display_name = self.name_input()
        #formats the inputted string to our standard db naming convention
        format_name = self.donor_name_format(display_name)
        #checks to see if the donor exists
        if not self.donor_exists(format_name):
            print("I was not able to find that donor!")
            self.menu()
        #if it exists we now need to convert the formatted string to the object instance
        obj_name = self.get_obj_name(format_name)
        #now let's print the report, first showing the header
        self.donor_report_header_display()
        #and now printing the object instances values
        self.donor_report_detail(obj_name)
        input("Press any key to continue")
        self.menu()

    def donor_report_header_display(self):
        #prints out the header on a report
        print("\n", "\n", "{:<25}{:5}{:5}{:5}{}".format("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift", "| Last Gift"))
        print("{:-<80}".format(""))

    def donor_report_detail(self, obj_name):
        #prints out a donors contributions details, which coincide with the
        #donor_report_header_display function
        print("{:<26} ${:<11.2f} {:<11} ${:<11.2f} ${:.2f}"
               .format(obj_name.name, sum(obj_name.donations), (len(obj_name.donations) -1),
               sum(obj_name.donations) / (len(obj_name.donations) -1),
               obj_name.last_donation))



#for testing
if __name__=="__main__":
    pass
