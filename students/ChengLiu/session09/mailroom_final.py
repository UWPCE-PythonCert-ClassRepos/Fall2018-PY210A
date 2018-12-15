#!/usr/bin/env python3

"""
Cheng Liu
Mail-room Final
"""

# import sys
import math


# def default_donor():
#     """Testing data"""
#     return [Donor("Default Test1", [1, 2, 3]),
#             Donor("Default Test2", [10, 20, 30]),  # tuples to list
#             ]


class Donor():
    """class for donors"""

    def __init__(self, name, donations=None):
        self.name = name.strip().title()
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)  # converting donations from tuple to list

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


class Donor_Library():
    def __init__(self, donors=None):
        if donors is None:
            self.donor_lib = {}
        else:
            self.donor_lib = {d.name: d.donations for d in donors}

    @property
    def find_donors(self, name):
        if self.key() == name:
            return {self.key(), self.values()}

    # def find_donor(self, name):
    #     if self.name == name:
    #         return Donor[name]
    #     return self.get(name())





    # def add_donation(self, donation):
    #     """ add new donations"""
    #     if donation <= 0.0:
    #         raise ValueError("Donation amount must be greater than zero!")
    #     self.donations.append(donation)

    # def list_donors(self):
    #     current_donors = []
    #     for donor in self.donors:
    #         current_donors.append(donor.name)
    #     return "\n".join(current_donors)

    # def find_donor(self, name):
    #     return self.donors.get(Donor(name))

    # def add_donor(self, name):
    #     new_donor = Donor(name)
    #     self.donors[name] = new_donor

    # def letter(self, donor):
    #     return ("\nHello {}! Thank you for your donation of ${:.2}.".format(donor.name, str(donor.last_donation)) + "\n")

    # def report(self):
    #     report_rows = []
    #     for donor in self.donors:
    #         report_rows.append((donor.name, donor.total_donations, donor.num_of_donations, donor.avg_donations))

    #     report = []
    #     report.append("{:<25s} | {:>11s} | {:>9s} | {:>12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    #     report.append("-" * 70)
    #     for row in report_rows:
    #         report.append("{:<25s} | {:>11s} | {:>9s} | {:>12s}".format(*row))
    #     return "\n".join(report)

    # def send_letter_to_file(self):
    #     for donor in self.donors.values():
    #         print("Saving letter to:", donor.name)
    #         saved_letters = self.letter(donor)
    #         filename = "Letter_to_".join(donor.name) + ".txt"
    #         open(filename, 'w').write(saved_letters)
