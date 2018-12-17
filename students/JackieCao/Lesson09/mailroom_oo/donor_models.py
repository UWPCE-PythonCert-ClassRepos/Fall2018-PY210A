#!/usr/bin/env python

import sys
import math
from textwrap import dedent




class Donor():

    def __init__(self, name, donations=None):
        self.name = name.strip()
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)

    @property
    def last_donation(self):
        return self.donations[-1]

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def average_donation(self):
        return self.total_donations / len(self.donations)

    def add_donation(self, dollar):
        self.donations.append(dollar)

class DonorDB():
    def __init__(self, donors=None):
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {d.name: d for d in donors}

    @property
    def donors(self):
        return self.donor_data.values()

    def list_donors(self):
        a_list = ["Donor list:"]
        for donor in self.donors:
            a_list.append(donor.name)
        return "\n".join(a_list)

    def add_donor(self, name):
        donor = Donor(name)
        self.donor_data[donor.name] = donor
        return donor

    def gen_letter(self, donor):
        return f"Dear {donor.name}, Thank you for your very kind donation of ${donor.last_donation}.\nSincerely,\nThe Team"

    @staticmethod
    def sort_key(item):
        return item[1]

    def generate_donor_report(self):
        report_rows = []
        for donor in self.donor_data.values():
            name = donor.name
            gifts = donor.donations
            total_gifts = donor.total_donations
            num_gifts = len(gifts)
            avg_gift = donor.average_donation
            report_rows.append((name, total_gifts, num_gifts, avg_gift))

        report_rows.sort(key=self.sort_key)
        report = []
        report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                "Total Given",
                                                                "Num Gifts",
                                                                "Average Gift"))
        report.append("-" * 66)
        for row in report_rows:
            report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
        return "\n".join(report)

    def save_letters_to_disk(self):
        for donor in self.donor_data.values():
            print("Writing a letter to:", donor.name)
            letter = self.gen_letter(donor)
            filename = donor.name.replace(" ", "_") + ".txt"
            open(filename, 'w').write(letter)

def get_sample_data():
    return [Donor("W Peter", [100, 100]),
            Donor("J Bob", [100]),
            Donor("U Allen", [100, 200, 500, 500]),
            Donor("C Zack", [1000, 1000]),
            ]

 


