import statistics


class Donor():
    def __init__(self, name, donation=""):
        self.name = name
        self.donation = list(donation)

    def add_donation(self, *values):
        for value in values:
            self.donation.append(value)

    def make_average(self, value):
        return statistics.mean(value)

    def make_total(self, value):
        return sum(value)

    def num_donations(self, value):
        return len(value)

    def make_thank_you(self, value):
        return f'Dear {self.name}, Thank you for your donation of ${self.make_total(value):.2f}. These funds help save the migratory butterflies of New South East.Thank you'

    def make_filename(self):
        return f'{self.name.replace(" ","_")}.txt'

    def make_report_string(self, value):
        return f'{self.name:<20} ${self.make_total(value):<15.2f} {self.num_donations(value):<15} ${self.make_average(value):<15.2f}'

    def __lt__(self, other):
        return (self.make_total(self.donation) > other.make_total(
            other.donation))

    def __gt__(self, other):
        return (self.make_total(self.donation) < other.make_total(
            other.donation))

    def __eq__(self, other):
        return (self.make_total(self.donation) == other.make_total(
            other.donation))

    def __str__(self):
        return self.name

    def sort_key(self):
        return (self.make_total(self.donation))


class Donors():
    def __init__(self, donor_list):
        self.donor_list = donor_list

    def append(self, cls):
        self.donor_list.append(cls)

    def list_donors(self):
        return [donor.name for donor in self.donor_list]

    def make_headers_string(self):
        headers = ("Donor Names", "Total Given", "Num Gifts", "Average Gifts")
        header_string = f'{headers[0]:<20} {headers[1]:<15} {headers[2]:<15} {headers[3]:<15}'
        return header_string

    def sort_donors(self):
        self.donor_list = sorted(self.donor_list)

    def make_report(self):
        report = self.make_headers_string() + "\n"
        self.sort_donors()
        for donor in self.donor_list:
            report += donor.make_report_string(donor.donation) + "\n"
        return report

    def make_thank_notes(self):
        self.thank_notes = []
        for donor in self.donor_list:
            self.thank_notes.append(donor.make_thank_you(donor.donation))
        return self.thank_notes
    def find_donor(self,value):
        donor_class=[]
        for donor in self.donor_list:
            if donor.name==value:
                donor_class=donor
        return donor_class        