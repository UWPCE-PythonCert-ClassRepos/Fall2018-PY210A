#!usr/bin/#!/usr/bin/env python
"""mailroom_oo module contains data objects donor and donor_collection to handle
all required operations for the mailroom script. User inputs are handled
elsewhere."""

# └── mailroom_oo
#    ├── __init__.py - empty for init
#    ├── cli_main.py - user interface file
#    ├── donor_models.py - data file
#    └── test_mailroom_oo.py - test file

import os
import yaml


class Donor:
    """Donor class handles all data, opperations, and attributes needed for
    donors."""
    def __init__(self, name):
        self.name = name
        self.donations = []

    def add_donation(self, donation):
        """Adds donation from donor to donor DB
        parma1: donation (number)"""
        self.donations.append(donation)

    @property
    def num_donations(self):
        """Returns number of donations."""
        return len(self.donations)

    @property
    def last_donation(self):
        """Returns last donation or None if no donations."""
        if self.num_donations:
            return self.donations[-1]
        else: return None

    @property
    def avg_donation(self):
        """Returns average donor donation or None if no donations."""
        if self.num_donations:
            return self.sum_donations/self.num_donations
        else: return None

    @property
    def sum_donations(self):
        """Returns total amount donated."""
        return sum(self.donations)

    def write_letter(self):
        """Writes thank you letter for donor's last donation. Returns string."""
        text = """Dearest {donor},\n
        We greatly thank you for your recent contribution of ${recent:.2f}.\n
        It will go straight to the person who needs it the most, our CEO.\n
        Please give more next time.\n
        \tLove,\n
        \t\tThe Team""".format(donor=self.name, recent=self.last_donation)
        return text


##Class manages collection of donations

#report - sort key needed
#thank you letters - return list of strings
#check donor if needed elsewhere
#list donors


#user interface code for input and prints

#init with collection
#add users from YAML
class donor_collection:
    def __init__(self):
        self.name = "donor_db_object"
        self.db = yaml.load(open("donor_db.yaml"))

    def add_donor(self, name):
        """Addes donor to database."""
        self.db.append(Donor(name))


    def list_donors(self):
        """Returns list of all donors in database."""
        donors = ""
        for donor in self.db():
            donors.join(donor.name + "\n")
