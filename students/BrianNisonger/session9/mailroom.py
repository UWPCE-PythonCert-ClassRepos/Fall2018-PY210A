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

    def make_thank_you(self):
        return f'Dear {self.name}, Thank you for your donation of ${self.make_total(self.donation):.2f}. These funds help save the migratory butterflies of New South East.Thank you'

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
            self.thank_notes.append(donor.make_thank_you())
        return self.thank_notes

    def find_donor(self, value):
        donor_class = []
        for donor in self.donor_list:
            if donor.name.lower() == value.lower():
                donor_class = donor
        return donor_class

    def make_filenames(self):
        filenames = []
        for donor in self.donor_list:
            filenames.append(donor.make_filename())
        return filenames


def send_file(msg, filename):
    with open(filename, "w") as outfile:
        outfile.write(msg)


def add_donation(d_list, full_name):
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
    while True:
        full_name = input("Please enter a Full Name==>")
        if full_name.lower() == "list":
            for name in d_list.list_donors():
                print(name)
        else:
            add_donation(d_list, full_name)
            break


def report(d_list):
    print(d_list.make_report())


def send_donors(d_list):
    for donor in d_list.donor_list:
        send_file(donor.make_thank_you(),donor.make_filename())


def unknown(d_list):
    print("Please enter a valid response")
    return None


def main():
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
