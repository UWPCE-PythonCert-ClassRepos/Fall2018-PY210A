#!/usr/bin/env python3

"""
Cheng Liu
Mail-room Final
"""

# import sys
import math


def donors():
    """Testing data"""
    return [Donor("Test Name_1", [1, 2, 3]),
            Donor("Test Name_2", [10, 20, 30]),
            Donor("Test Name_3"),  # tuples to list
            ]


class Donor():
    """class for donors"""

    def __init__(self, name, donations=None):
        self.name = name.strip().title()
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)  # converting donations from tuple to list

    @property
    def donor(self):
        return (self.name, self.donations)

    @property
    def donor_name(self):
        return self.name

    @property
    def list_donations(self):
        try:
            return self.donations
        except IndexError:
            return None

    @property
    def last_donation(self):
        try:
            return self.donations[-1]
        except IndexError:
            return None

    @property
    def total_donations(self):
        try:
            return sum(self.donations)
        except IndexError:
            return 0

    @property
    def num_of_donations(self):
        try:
            return len(self.donations)
        except IndexError:
            return 0

    @property
    def avg_donations(self):
        try:
            return self.total_donations / self.num_of_donations
        except ZeroDivisionError:
            return None


class DonorDB():

    def __init__(self, donors=None):  # donors needs to be a list here
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {d.name: d.donations for d in donors}

    def find_donor(self, name):  # find donations based on donor name
        if name in self.donor_data.keys():
            return self.donor_data.get(name)
        else:
            return None

# need more works here
    # def add_donor(self, donors):
    #     donors_add = Donor(donors)
    #     return self.donor_data.update(donors_add)

    def list_donors(self):
        current_donors = []
        for data in self.donor_data:  # donor_data is a dictionary
            current_donors.append(data)
        return "\n".join(current_donors)


    def letter(self):
        name = self.donor_data.keys()
        donation = self.donor_data.values()
        return ("\nHello {}! Thank you for your donation of ${:.2}.".format(name, str(donation)) + "\n")


    def report(self):
        report_rows = []
        for donor in self.donors:
            report_rows.append((donor.name, donor.total_donations, donor.num_of_donations, donor.avg_donations))

        report = []
        report.append("{:<25s} | {:>11s} | {:>9s} | {:>12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
        report.append("-" * 70)
        for row in report_rows:
            report.append("{:<25s} | {:>11s} | {:>9s} | {:>12s}".format(*row))
        return "\n".join(report)

    def send_letter_to_file(self):
        for donor in self.donors.values():
            print("Saving letter to:", donor.name)
            saved_letters = self.letter(donor)
            filename = "Letter_to_".join(donor.name) + ".txt"
            open(filename, 'w').write(saved_letters)
