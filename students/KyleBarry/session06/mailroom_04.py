#!/usr/local/bin/python3
from datetime import datetime
import csv

# Establish some data to work with in a dictionary
# donors = {"Timothy Tander": [100, 200, 300],
#          "Tara Towers": [200, 400, 600],
#          "Charlie Day": [700, 100, 2000],
#          "Sandra Connors": [1800, 2300, 7000],
#          "Betsy Hammond": [500, 190, 212, 55]}

#i donors = {}


class DonorManager:

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
        return self.donors[name]


class Donor(DonorManager):

    def __init__(self, name):
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
        if len(self.donations) != 0:
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
        self.name = str(new_name)



# def make_list():
#    """Print out list of donors"""
#    donor_list = []
#    for i in donors:
#        donor_list.append(i)
#        print(i)
#    return donor_list
#
#
#def add_donation(self.name, donation):
#    """Add to donation list for donors that already exist in database"""
#    donors[self.name].append(donation)
#    make_thank_you_file(self.name, donation)
#    return donors[self.name]
#
#
#def add_donation_new(self.name, donation):
#    """Add new donor with donation total to database"""
#    donors[self.name] = [donation]
#    make_thank_you_file(self.name, donation)
#    return donors[self.name]
#
#
#def make_donation_input():
#    """Get name of donor and donation amount and pass to appropriate func"""
#    self.name = input("Please enter your name: ")
#    donation = float(input('How much would you like to donate? '))
#    if self.name in donors:
#        add_donation(self.name, donation)
#    else:
#        add_donation_new(self.name, donation)
#
#
#def make_thank_you_file(self.name, donation):
#    """Print out thank you letter and store file"""
#    now = datetime.now().strftime("%Y-%m-%d")
#
#    with open(f"{self.name}_{now}.txt", 'w') as f:
#        f.write(f"Dear {self.name},\n\n")
#        f.write(f"\tThank you for your generous donation of {donation}!\n\n")
#        f.write("\t\t\t\t\tSincerely, Donor Team")
#
#    print("""\nThank you! A thank you letter has been generated and will be
#          emailed to you shortly!\n""")
#
#    return f"{self.name}_{now}.txt"
#
#
#def thank_you_input():
#    """Get thank you option from user and call appropriate function"""
#    while True:
#        response = input(thank_you_prompt)
#        if thank_you_dispatch[response]() == "exiting":
#            break
#        else:
#            print("Please enter a valid response")
#
#
#def make_report():
#    """Print donation report and store file"""
#    format_string = "{:<20}|{:>20}|{:>20}|{:>20}"
#    print("{:^20}|{:^20}|{:^20}|{:^20}".format("Donor Name",
#                                               "No. Donations",
#                                               "Avg. Donation",
#                                               "Total Donations"))
#
#    for k, v in donors.items():
#        print(format_string.format(k,
#                                   len(v),
#                                   "$" + str(round(sum(v)/len(v), 2)),
#                                   "$" + str(sum(v))))
#
#    # Create csv file for report data
#    now = datetime.now().strftime("%Y-%m-%d")
#    with open(f"report_{now}.csv", "w") as f:
#        writer = csv.writer(f)
#        writer.writerow(["Donor Name", "No. Donations", "Avg Donation",
#                         "Total Donations"])
#
#        # Zip lists of values to pass to writerow
#        names = [k for k in donors]
#        no_dons = [len(v) for v in donors.values()]
#        avg_don = [round(sum(v)/len(v), 2) for v in donors.values()]
#        total_dons = [sum(v) for v in donors.values()]
#        zipped = zip(names, no_dons, avg_don, total_dons)
#
#        for i in zipped:
#            writer.writerow(i)
#
#    return f"report_{now}.csv"
#
#
#def exiting():
#    """Return exiting, which breaks out of loops"""
#    return "exiting"
#
#
#def main(prompt, options_dict):
#    """Get input from user and call appropirate function"""
#    print("Welcome to the mailroom!")
#    while True:
#        answer = input(prompt)
#        if options_dict[answer]() == "exiting":
#            break
#        else:
#            print("Please make a valid selection")
#
#
#"""Establish dispatch dictionaries and prompts"""
#options_dict = {"1": thank_you_input, "2": make_report, "3": exiting}
#
#thank_you_dispatch = {"1": make_list, "2": make_donation_input, "3": exiting}
#
#thank_you_prompt = """Please select one of the following:
#          (1): Display list of donors
#          (2): Make a donation
#          (3): Back to main menu
#          """
#
#prompt = """Please enter one of the following:
#            (1): Send a thank you note
#            (2): Create a report
#            (3): Quit
#            """
#
#if __name__ == '__main__':
#    main(prompt, options_dict)
