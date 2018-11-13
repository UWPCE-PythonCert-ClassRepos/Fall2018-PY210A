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
            donation_amount = int(input('\nHow much was contributed?: '))
            add_donation(donor_name, donation_amount)
            create_email(donor_name, donation_amount)
            break
        #donor not in list
        elif donor_name not in donation_list:
            add_donor(donor_name)
            donation_amount = int(input('\nHow much was donated?: '))
            add_donation(donor_name, donation_amount)
            create_email(donor_name, donation_amount)
            break


def create_report():
    print(menu['2'])
    return report_creator()


def quit():
    print(menu['3'])
    sys.exit()


def add_donor(a):
    indicator = False
    for i, donor in enumerate(donation_list):
        if a == (donation_list[i][0]):
            indicator = True

    if(indicator == False):
        donation_list.append(a)
        print('Added', a, 'to the donors list.')


def add_donation(a, b):
    for i, donor in enumerate(donation_list):
        if a == (donation_list[i][0]):
            donation_list.append(b)
    print('Added ${:.2f} to the donation list for {}.'.format(b, a))


def create_email(a, b):
    print('\n\nDear {}: '
          '\n\nThank you for your contribution of ${:.2f}. Your donation will help.'
          '\n\nSincerely, The Non-Profit'.format(a, b))
    print(donation_list)


def average(a):
    return sum(a) / len(a)


def count(a):
    return len(a)


def report_creator():
    print(' ')
    print("{:<20} | {:^16} | {:^16} | {:^17}".format('Donor Name:', 'Total Given:', 'Num Gifts:', 'Average Gift:'))
    print('=' * 80)
    for i, donor in enumerate(donation_list):
        user = donation_list[i][1]
        print('{:<20} | ${:>15,.2f} | ${:>15,.2f} | {:^15}'.format(donation_list[i][0], sum(user), average(user), count(user)))


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
    main()
