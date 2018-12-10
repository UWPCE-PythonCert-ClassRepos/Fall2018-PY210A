#!/usr/bin/env Python3


##########
#Created by: Carol Farris
#Purpose: Create a OO version of Mailroom 
#Progress:
#
############

donor_db = {"William Gates III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "John Galt": [25.00, 9038.01, 0.01]
            }

donor_collection = {"name": donor_object,
    
}            

"""Everything you want to use wto manage the bacth of collections"""
class DonorCollection():

    def __init__(self, donor=None, donation=0, **kwargs):
        self.donors=

    def list_donors():
        pass

    def thank_donors():
        pass

    def report():
        pass

    def addDonor():
        """"adds donor to collection"""

    def find_donor():
        """Checks collection to see if current donor is in list. If not, ask to add"""
        pass


"""Everything one needs to know about a single donor"""
"""you don't want donor to know how it is being stored"""
"""Your searching and adding would be in donorCollection"""
"""Your individual donor file would be in donor"""
class Donor ():

    def __init__(self, name=None, donation=0):
        self.name = name
        self.donation = donation
        self.donations = []

    def _add_donation(self, donation):
        """adds a new donation to donors list"""
        self.donations.append(donation)

    @property
    def num_donations(self):
        """counts the number of donations present for a single donor"""
        return len(self.donations)

    @property
    def sum_donations(self):
        """returns the sum of all the donors donations"""
        pass

    def donor_thank_your_letter():
        """Send a single donor to file"""
        pass

    def _donor():
        pass    
