"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
Session 9 OOP Mailroom


directions found at:
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-oo.html

-Three main classes:
    1.  class Donor():
    - This class will hold all the information about a single donor - and have attributes,
    properties, and methods to provide access to the donor specific information that is 
    needed.  If code is being written that only access information about a single donor - 
    then it should be here.  
    - Anything that needs to know about one donor goes here.
    - *No input, no user interaction.* 

    2.  class Donor_Collection():
    - This class will hold the donor objects, as well as methods to add a new donor, search 
    for a given donor, etc.  If you want to save and re-load data, this class would hold that
    method.
    - Anything that needs to know about the collection goes here.
    - This class holds the code that generates reports about multiple donors
    - *No input, no user interaction.* 

    3.  class cli_main():
    -This is entry point for the program; it will handle the input and console output.  This 
    module will be using the classes listed above.
    - What goes in here: main "switch dictionary."
"""



from donor_models import *



def thank_to_all():
    dc.send_thank_to_all()
    list_of_donors = dc.list_donors
    print(f"The thank you letters for {list_of_donors} have been sent")


def make_report():
    data = dc.report_data
    # sort the data
    data.sort(key=lambda tup: tup[0])
    # format
    print("{:20s} | {:11s} | {:9s} | {:12s}".format(
          "Donor's Name", "Total Donated", "Number of Donations", "Average$"))
    for row in data:
        print("{:20s}   {:11.2f}   {:9d}   {:20.2f}".format(*row))


def thank_you():
    # ask user for donor's name
    while True:
        # add exception
        try:
            name = input("Enter a donor's name "
                        "(or 'list' to see all donors or 'menu' to exit)>")
        except (KeyboardInterrupt, EOFError):
            return None
        if name == "list":
            print(dc.list_donors)
        elif name == "menu":
            return
        else:
            break


    # ask user for donation amount
    while True:
        # add exception
        try:
            dollar = input("Enter a donation amount (or 'menu' to exit)>")
        except (KeyboardInterrupt, EOFError):
            return None
        if dollar == "menu":
            return
        # add exception
        try:
            dollar = float(dollar)
        except ValueError:
            print("Input must be a number")
        else:
            break


    donor = Donor(name)
    donor.add_donation(dollar)
    # add new name and donation amount to the donors history
    dc.add_donor(donor.name, donor.donations)
    # print the thank you letter
    d = donor.thank_you_data

    print("Dear {d_name},\n\n    Thank you for your donation of ${d_dollar}.\n\nRespectfully".format(**d))


#this is main driver for the program
def main():
    print("\nWelcome to the Mailroom\n", "{:_<20}".format("_"))
    answer = ""
    while answer != "q":
        print("\nPlease select from the following:")
        print("'q': Quit,\n't': Send Thank You to single donor\n'r': Donor Report\n's': Send Thank You to all donors")
        try:
            answer = input(" > ")
        except (KeyboardInterrupt, EOFError):
            return None
        answer = answer.strip()
        answer = answer[:1].lower()
        if answer == 't':
            thank_you()
        elif answer == 'r':
            make_report()
        elif answer == 's':
            thank_to_all()

donors = {"Javier Bardem":[1000, 800, 4000],
          "Pino Aprile": [200, 400, 1000],
          "Oprah Winfrey": [10000, 20000],
          "Peter Voss": [3000, 200, 1500],
          "Luciano Pavarotti": [2000, 750, 3000]
          }

if __name__ == "__main__":

    dc = DonorCollection()
    dc.add_old_donors(donors)
    main()

