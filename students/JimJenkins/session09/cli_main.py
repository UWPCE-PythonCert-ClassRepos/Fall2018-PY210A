#!/usr/bin/env python3

"""
Author: Jim Jenkins
Date: 12/10/2018

Description: menu for mail room.
"""

import sys

from .mailroom import Donor, Donor_collection

#menu system
menu = {}
menu['1'] = 'Send a thank you'
menu['2'] = 'Create a Report'
menu['3'] = 'Quit'



#TODO refactor
while True:
    options = menu.keys()

    for entry in options:
        print(entry, menu[entry])
    print(' ')
    selection = input("Please select an option number: ")
    print(' ')
    if selection == '1' :
        donor_thankyou_letter()
        break
    elif selection == '2':
        #create_report()
        break
    elif selection == '3':
        quit()
        break
    else:
        print('Unknown option selected')
        print(' ')

def quit():
    sys.exit(0)


if __name__ == '__main__':
    main()







