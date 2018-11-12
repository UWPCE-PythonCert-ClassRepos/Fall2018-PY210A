#!/usr/bin/env python3

"""
Author: Jim Jenkins (dvlupr)
Date: 11/05/2018

"""
#import modules
import sys


#donor database (in dict structure)
donation_list = [('John Roberts', [100, 200, 300]),
                ('Clarence Thomas', [200, 400, 600]),
                ('Ruth Bader-Ginsberg', [700, 100, 2000]),
                ('Elena Kagen', [1800, 2300, 7000]),
                ('Sonia Sotomayor', [500, 190, 212, 55]),
                ('Neil Gorsuch', [100, 3000]),
                ('Brett Kavanaugh',[400, 4500]),
                ('Samuel Alito', [1000, 1000, 1000]),
                ('Stephen Breyer', [200, 300, 10000])]


menu = {}
menu['1'] = 'Send a thank you'
menu['2'] = 'Create a Report'
menu['3'] = 'Quit'


#functions
def main():
    pass


def send_thankyou():
    print(menu['1'])
    #donor name information
    while True:
        donor_name = str(input('\nWho would you like to send a thank you note to?: '))
        #show list
        if donor_name == 'list':
            for i, donor in enumerate(donation_list):
                print(donation_list[i][0])
        #donor in list
        elif donor_name in donation_list:
            donation_amount = input('\nHow much was contributed?: ')
            add_donation(donor_name, donation_amount)
            create_email(donor_name)
            break
        #donor not in list
        elif donor_name not in donation_list:
            add_donor(donor_name)
            donation_amount = input('\nHow much was donated?: ')
            add_donation(donor_name, donation_amount)
            create_email(donor_name)
            break


def create_report():
    print(menu['2'])

    print("{} | {} | {} | {}".format('Donor Name:', 'Total Given:', 'Num Gifts:', 'Average Gift:'))
    for donor in donation_list:
        print('{:<15}   ${:>9,.2f}'.format(donor['name'], donor['donation_amount']))

    return


def quit():
    print(menu['3'])
    sys.exit()


def add_donor(a):
    #donation_list{0][1] = 'Clarence Thomas'
    #if donation_list[0][1] == a
    #donation_list[1][1].append(donation)

    if a not in donation_list:
        donation_list.append(a)
        print('Added', a, 'to the donors list.')


def add_donation(a, b):
    if a in enumerate(donation_list):
        donation_list.append(b)


#donation_list[3][1].append(donation)

def create_email(a):
    print('create email', a)


#menu
print('MAILROOM v1.0')


#menu logic
while True:
    options = menu.keys()

    for entry in options:
        print(entry, menu[entry])
    print(' ')
    selection = input("Please select an option number: ")
    print(' ')
    if selection == '1' :
        send_thankyou()
        break
    elif selection == '2':
        create_report()
        break
    elif selection == '3':
        quit()
        break
    else:
        print('Unknown option selected')
        print(' ')


if __name__ == '__main__':
    #main()
    '''
    print('<<<<< unit tests >>>>>>')
    assert show_list('yes') is None
    assert show_list('no') is None
    assert search_donors('Clarence Thomas') is None
    assert search_donors('clarence Thomas') is None
    assert search_donors('Robert Bork') is None
    assert search_donors('Ruth Bader Ginsberg') is None
    assert add_donor('Sandra Day Oconnor') is None
    print(donor_list)
    assert get_donation_amount(200.00)is None
    '''


"""
#from class discussion

def menu_selection(prompt, dispatch_dict):
    while True: #runs until quit is selected
        response = input(prompt)
        response = response[:1].lower()
        If dispatch_dict.get(response, unknown)() == 'exit menu'
            break

main_dispatch = 

"""