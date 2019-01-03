import math
import sys


def test_data():
    """ Data to be used as samples for coding and testing."""
    return [Donor("David Andrews", [200.50, 400.00, 250.75]),
            Donor("John Goodfellow", [25.00, 175.50]),
            Donor("Mary Suzuki", [75.00, 125.00, 250.00]),
            Donor("Bonney Lake", [500.50, 700.75, 500.25]),
            Donor("DeMarcus Rollins", [155.00, 165.00])
            ]


class Donor:
    def __init__(self, name, donations=None):
        """ Create Donor class for data and methods for individual donor."""
        self.name = name.strip()
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)

    @staticmethod
    def valid_donation(donation):
        """ Make sure entered amount of a donation is valid before adding to database."""
        donation = float(donation)
        if donation < 0:
            raise ValueError("Donation has to be more than 0.")
        if donation < 0.1:
            raise ValueError("Donation has to be more than 10 cents")
        return donation

    def add_donation(self, amount):
        amount = self.valid_donation(amount)
        self.donations.append(amount)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def tot_donations(self):
        return sum(self.donations)

    @property
    def avg_donation(self):
        """ Average donation is total donations divided by the number of donations."""
        return self.tot_donations / self.num_donations

    @property
    def last_donation(self):
        try:
            return self.donations[-1]
        except IndexError:
            return None


class DonorCollection:
    def __init__(self, donors=None):
        """ Initialize the DonorCollection class to hold donors info and methods for donors in database."""
        if donors is None:
            self.donor_info = {}
        else:
            for donor in donors:
                self.donor_info.update({donor.name: donor})

    @property
    def donors(self):
        return self.donor_info.values()

    @property
    def list_of_donors(self):
        donor_list = []
        for donor in self.donors:
            donor_list.append(donor.name)
        return "\n".join(donor_list)

    @classmethod
    def add_donor(self, name, donations):
        donor = self.donor_info[donor_name(name)]
        if donor not in donor_info:
            donor = self.add_donor(name)
        donor.add_donation(donation)
        return donor

    @classmethod
    def find_donor(self, name):
        if donor in self.donor_info:
            return self.donor
        else:
            print("Donor name not found. Would you like to join?")
            self.add_donor()

    @property
    def thank_all_donors(self, donors):
        return self.thank_all_donors(donors)

    def send_thank_you_letter(self, donor):
        print("Dear {}, \n"
            "Thank you for your generous gift of ${} to promote public education \n"
            "and to support research about bats. \n"
            "The Bat Society".format(self.name, self.last_donation))


    @staticmethod
    def sort_key(item):
        return item[1]


def make_donor_report(self):
    """
    Summary report. Show total donation, the number of donations, and the average amount per donation.
    Print out the results in a table.
    """
    report_rows = []
    for donor in self.donor_info.values():
        name = donor.name
        donations = donor.donations
        tot_don = donor.tot_donations
        num_don = len(donations)
        avg_don = donor.avg_donation
        report_rows.append(name, tot_don, num_don, avg_don)
    report_rows.sort(key=self.sort_key)
    report = []
    report.append("{:<25s}|{:>16s}|{:>16s}|{:>16s}".format("Donor Name","Total Donation",
                                                 "Num Donations","Average Amount"))
    for row in report_rows:
        report.append("{:<25s} {:>16.2f} {:>16d} {:>16.2f}".format(*row))
    return "\n".join(report)


def cli_main_menu():
    while True:
        try:
            print("Welcome to the Bat Society. Please select from 1 to 4 in the following: ")
            answer = int(input("1 Send a Thank You letter \n"
                               "2 Create a Report \n"
                               "3 Send letters to all donors \n"
                               "4 Quit \n"))
            if answer == 4:
                print("Thank you for visiting our website.")
                sys.exit()
            elif answer == 1:
                thank_you()
            elif answer == 2:
                make_donor_report()
            elif answer == 3:
                letters_to_all_donors()
                break
            else:
                print("Please try again choosing from 1 to 4.")
        except ValueError:
            print("Please enter a valid response.")


def thank_you():
    while True:
        name = input("What is your full name? \n"
                    "Type 'list' for a list of donors. \n"
                    "Or type 'menu' to exit. \n"
                    )
        name = name.strip().title()
        if name == "Menu":
            return
        elif name == "List":
            return list(donors_info)
            choose_name_from_list()
        else:
            print("Welcome back {}.".format(name))
            break
        """ When name not in donors database, add name to database."""
        if name is None:
            donor = test_data.add_donor(name)
    make_donation()
    return

def choose_name_from_list():
    try:
        name = input("Please type in a name from the list: \n")
    except ValueError:
        print("Please type in a valid name.")
    return


def make_donation():
    """ Prompt user to make a donation."""
    while True:
        don_resp = input("How much would you like to donate? \n"
                     "Or type 'menu' to exit. \n").strip()
        if don_resp in ("menu", "Menu"):
            return
        else:
            try:
                don_resp = float(don_resp)
                break
            except ValueError:
                print("Please enter a valid amount.")
    test_data.append(name[don_resp])
    send_thank_you_letter()
    return


def letters_to_all_donors():
    pass



if __name__ == '__main__':
    cli_main_menu()
    make_donor_report()
    thank_you()
    send_thank_you_letter()
    make_donation()
    choose_name_from_list()
    add_donor()
    letters_to_all_donors()






