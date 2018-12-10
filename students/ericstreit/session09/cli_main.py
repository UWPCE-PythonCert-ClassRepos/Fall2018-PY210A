#Lesson09
#Objected Oriented Mailroom Exercise 09 - CLI Menu
#
#!/usr/bin/env python3
#importe modules
from donor_models import *
from pathlib import Path
from sys import exit
import os

#define variables

data_folder = r'C:\pythonuw\Fall2018-PY210A\students\ericstreit\files'

#define menus
# This creates the menu as a class

main_menu  = Menu("Main Menu")
report_menu = Menu("Report Menu")
thankyou_menu = Menu("Send a Thank You")

# define menu options
# These are the choices that will display to the user in a menu
# Be sure to create a dictionary below that will tie to the choices

main_menu.menu_options = ["(R)eport Menu", "(S)end a Thank You",
                          "(A)dd a new donation",
                          "(Q)uit"]


report_menu.menu_options = ["Create report of (A)ll donors",
                            "Create report of a (S)ingle donor",
                            "(B)ack to Main Menu",
                            "(Q)uit"]



thankyou_menu.menu_options = ["Send a Thank You to a (S)ingle donor",
                              "Send a Thank You to (A)ll donors",
                              "(B)ack to Main Menu",
                              "(Q)uit"]



#define the menu dictionaries
#each selection should point to a function

main_menu.dict = {"r": report_menu.menu, "s": thankyou_menu.menu, "q": main_menu.quit}
report_menu.dict = {"a": main_menu.menu, "s": main_menu.menu, "b": main_menu.menu, "q": report_menu.quit}
thankyou_menu.dict = {"a": main_menu.menu, "s": main_menu.menu, "b": main_menu.menu, "q": thankyou_menu.quit}

#define additional functions

# run the program!

main_menu.menu()

#for testing
if __name__=="__main__":
    main_menu.menu
