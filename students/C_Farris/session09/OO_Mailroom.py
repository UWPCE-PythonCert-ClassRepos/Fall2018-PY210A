#!/usr/bin/env Python3


##########
#Created by: Carol Farris
#Purpose: Create a OO version of Mailroom 
#Progress:
#Need to add Thank yous to all donors.
#
############




import sys
import os
from textwrap import dedent
OUT_PATH = "thank_you_letters"


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

    def thank_donor(self):
        pass

    def addDonor(self, donor_name, donor): #returns an f-string. Not ideal
        """"adds donor to collection
            cleans donor name to have it with capital letters an all else lower case."""
        donor_name = donor_name.strip().lower().title()
        self.donor_dict[donor_name] = donor


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


    def create_report(self):
        """returns data for report"""
        donorReport = [[round(float(sum(value.donations)), 2), key, len(value.donations),
                    round(float(sum(value.donations) / len(value.donations)), 2)]
                    for key, value in self.donor_dict.items()]
        sortedReport = sorted(donorReport)
        ascendingReport = sortedReport[::-1]
        return ascendingReport

    def prepare_to_write_to_disk(self, out_path=OUT_PATH):
        
        """Check OUT_PATH specified is a directory, if not, it will make it
        This is to run once at the start of the application.
        :Param: none
        :Return: none. Creates specified folder in CWD if not already created.
        """
        if not os.path.isdir(out_path):
            os.mkdir(out_path)

    def send_file_to_disk(self, key, donorLetter):
        """
        Accepts "Thank You" donor Letter and writes to disk.
        :param (person): Name of person, will be used in file name
        :param (donorLetter): Thank you letter to donor
        :return: none. Will send file to directory set in outpath.
        """
        filename = key.replace(' ', '_') + '.txt'
        filename = os.path.join(OUT_PATH, filename)
        open(filename, 'w').write(donorLetter)
        


    def save_all_thank_yous(self, out_path = OUT_PATH):
        """returns thank you's for all donors in donor collection"""
        for key, value in self.donor_dict.items():
            print(value.thank_your_letter())
            self.prepare_to_write_to_disk(out_path)
            self.send_file_to_disk(key, value.thank_your_letter())



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
  