#!/usr/bin/env python3

"""
Author: Jim Jenkins
Date: 12/10/2018
"""

import cli_main

if __name__ == '__main__':
	cli_main.py


import sys

#from donorLib import donor, donor_collection

"""
sample data
"""


donor_datastore = {'Samuel Alito': [1000, 1000, 1000],
                   'Ruth Bader-Ginsberg': [700, 100, 2000],
                   'Stephen Breyer': [200, 300, 10000],
                   'Neil Gorsuch': [100, 3000],
                   'Elena Kagen': [1800, 2300, 7000],
                   'Brett Kavanaugh': [400, 4500],
                   'John Roberts': [100, 200, 300],
                   'Sonia Sotomayor': [500, 190, 212, 55],
                   'Clarence Thomas': [200, 400, 600]}


class Donor:
	'''
    class for the management of a single donor (d)
    '''
	def __init__(self, name, donations = None):
		self.norm_name = self.normalize_name(name)
		self.name = name.strip()
		if donations is None:
			self.donations = []
		else:
			self.donations = list(donations)


	@staticmethod
	def normalize_name(self):
		'''
        clean up the name
        :return: name
        '''
		return self.name.lower().strip().replace(" ", "")


	def add_donation(self, donation_amount):
		'''
        add the donation to the db
        :param donation:
        :return: updated db
        '''
		self.donations.append(donation_amount)


	@property
	def last_donation(self):
		'''
        returns the donors last donation
        :return: last donation
        '''
		return self.donations[-1]


	@property
	def sum_donations(self):
		'''
        sum the donations in dollars
        :return: donation amount ($)
        '''
		return sum(self.donations)


	@property
	def num_donations(self):
		'''
        count up the number of donations
        :return:
        '''
		return len(self.donations)


	def avg_donations(self):
		return (self.sum_donations/self.num_donations)


	def __lt__(self, other):
		'''
        sorts the list of donors by name and donation
        :param other: donor
        :return: list of donors by name and donation
        '''
		return (self.name, self.donations < other.name, other.donations)



class Donor_collection():
	'''
    class for the management of the collection of all donors (dc)
    '''
	def __init__(self, donors = None):
		if donors is None:
			self.donor_datastore = {}
		else:
			self.donor_datastore = {d.norm_name: d for d in donors}


	@property
	def donors(self):
		'''
        retrieve the list of donors
        :return: list of donors
        '''
		return self.donor_datastore.values()


	def add_donor(self, name):
		'''
        create a new donor
        :returns: donor name
        '''
		donor = Donor(name)
		self.donor_datastore[donor.norm_name] = donor
		return donor


	def list_donors(self):
		pass


	def find_donor(self, name):
		'''
        lookup the donor
        :param name:
        :return: donor
        '''
		return self.donor_datastore.get(Donor.normalize_name(name))


	def donor_thankyou_letter(self, donor):
		'''
        creates the donor thank you letter
        :param donor: donor
        :return: message for donor
        '''
		return print('Dear {0:s}:\n, '
                     'On behalf of our organization, thank you for your donation of ${1:.2f}. \n,'
                     'It will surely be used well. \n,'
                     'Yours cordially, \n,'
                     'Board of Directors'.format(donor.name, donor.last_donation))


	@classmethod
	def load_from_file(cls):
		pass


	def save_to_file(self, filename):
		'''
        writes thank you letter to file
        :param filename:
        :return:
        '''
		with open(filename, 'w') as outfile:
			outfile.write(self.donor_thankyou_letter())

	def sort_key(self):
		return(self.name, self.donations)


	def create_report(self):
		pass


	def print_donor_report(self):
		print(self.create_report())


	def save_letters(self):
		pass



