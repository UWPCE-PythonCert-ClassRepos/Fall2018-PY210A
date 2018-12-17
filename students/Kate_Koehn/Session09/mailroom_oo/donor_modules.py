#!/usr/bin/env python3

"""
mailroom assignment
"""

# Mailroom Part 5

# import relevant dictionaries
import os
import sys
import math
from textwrap import dedent


# Dictionary of previous donors names and their donation amounts
def get_sample_donors():
    donors = {"Rick Sanchez": [3.00, 1.00],
              "Liz Lemon": [4000.00, 3000.00, 6000.00],
              "Andy Dwyer": [10.00],
              "Brendan Small": [3.00, 10.00],
              "Coach McGuirk": [2.00, 1.00]}
    return donors


class Donor:
    """
    contains all the attributes, properties, and methods to provide access to donor-specific information
    """

    def __init__(self, name, donations=None):
        self.name = name
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)


    def add_donation(self, donation):
        donation = float(donation)
        if math.isnan(donation) or math.isinf(donation) or round(donation, 2) <= 0.00:
            raise ValueError
        self.donations.append(donation)


    @property
    def num_donations(self):
        return len(self.donations)


    @property
    def last_donation(self):
        try:
            return self.donations[-1]
        except IndexError:
            return None

    @property
    def sum_donations(self):
        return sum(self.donations)

    @property
    def avg_donations(self):


# create properties for sum, avg, number donations
#have class that manages the collections


##haven't been able to test this yet.
class DonorCollection():
    """
    This class holds all of the donor objects as well as methods to add a new donor, search for an existing donor, etc.
    """

    def get_donor_key(donor_name):
        """looks up key in donor dict"""
        donor_key = donor_name.strip()
        for key in donors.keys():
            if donor_key == key:
                return True
        return False


    def add_new_donor(donor_name):
        name = donor_name.strip()
        if name not in donors.keys():
            donors[name] = []
        return donor_name


    def add_donation_to_donor(donor_name, donation):
        donors[donor_name].append(donation)




