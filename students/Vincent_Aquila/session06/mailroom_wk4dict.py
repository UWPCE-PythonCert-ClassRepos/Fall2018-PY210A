"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
Mailroom Assignment - part 4 / session 06 - with dictionary structure and tests
"""


"""
Objectives:
- Create a program that will generate thank you letters showing:
    donor's name and donation amount
- Initial display menu offers:
    -list of donors, adding a new donor, or sending a thank you email
    -generate donor report
    -send a thank you email to all donors (auto-generated file creation)
- Submenu offers:
    first option above broken down into three options 

*** This program uses a dictionary look-up method (see main_prompt, sub_prompt).  

There are still program bugs.

Previous non-dictionary look-up format program works, but prefer to make 
dictionary style look-up work.  On verge of abandoning this program for 
non-dictionary style look-up program.             


*** Note to self - keep to PEP8 - program lines no longer than 78 characters
"""




"""
import sys - was used in previous program, but not needed here since
def menu_selection contains a break statement
"""


import os

from textwrap import dedent #text formatting into a string


def record_donor_db():
    return {"javier bardem": ("Javier Bardem", [1000, 800, 4000]),
            "pino aprile": ("Pino Aprile", [200, 400, 1000]),
            "oprah winfrey": ("Oprah Winfrey", [10000, 20000]),
            "peter voss": ("Peter Voss", [3000, 200, 15000]),
            "luciano pavarotti": ("Luciano Pavarotti", [2000, 750, 3000]),
            }

#program header
print("\nWelcome to the Mailroom\n", "{:_<20}".format("_"))


donor_db = record_donor_db()


#this is the main function that drives the program
def menu_selection(prompt, menu_dict):
    while True:
        response = input(prompt)
        response = response[:1].lower()
        if menu_dict.get(response, unknown)() == "exit menu":
            break


#this returns a list of donors, then returns to the submenu
def donor_list():
    #convert to a list, so append function can be used
    list_of_donors = ["-- Donors --"] 
    for donor in donor_db.values():
        list_of_donors.append(donor[0])
    print(list_of_donors)
    return "\n".join(list_of_donors)      
        

def add_new_donor():
    """
    selection 1 in main_menu_dict - then 2 in sub_dispatch leads here 
    
    this is the first time the variable 'name' for a new donor is introducted 
    in the program
    'name' will be passed through various functions throughout the program
    
    this is the first time the variable 'donation_amount' (of the new donor) 
    is introduced in the program
    'donation_amount' will be passed through various functions throughout the 
    program
    """
    name = input("Please enter the name of a new donor: ")
    """
    add_new_donor function is a bridge function between the sub_dispatch menu  
    and register_new_donor function
    """
    register_new_donor(name)


def register_new_donor(name):
    while True:
        donation_amount = input("Please enter a donation amount (or 'menu' to exit): ").strip() 
        if donation_amount == "menu":
            return 
        """
        variable name is passed through the find_donor and add_donor functions
        
        variable 'name' and variable 'donation_amount' describe a donor and their donation 
        which returns as the new variable called 'donor' 
        """
    donor = find_donor(name)
    if donor is None: 
        donor = add_donor(name)
    #a new donor's name will not be found in the donor db, thus new donors are set equal to None
    donor[1].append(donation_amount)

    print(create_thankyou_letter(donor))


def find_donor():
    key = name.strip().lower()
    return donors.get(key)


def add_donor():
    name = name.strip()
    donor = (name, [])
    donors[name.lower()] = donor
    return donor        
                

def create_thankyou_letter(donor):
    return dedent ("""Dear{0:s},

            Thank you for your generous donataion of ${1:.2f} to the Neighborhood Food Bank.
            We rely on donations such as this for continued operation.

                                  Best Regards,
                                  The Neighborhood Food Bank
            """.format(donor[0], donor[1][-1]))   


def donor_report():
    """
    this creates a report showing the donor and the amount donated    
    """  
    report_rows = []
    for (name, gifts) in donor_db.values():
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))
        

    report_rows.sort(key = sort_key)
    report = []
    report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                            "Total Given",
                                                            "Num Gifts",
                                                            "Average Gift"))
    report.append("-" * 66)
    for row in report_rows:
      report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
    return "\n".join(report)


def sort_key(item):
    return item[1]

 
def letter_to_all_donors():
    for donor in donor_db.values():
        letter = create_thankyou_letter(donor)
        filename = donor[0].replace(" ", "_") + ".txt"
        print("writting letter to:", donor[0])
        open(filename, 'w').write(letter)
    

#in case a number other than a menu selection is entered, this redirects the user
def unknown():
    print("That was not a valid response, please enter a number from the menu.")
    return None


def exit_program():
    print("The program is over, thank you.")
    """
    sys.exit() - not needed in this program because the import sys is removed, 
    since def menu_selection contains a break statement 
    """
    return "exit menu"


def sub_menu():
    menu_selection(sub_prompt, sub_dispatch)


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
              "Press e at any time to return to the main menu."
              )


sub_dispatch = {"1" : donor_list,
                "2" : add_new_donor, 
                "e" : exit_program
                }


if __name__ == "__main__":

    
    menu_selection(main_prompt, main_menu_dict)


    #assertion test:
    assert record_donor_db("javier bardem") is not None
    assert record_donor_db("pino aprile") is not None
    print("All tests passed.")


    