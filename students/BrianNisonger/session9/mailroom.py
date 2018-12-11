import statistics


class Donor():
    """ Class used to contain donor name,donation, and methods involved with a single donor """

    def __init__(self, name, donation=""):
        """ Takes a name, and optionally a donation list"""
        self.name = name
        self.donation = list(donation)

    def add_donation(self, *values):
        """Takes either a single donation, and appends it to the list, or appends a set of donations"""
        for value in values:
            self.donation.append(value)

    def make_average(self, value):
        """Averages the donations"""
        return statistics.mean(value)

    def make_total(self, value):
        """Totals the donations"""
        return sum(value)

    def num_donations(self, value):
        """Counts the donations"""
        return len(value)

    def make_thank_you(self):
        """ Returns a thank you note for total donations of donor"""
        return f'Dear {self.name}, Thank you for your donation of ${self.make_total(self.donation):.2f}. These funds help save the migratory butterflies of New South East.Thank you'

    def make_filename(self):
        """Turns a donor name into a filename"""
        return f'{self.name.replace(" ","_")}.txt'

    def make_report_string(self, value):
        """Makes a single line of the report(Name,Total Donations,Num of Donatioms, Average Donations)"""
        return f'{self.name:<20} ${self.make_total(value):<15.2f} {self.num_donations(value):<15} ${self.make_average(value):<15.2f}'

    def __lt__(self, other):
        """less than"""
        return (self.make_total(self.donation) > other.make_total(
            other.donation))

    def __gt__(self, other):
        """greater than"""
        return (self.make_total(self.donation) < other.make_total(
            other.donation))

    def __eq__(self, other):
        """equal"""
        return (self.make_total(self.donation) == other.make_total(
            other.donation))

    def __str__(self):
        """Returns name of the donor if str is called"""
        return self.name

    def sort_key(self):
        """What to sort on"""
        return (self.make_total(self.donation))


class Donors():
    """ This contains a list of classes, used to store multiple instances of the Donor class for grouping"""

    def __init__(self, donor_list):
        self.donor_list = donor_list

    def append(self, cls):
        """Adds another donor to the donor_list"""
        self.donor_list.append(cls)

    def list_donors(self):
        """returns a list containing the names of all the donors in the donor list"""
        return [donor.name for donor in self.donor_list]

    def make_headers_string(self):
        """Header for the report"""
        headers = ("Donor Names", "Total Given", "Num Gifts", "Average Gifts")
        header_string = f'{headers[0]:<20} {headers[1]:<15} {headers[2]:<15} {headers[3]:<15}'
        return header_string

    def sort_donors(self):
        """Takes a list of donors and sorts by total donations"""
        self.donor_list = sorted(self.donor_list)

    def make_report(self):
        """Combines the report header with individual report strings"""
        report = self.make_headers_string() + "\n"
        self.sort_donors()
        for donor in self.donor_list:
            report += donor.make_report_string(donor.donation) + "\n"
        return report

    def make_thank_notes(self):
        """Provides a list containing all the thank you notes for Donors, Not Implemented in final code"""
        self.thank_notes = []
        for donor in self.donor_list:
            self.thank_notes.append(donor.make_thank_you())
        return self.thank_notes

    def find_donor(self, value):
        """Takes a string value and returns a donor class if donor name matches string, or a empty list if not"""
        donor_class = []
        for donor in self.donor_list:
            if donor.name.lower() == value.lower():
                donor_class = donor
        return donor_class

    def make_filenames(self):
        """Makes a list of filenames for the donor list, Not implemented in final code"""
        filenames = []
        for donor in self.donor_list:
            filenames.append(donor.make_filename())
        return filenames


def send_file(msg, filename):
    """Take a string and a filename and write the msg out to the file specified"""
    with open(filename, "w") as outfile:
        outfile.write(msg)


def add_donation(d_list, full_name):
    """Takes the list of donor classes and a full name and adds a donation using user input"""
    donor = d_list.find_donor(full_name)
    if type(donor) == list:
        donor = Donor(full_name)
        d_list.append(donor)
    donation = input("Please enter a donation==>")
    while not donation.isdigit():
        donation = input("Please enter a donation==>")
    donation = float(donation)
    donor.add_donation(donation)
    send_file(donor.make_thank_you(), donor.make_filename())


def thank_you(d_list):
    """Gnerates a thank you for a new donation, using user input it either lists the donors, or otherwise adds a donation to the list"""
    while True:
        full_name = input("Please enter a Full Name==>")
        if full_name.lower() == "list":
            for name in d_list.list_donors():
                print(name)
        else:
            add_donation(d_list, full_name)
            break


def report(d_list):
    """Generates the report to the screen"""
    print(d_list.make_report())


def send_donors(d_list):
    """Writes out a thank you note for each donor in the donor list, amount in file is total donations given"""
    for donor in d_list.donor_list:
        send_file(donor.make_thank_you(), donor.make_filename())


def unknown(d_list):
    """Used for the menu to prevent invalid responses"""
    print("Please enter a valid response")
    return None


def main():
    """Defined the donors, added them to a list, and created a menu to all user input to manipulate"""
    d1 = Donor("Fred Flinstone", [100, 200, 300, 400])
    d2 = Donor("James Dean", [500, 600, 700, 800])
    d3 = Donor("Jack the Ripper", [1, 2, 3, 4])
    d4 = Donor("Mickey Mouse", [100, 200, 300, 5, 15, 7])
    d_list = Donors([d1, d2, d3, d4])
    menu = {
        "t": thank_you,
        "r": report,
        "s": send_donors,
    }
    while True:
        print("Please enter one of the following")
        try:
            answer = input("t to Thank a Single Donor\n"
                           "r to Send a Report\n"
                           "s to Send all Donors a Thank You Email\n"
                           "q to Quit:")
            answer = answer[0].lower()
            if answer == "q":
                break
            menu.get(answer, unknown)(d_list)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
