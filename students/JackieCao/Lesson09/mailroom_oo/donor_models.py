#!/usr/bin/env python3
"""
Donor and DonorCollection classes
"""
class Donor:
    def __init__(self, name):
        self.name = name
        self.donations = []
        self.new_donation = 0

    def add_donation(self, donation):
        self.new_donation = donation
        self.donations.append(donation)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def thank_you_data(self):
        return {'d_name': self.name, 'd_dollar': self.new_donation}

class DonorCollection:
    def __init__(self):
        self.donors = {}

    def add_old_donors(self, dict_donors):
        self.donors.update(dict_donors)

    def add_donor(self, name, donation):

        if name in self.donors:
            for i in donation:
                self.donors[name].append(i)
        else:
            self.donors[name] = donation

    @property
    def list_donors(self):
        return list(self.donors.keys())

    @property
    def total_donated(self):
        return [sum(self.donors[k]) for k in self.donors]

    @property
    def num_of_donations(self):
        return [len(self.donors[k]) for k in self.donors]

    @property
    def average_donation(self):
        return [t/d for t, d in zip(self.total_donated, self.num_of_donations)]

    @property
    def report_data(self):
        return [(name, dollar, num, ave) for name, dollar, num, ave in
                zip(self.list_donors,
                    self.total_donated,
                    self.num_of_donations,
                    self.average_donation)]

    def send_thank_to_all(self):
        for name in self.donors:
            total = sum(self.donors[name])
            d = {'d_name': name, 'd_dollar': total}
            letter = "Dear {d_name},\n\n    Thank you for your donation of ${d_dollar}.\n\nBest,\nDonation Group".format(**d)
            with open(name + '.txt', 'w') as f:
                f.write(letter)

