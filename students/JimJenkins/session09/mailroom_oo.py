#!/usr/bin/env python3

class Donor:
    def __init__(self, name):
        self.name = name

        self.norm_name = self.normalize_name(name)
        self.name = name.strip()
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)

        self.donations = []



    def add_donation(self, donation):
        self.donations.append(donation)

    '''
    def test_add_donation():
        donor = Donor('name')

        donor.add_donation(500)

        assert donor.num_donations == 1
    '''

    @property
    def num_donations(self):
        return len(self.donations)


    def create_donor(self):
        pass


    '''
    def test_create_donor():
        donor = Donor('name')
    
        assert donor.name == 'name'
    '''


    def donor_thankyou_letter(self):
        pass


    '''    
    def test_donor_thank_you_letter():
        pass
    '''

class donor_collection():
    pass

    '''
    def test_donation_collection():
        dc = DonorCollection()
    
        dc.add_donor(Donor('Bob'))
        dc.find_donor()
    
        dc.list_donors()
    
        dc.thank_donors()
    
        dc.create_report()
    '''

import os


def main_menu_selection():
    action = input(dedent('''
      Choose an action:
      1 - Send a Thank You
      2 - Create a Report
      3 - Send letters to everyone
      4 - Quit
      > '''))
    return action.strip()


def quit():
    sys.exit(0)




#@lastdonation
#@sumdonations

