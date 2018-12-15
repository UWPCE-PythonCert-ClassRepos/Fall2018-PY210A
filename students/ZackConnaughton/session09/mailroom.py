"""
mailroom assignment
Command Line Interface for managing donors donations, reporting and sending
personalized thank you letters
"""

# import yaml

class Donor():
    """
    Name, donations list, method for average, number and total of avg_of_donations
    """
    save_path = './thank_you_letters/'

    def __init__(self, donor_info_dict):
        self.name = donor_info_dict['name']
        try:
            self.donation_list = donor_info_dict['donation_list']
        except KeyError:
            self.donation_list = []

    @property
    def donation_count(self):
        return len(self.donation_list)

    @property
    def donation_total(self):
        return round(float(sum(self.donation_list)), 2)

    @property
    def donation_average(self):
        """
        returns the average donation for the donor or 0 if the donor has not made
        any donation yet.
        """
        if self.donation_total > 0:
            return round(self.donation_total / self.donation_count, 2)
        else:
            return 0

    def add_donation(self, donation):
        try:
            if int(donation) > 0:
                self.donation_list.append(int(donation))
                print("\nDonation of ${:.2f} added to {}\n"
                      .format(self.latest_donation, self.name))
            else:
                raise ValueError("Donation value <= 0")
        except ValueError:
            print("\nInvalid entry for donation\nDONATION NOT ENTERED\n")

    @property
    def latest_donation(self):
        """
        returns the last donation the donor made, or None if there are no
        donations made by this donor
        """
        if self.donation_list:
            return self.donation_list[-1]

    def thank_you_letter(self):
        """
        returns a formatted letter for the donor
        """
        output = "Dear {},\n\n".format(self.name)
        if self.latest_donation:
            output += "{:<10}Thank you for your kind donation of ${:.2f}.\n\n".format(" ", self.latest_donation)
            output += "{:10}It will be put to very good use.\n\n".format(" ")
        else:
            output += "{:<10}Thank you for your interest in donating to our cause.\n\n".format(" ")
            output += "{:10}We would welcome your support.\n\n".format(" ")
        output += "{fill:<15}Sincerely,\n{fill:<18}-Everyone here at Company Spot".format(fill=" ")
        return output

    def save_thank_you_letter(self):
        f = open(self.save_path + self.name + '.txt', 'w')
        f.write(self.thank_you_letter())
        f.close()

    def donor_sort_key(self):
        return self.donation_total

    @classmethod
    def from_name(cls, name):
        return cls({'name': name, 'donation_list': []})


class Donor_Collection():

    def __init__(self, donor_list_dict):
        self.donors = []
        #print(donor_list_dict)
        for key, donor in donor_list_dict.items():
            #print(donor)
            self.donors.append(Donor(donor))

    def report(self):
        donor_report_list = []
        for d in sorted(self.donors, key=Donor.donor_sort_key, reverse=True):
            donor_report_list.append([d.name,d .donation_total,
                                      d.donation_count, d.donation_average])
        #print(donor_report_list)
        return donor_report_list

    def list_donors(self):
        output = [d.name for d in self.donors]
        return output

    def add_donor(self, name):
        self.donors.append(Donor.from_name(name))

    def find_donor(self, name):
        for d in self.donors:
            #print(d.name)
            if d.name == name:
                return d
        return False
