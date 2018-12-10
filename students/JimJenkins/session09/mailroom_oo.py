#!/usr/bin/env python3

"""
Author: Jim Jenkins
Date: 12/10/2018

Description: Object oriented version of mail room.
"""

import sys


"""
sample data (remove when ready)
"""


donor_datastore = {'Samuel Alito': [1000, 1000, 1000],
                   'Ruth Bader-Ginsberg': [700, 100, 2000],
                   'Stephen Breyer': [200, 300, 10000],
                   'Neil Gorsuch': [100, 3000],
                   'Elena Kagen': [1800, 2300, 7000],
                   'Brett Kavanaugh': [400, 4500],
                   'John Roberts': [100, 200, 300],
                   'Sonia Sotomayor': [500, 190, 212, 55],
                   'Clarence Thomas': [200, 400, 600]}


"""
class section
"""


class Donor:
    '''
    class for the management of a single donor (d)
    '''
    def __init__(self, name, donations = None):
        self.norm_name = self.normalize_name(name)
        self.name = name.strip()
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)


    @staticmethod
    def normalize_name(self):
        '''
        clean up the name
        :return: name
        '''
        return self.name.lower().strip().replace(" ", "")


    def add_donation(self, donation_amount):
        '''
        add the donation to the db
        :param donation:
        :return: updated db
        '''
        self.donations.append(donation_amount)


    @property
    def last_donation(self):
        '''
        returns the donors last donation
        :return: last donation
        '''
        return self.donations[-1]


    @property
    def sum_donations(self):
        '''
        sum the donations in dollars
        :return: donation amount ($)
        '''
        return sum(self.donations)


    @property
    def num_donations(self):
        '''
        count up the number of donations
        :return:
        '''
        return len(self.donations)


    @property
    def avg_donations(self):
        '''
        average donation amount
        :return: average donation ($)
        '''
        return (self.sum_donations/self.num_donations)


class donor_collection():
    '''
    class for the management of the collection of all donors (dc)
    '''
    def __init__(self, donors = None):
        if donors is None:
            self.donor_datastore = {}
        else:
            self.donor_datastore = {d.norm_name: d for d in donors}


    @property
    def donors(self):
        '''
        retrieve the list of donors
        :return: list of donors
        '''
        return self.donor_datastore.values()


    def add_donor(self, name):
        '''
        create a new donor
        :returns: donor name
        '''
        donor = Donor(name)
        self.donor_datastore[donor.norm_name] = donor
        return donor


    def list_donors(self):
        pass


    def find_donor(self, name):
        '''
        lookup the donor
        :param name:
        :return: donor
        '''
        return self.donor_datastore.get(Donor.normalize_name(name))


    def donor_thankyou_letter(self, donor):
        '''
        creates the donor thank you letter
        :param donor: donor
        :return: message for donor
        '''
        return print('Dear {0:s}:\n, '
                     'On behalf of our organization, thank you for your donation of ${1:.2f}. \n,'
                     'It will surely be used well. \n,'
                     'Yours cordially, \n,'
                     'Board of Directors'.format(donor.name, donor.last_donation))


    @classmethod
    def load_from_file(cls):
        pass


    def save_to_file(self, filename):
        '''
        writes thank you letter to file
        :param filename:
        :return:
        '''
        with open(filename, 'w') as outfile:
                outfile.write(self.donor_thankyou_letter())


    @staticmethod
    def sort_donor(item):
        '''

        :param item:
        :return:
        '''
        return item[1]


    def create_report(self):
        pass


    def save_letters(self):
        pass


"""
menu section
"""


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
        #send_thankyou()
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


"""
testing section
"""


def test_create_donor():
    donor = Donor('Tom Tinker')

    assert donor.name == 'Tom Tinker'


def test_add_donation():
    donor = Donor('Tom Tinker')
    donor.add_donation(500)

    assert donor.num_donations == 1


def test_lookup_donor():
    donor = Donor('Tom Tinker')
    assert donor.lookup_donor(donor) == 1

def test_donor_thank_you_letter():
    pass


def test_donation_collection():
    dc = Donor_collection()


def test_add_donor():
    dc = Donor_collection()
    dc.add_donor(Donor('Bob'))


def test_find_donor():
    dc.find_donor()


def test_list_donors():
    pass


def test_thank_donors():
    pass


def test_create_report():
    pass

