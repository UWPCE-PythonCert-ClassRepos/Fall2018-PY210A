#!/usr/bin/env python3
from textwrap import dedent
import os


def sample_disney_donors():
#     donor_name = ["Yosemite Sam", "Yogi Bear", "Daffey Duck",
#                   "Wile E. Coyote", "Bugs Bunny", "Mickey Mouse"]
#     donation = [[100.56, 200.23, 300], [2000.33, 4000, 1000],
#                 [5000.24, 10000.34, 30000, 300], [300.40, 1000, 750.17],
#                 [100000.87, 50000, 100], [1345.67, 345.78, 1.23]]
#     return dict(zip(donor_name, donation))

    return [Donor("Yosemite Sam", [100.56, 200.23, 300]),
            Donor("Yogi Bear", [2000.33, 4000, 1000]),
            Donor("Daffey Duck", [5000.24, 10000.34, 30000, 300]),
            Donor("Wile E. Coyote", [300.40, 1000, 750.17]),
            Donor("Bugs Bunny", [100000.87, 50000, 100]),
            Donor("Mickey Mouse", [1345.67, 345.78, 1.23]),
            ]


class Donor:

    def __init__(self, name, donations=None):
        self.name = name
        self.donations = []

    def add_donation(self, donation):
        self.donations.append(donation)

    @property
    def num_donations(self):
        return len(self.donations)

    def last_donation(self):
        try:
            return self.donations[-1]
        except IndexError:
            return None

    @property
    def sum_donation_total(self):
        return sum(self.donations)

    @property
    def total_donations_made(self):
        return len(self.donations)

    def send_letter(self):
        return dedent('''Dear {0:s},

              Thank you for your very kind donation of ${1:.2f}.
              It will be put to very good use.

                             Sincerely,
                                -The Team\n
              '''.format(self.name, self.donations[-1]))

    def avg_donation(self):
        return self.sum_donation_total / self.num_donations


class DonorCollection():

    # Can I put this here as a class object? Used to right letter to disk
    OUT_PATH = "thank_you_letters"

    def __init__(self, donors=None):
        self.donors = {}


        ### AssertionError keeps getting raised on my for donor not being in don_list....thought???####
    # def donor_list(self):
    #     # Used same for loop as my Mailroom4
    #     list_don = ["List of Disney Donors:\n"]
    #     for donor in self.donors:
    #         list_don.append(donor.name)
    #     return "\n".join(list_don)

    def add_donor(self, name):
        # if name not in self.donors:
        #     self.donors.append(name)
        # return self.donors
        donor = Donor(name)
        self.donors[name] = donor
        return donor

    def find_donor(self):
        return self.donor in sample_disney_donors

    @staticmethod
    def sort_key(item):
        return item[1]

    def generate_report(self):
        report_rows = []
        for (name, gifts) in self.donors.items():
            total_gifts = sum(gifts)
            num_gifts = len(gifts)
            avg_gift = total_gifts / num_gifts
            report_rows.append((name, total_gifts, num_gifts, avg_gift))

        report_rows.sort(key=self.sort_key)
        print("{:25s} | {:11s} | {:9s} | {:12s}".format(
            "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
        print("-" * 66)
        for row in report_rows:
            print("{:25s}   ${:11.2f}   {:9d}   ${:12.2f}".format(*row))

    # Uses class object from DataCollection
    def prepare_to_run(self):
        if not os.path.isdir(self.OUT_PATH):
            os.mkdir(self.OUT_PATH)


    # Do I need to call super() because self.send_letter is from the superclass??
    # For this example send_letter is method from superclass
    # If so then do I need to call it on every instance for DataCollection class 
    def send_letters_to_disk(self):
        """
        make a letter for each donor, and save it to disk.
        """
        for donor, donations in self.donors.items():
            letter = self.send_letter(donor, sum(self.donations))
            filename = donor.replace(" ", "_") + ".txt"
            print("Your letter has been written to:", donor)
            filename = os.path.join(self.OUT_PATH, filename)
            open(filename, 'w').write(letter)







