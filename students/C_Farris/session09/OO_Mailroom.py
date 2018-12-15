#!/usr/bin/env Python3


##########
#Created by: Carol Farris
#Purpose: Create a OO version of Mailroom 
#Progress:
#Finished first pass of Donor class. Now need to fill out and test 
#Donor Coollection class
#Then, create CLI.py and see if I can runn the OO Mailroom
#
############

""""
import mailroom_oo

dir(Mailroom_oo)

__version__ = "1.0.0"

"""


import sys
import os
from textwrap import dedent

"""Everything you want to use wto manage the bacth of collections"""
class DonorCollection():
    """Manages the donor collection in donor_dict and manipulates the collection"""

    def __init__(self, donor=None):

        if donor:
            self.donor_dict={}

            for items in donor:
                self.donor_dict[items.name] = items
        else:
            self.donor_dict={}


    def list_donors(self):
        """return the donor names from donor_dict"""
        keyList = ""
        for key in self.donor_dict:
            keyList = keyList + key + '\n'
        return keyList

    def thank_donors(self):
        pass

    def report(self):
        pass
        """Checks collection to see if current donor is in list. If not, ask to add"""


    def addDonor(self, donor_name, donor): #returns an f-string. Not ideal
        """"adds donor to collection
            cleans donor name to have it with capital letters an all else lower case."""
        donor_name = donor_name.strip().lower().title()
        self.donor_dict[donor_name] = donor


    def retrieve_donor_object(self, donor):
        """uses a donor object to retrieve a donor"""
        try: 
            name = self.donor.name in donor_dict
            print("its in the dictionary!")
            return donor
        except KeyError:
            print("That donor is not in the dictionary.")
            return None


    def donor_in_dictionary(self, donor_name):
        """Returns boolean if donor_name supplied is in dictionary""" 
        donor_name = donor_name.strip().lower().title()
        if donor_name in self.donor_dict:
                return True
        else:
            return False

    def add_donor_donation(self,donor_name, newDonation):
        """adds new donation to donor in donor collection"""
        try:
            value = newDonation/2
        except TypeError:
            return "Donation value must be entirely numeric!"
        else:
            if value <=0.005:
                return "Donation cannot be smaller than a penny!"
            else:
                self.donor_dict[donor_name].add_donation(newDonation)

"""Everything one needs to know about a single donor"""
"""you don't want donor to know how it is being stored"""
"""Your searching and adding would be in donorCollection"""
"""Your individual donor file would be in donor"""
class Donor ():

    def __init__(self, name, donations=None): ##change donations to none, 
        self.name = name
        #self.donation = donation

        if donations is None:
            self.donations = []
        else:
            try:
                self.donations = list(donations)
            except TypeError:
                self.donations = [donations]  

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}) : {self.donations}'

    def add_donation(self, donation):
        """Adds a new donation to the donor list. 
        Validation requires amount to be a penny or greater and 
        a numeric value.""" 
        try:
            value = donation/2
        except TypeError:
            return "Donation value must be entirely numeric!"
        else:
            if value <=0.005:
                return "Donation cannot be smaller than a penny!"
            else:
                self.donations.append(donation)
   
    @property
    def num_donations(self):
        """counts the number of donations present for a single donor"""
        return len(self.donations)


    def sum_donations(self):
        """returns the sum of all the donors donations"""
        return sum(self.donations)

    def get_last_donation(self):
        """returns the last donation made by donor"""
        return (self.donations[-1])

    def thank_your_letter(self, donation_type=''):
        """Send a single donor thank you for their last donation (default) or sum of their donations (if specified)"""
        if donation_type == 'sum':
            donation_amount = self.sum_donations()
        else:
            donation_amount = self.get_last_donation()

        return dedent(
        '''\tDear {},
        Thank you for your generous donation of ${} to our cause.
        
        Sincerely,
        The Team'''.format(self.name, donation_amount))

    @property
    def _donor(self):
        print(Donor)
        return Donor

    @property
    def _name(self):
        return self.name


###############Mock Donor List#######
donor_mock2 = [Donor("William Gates III", [653772.32, 12.17]),
              Donor("Jeff Bezos", [877.33]),
              Donor("Paul Allen", [663.23, 43.87, 1.32]),
              Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
              Donor("John Galt", [25.00, 9038.01, 0.01])]
 ###############Mock Donor List#######       
  