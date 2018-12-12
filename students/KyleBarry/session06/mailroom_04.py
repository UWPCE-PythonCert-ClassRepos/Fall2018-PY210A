#!/usr/local/bin/python3
from datetime import datetime
import csv


class DonorManager:
    """Collects all donorsand adds functionality for things related to all
    donors"""

    # Dict to hold donor names as keys and donor instances as values
    donors = {}

    def __init__(self):
        pass

    def make_report(self):
        now = datetime.now().strftime("%Y-%m-%d")

        # Create csv file for report data
        with open(f"report_{now}.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Donor Name", "No. Donations", "Avg Donation",
                             "Total Donations"])

            # Zip lists of values to pass to writerow
            names = [i for i in self.donors]
            no_dons = [i.num_donations for i in self.donors.values()]
            avg_don = [i.average_donation for i in self.donors.values()]
            total_dons = [i.total_donations for i in self.donors.values()]
            zipped = zip(names, no_dons, avg_don, total_dons)

            for i in zipped:
                writer.writerow(i)

        return f"report_{now}.csv"

    def display_donor(self, name):
        return f"""Name: {self.donors[name].name}\nNo. Donations:{self.donors[name].num_donations}\nTotal Donations: {self.donors[name].total_donations}\nAverage Donation: {self.donors[name].average_donation}"""


class Donor:
    """Creates instance for individual donors and adds functionality for things
    related to individual donors"""

    def __init__(self, name):
        """Set donor name, give it empty list for future donations.
        Pass donor instance with name as key to DonorManager dict"""
        self.name = name
        self.donations = []
        DonorManager.donors[name] = self

    def add_donation(self, donation):
        self.donations.append(donation)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def average_donation(self):
        if len(self.donations):
            return round(sum(self.donations)/len(self.donations), 2)
        else:
            return 0

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def get_last_donation(self):
        return self.donations[-1]

    def make_thank_you_file(self):
        """Store thank you file"""
        now = datetime.now().strftime("%Y-%m-%d")
        file_ = f"{self.name}_{now}.txt"

        with open(file_, 'w') as f:
            f.write(f"Dear {self.name},\n\n")
            f.write(f"""\tThank you for your generous donations of
                    {Donor.total_donations}!\n\n""")
            f.write("\t\t\t\t\tSincerely, Donor Team")

        return file_

    def change_name(self, new_name):
        DonorManager.donors[new_name] = DonorManager.donors.pop(self.name)
        self.name = str(new_name)
