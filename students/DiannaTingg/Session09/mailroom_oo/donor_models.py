# Lesson 09 Assignment: Mailroom - Object Oriented
# Donor and DonorCollection Classes

import datetime

logo = r"""
   _   _   _   _     _   _   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( M | a | r | s ) ( F | o | u | n | d | a | t | i | o | n )
  \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
"""


class Donor:
    """
    This class holds all the info about a single donor.
    """

    def __init__(self, name):
        self.name = name
        self.donations = []

    def add_donation(self, new_donation):
        self.donations.append(new_donation)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def avg_donation(self):
        try:
            return self.total_donations / self.num_donations
        except ZeroDivisionError:
            return 0

    def thank_you_letter(self):

        date = datetime.datetime.now().strftime("%B %d, %Y")
        letter = f"{logo}\n\n{date}\n\n"\
            f"Dear {self.name}:\n\n"\
            f"Thank you so much for the generous donation of ${self.donations[-1]:,.2f}.\n"\
            f"We will use the money to help Earthlings move to Mars!\n\n"\
            f"Best regards,\nDianna Tingg\nMars Foundation"
        return letter


class DonorCollection:
    """
    This class holds all of the donor objects and methods to create a donor, find a donor, or list donors.
    It can also run a report on all donors and it saves/reloads data.
    """

    def __init__(self):
        self.donors_dict = {}

    def create_donor(self, donor_name):
        new_donor = Donor(donor_name)
        self.donors_dict[donor_name] = new_donor
        return new_donor

    def find_donor(self, donor_name):
        try:
            return self.donors_dict[donor_name]
        except KeyError:
            return self.create_donor(donor_name)

    def list_donors(self):
        donor_list = [donor.name for donor in self.donors_dict.values()]
        sorted_donors = sorted(donor_list)
        return sorted_donors

    @staticmethod
    # Returns total donations
    def sort_key(donor_stats):
        return donor_stats[1]

    def create_report(self):
        """
        Creates a list of donation statistics for all donors in the database.
        :return: Returns a sorted donor list based on total donations in descending order.
        """
        summary = [[donor.name, donor.total_donations, donor.num_donations, donor.avg_donation]
                   for donor in self.donors_dict.values()]

        sorted_summary = sorted(summary, key=self.sort_key, reverse=True)

        return sorted_summary
