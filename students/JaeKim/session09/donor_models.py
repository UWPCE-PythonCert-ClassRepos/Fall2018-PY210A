import textwrap
import tempfile


def get_donordb():
    return [Donor("LeBron James", [500, 300, 200]),
            Donor("Dwyane Wade", [100, 200]),
            Donor("Carmelo Anthony", [1])
            ]


class Donor:
    def __init__(self, name, donation=None):
        self.name = name

        if donation is None:
            self.donation = []
        else:
            self.donation = donation

    def add_donation(self, donation):
        self.donation.append(donation)

    @property
    def num_donations(self):
        return len(self.donation)

    @property
    def last_donation(self):
        if len(self.donation) > 1:
            return self.donation[-1]
        else:
            return self.donation[0]

    @property
    def total_donation(self):
        return sum(self.donation)

    @property
    def average_donation(self):
        return sum(self.donation) / self.num_donations


class DonorCollection:
    def __init__(self, donors=None):
        if donors is None:
            self.donor_list = {}
        else:
            self.donor_list = {}

            for donor in donors:
                self.donor_list[donor.name] = donor

    @property
    def donors(self):
        return self.donor_list

    def add_donor(self, donor):
        if donor.name is not None:
            self.donor_list[donor.name] = donor
        else:
            return

    def list_donors(self):
        donor_list = []
        for donor in self.donor_list:
            donor_list.append(donor)
        return "\n".join(donor_list)

    def find_donor(self, name):
        if name in self.donor_list:
            return True
        else:
            return False

    def add_donor(self, name):
        self.donor_list[name.name] = name

    def add_donor_donation(self, name, amount):
        name.add_donation(amount)

    def thank_you(self, name):
        name = self.donor_list[name]
        return textwrap.dedent('''
                      Hi {},\n
                      Thank you for your donation of ${} to the research center.\n
                      Have a great day!
                      '''.format(name.name, name.total_donation)
                      )

    def make_report(self):
        report = ("Donor Name                | Total Given   | Num Gifts   | Average Gift\n"
                  "-------------------------------------------------------------------------")

        format = "%-20s  $ % 16f% 14i  $% 16f"

        for donor in self.donor_list.values():
            report += "\n" + format % (donor.name, donor.total_donation, donor.num_donations, donor.average_donation)

        return report

    def send_all_donors(self):
        email_full_output = ""
        for donor in self.donor_list.values():
            email_path = tempfile.gettempdir() + '\\' + donor.name + ".txt"

            email_body =("\nHi {},\n\n"
                  "Thank you for your donation of {} to the research center.\n\n"
                  "Have a great day!".format(donor.name, donor.total_donation))

            print(email_body)
            email_full_output += "\n" + email_body

            email_file = open(email_path, 'w')
            email_file.write(email_body)
            email_file.close()

            print('Email saved to ', email_path)

        return email_full_output