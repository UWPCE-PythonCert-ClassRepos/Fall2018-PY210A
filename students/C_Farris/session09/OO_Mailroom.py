#!/usr/bin/env Python3


##########
#Created by: Carol Farris
#Purpose: Create a OO version of Mailroom 
#Progress:
#
############

#May be unnecessary
#donor_db = {"William Gates III": [653772.32, 12.17],
#            "Jeff Bezos": [877.33],
#            "Paul Allen": [663.23, 43.87, 1.32],
#            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
#            "John Galt": [25.00, 9038.01, 0.01]
#            }

#May be unnecessary
#donor_collection = {"name": donor_object,
    
#}

"""Everything you want to use wto manage the bacth of collections"""
class DonorCollection():
    """Manages the donor collection in donor_dict and manipulates the collection"""

    def __init__(self, donor=None):
        
        if donor:
            self.donor_dict={}

            for items in donor:
                self.donor_dict[donor.name] = donor
        else:        
            self.donor_dict={}

    def list_donors(self):
        pass

    def thank_donors(self):
        pass

    def report(self):
        pass
        """Checks collection to see if current donor is in list. If not, ask to add"""

    def addDonor(self, donor_name, donor):
        """"adds donor to collection"""
        self.donor_dict[donor.name] = donor

    def return_donor(self, donor):
        return self.donor_dict[self.donor_name]
         


"""Everything one needs to know about a single donor"""
"""you don't want donor to know how it is being stored"""
"""Your searching and adding would be in donorCollection"""
"""Your individual donor file would be in donor"""
class Donor ():

    def __init__(self, name, donation=0):
        self.name = name
        self.donation = donation
        self.donations = []

    def add_donation(self, donation):
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

    @property
    def _donor(self):
        print(Donor)
        return Donor

    @property
    def _name(self):
        return self.name
  