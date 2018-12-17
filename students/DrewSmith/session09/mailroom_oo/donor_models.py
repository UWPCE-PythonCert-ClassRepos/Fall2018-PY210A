#!/usr/bin python3
"""
Models for Donors
"""
import functools
import collections
from numbers import Number


@functools.total_ordering
class Donor():
    """ Represents a Donor and their donation values """

    def __init__(self, name, donations=None):
        self.name = name
        self._donations = []
        if donations is not None:
            self._donations.extend(donations)

    @property
    def num_donations(self):
        """ Number of donations """
        return len(self._donations)

    @property
    def donations(self):
        """ Tuple of donations """
        return tuple(self._donations)

    @property
    def name(self):
        """ Get Donor name """
        return self._name

    @name.setter
    def name(self, value):
        """ Set Donor name """
        self._name = value
        self._keyName = Donor.getDonorNameKey(value)

    @property
    def last_donation(self):
        """ Get last donation made """
        return None if len(self._donations) == 0 else self._donations[-1]

    @property
    def key(self):
        """ Standarized name key """
        return self._keyName

    @property
    def file_name(self):
        return f"{self.key}.txt"

    def add_donation(self, amount):
        """
        Add a donation to donor

        :param amount: amount of donation
        """
        if not isinstance(amount, Number) or amount < 0:
            raise TypeError("Donation must be a positive number")
        self._donations.append(amount)

    def donation_average(self):
        """ Compute donation average """
        return self.donation_sum() / self.num_donations

    def donation_sum(self):
        """ Compute total donation sum """
        return sum(self._donations)

    def get_thank_you_text(self):
        """ Thank you text """

        return f"""
Dear {self.name},
Thank you for your ${self.last_donation:.2f} donation to our charity.

Sincerely,
CEO Bob Newsenbaumerson"""

    def __eq__(self, other):
        """ Compare two Donor objects for equality """
        return isinstance(other, Donor) and self._keyName == other._keyName

    def __lt__(self, other):
        """ Compare two Donor objects for less than """
        return self._keyName < other._keyName

    def __hash__(self):
        """ Compute donor hash """
        return hash(self._keyName)

    def __iadd__(self, other):
        """ Add donations from another donor instance to this instance """
        for donation in other.donations:
            self.add_donation(donation)
        return self

    @staticmethod
    def getDonorNameKey(name):
        """
        Get the donor name key - Key used for case insensitive lookups

        :param name: donor name to compute key from
        """
        key = " ".join(name.split())  # condense multiple spaces into single space
        return key.strip().lower().replace(" ", "_").replace(".", "")

    @staticmethod
    def sort_key_total(self):
        """ Sort key method based on donation total then name """
        return (self.donation_sum(), self.name)


class DonorCollection():
    """ Represents a collection of Donors """

    def __init__(self):
        self._donors = dict()

    def add_donor(self, donor):
        """
        Adds new donor if if it does not exist.
        If it exists donations are added to existing donor.
        """
        if donor in self:
            self._donors[donor.key] += donor
        else:
            self._donors[donor.key] = donor

    def generate_report(self):
        """ Generates data for standard report (with headers)"""
        rows = [("Donor Name", "Total Given", "Num Gifts", "Average Gift")]
        rows.extend([
            (donor.name, donor.donation_sum(), donor.num_donations, donor.donation_average())
            for donor in sorted(self, key=Donor.sort_key_total, reverse=True)])
        return rows

    def list_donors(self):
        """ Returns a iterator of donor names """
        return (donor.name for donor in self)

    def generate_donor_files(self, dir_path, donor=None):
        """
        Generates Thank you files for donors

        :param dir_path: pathlib directory to save files
        :param donor: single donor to write file for, otherwise all donors are saved
        """
        donors = self if donor is None else (donor, )
        for donor in donors:
            with open(dir_path / donor.file_name, 'w') as f:
                f.write(donor.get_thank_you_text())

    def __iter__(self):
        """ Iterator for donors """
        return (val for val in self._donors.values())

    def __len__(self):
        """ Number of donors """
        return len(self._donors)

    def __contains__(self, other):
        """
        Determine if Donor or Name are in collection

        :param other: Donor instance or donor name to search
        """
        if isinstance(other, Donor):
            key = other.key
        else:
            key = Donor.getDonorNameKey(other)
        return key in self._donors

    def __getitem__(self, index):
        """
        Return Donor if it exists in collection, otherwise None

        :param index: Donor instance or donor name to search
        """
        if isinstance(index, Donor):
            key = index.key
        else:
            key = Donor.getDonorNameKey(index)
        return self._donors.get(key, None)
