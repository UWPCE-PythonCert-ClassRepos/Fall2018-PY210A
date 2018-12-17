# The module can contain the donor and donor collection
from textwrap import dedent


class Donor:
    # -----------------------------------------------------------------
    # This holds all the objects for a single donor
    # -----------------------------------------------------------------

    def __init__(self, name, donations=None):

        self._name = name
        self._donations = []
        if donations:
            if type(donations) is int and float:
                self._donations = [donations]
            else:
                self._donations = list(donations)

    @property
    def name(self):
        return self._name

    @property
    def donations(self):
        return self._donations

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def average_donations(self):
        return self.total_donations / len(self.donations)

    def add_donation(self, amount):
        self._donations.append(amount)

    @property
    def recent_donation(self):
        return self.donations[-1]

    @property
    def gen_letter(self):
        return dedent('''Dear {name},
        
        Thank you for your very kind donation of ${donation}. 
        It will be put to very good use.
                                
        Sincerely, 
        The Team'''.format(name = self.name, donation= self.recent_donation)
                      )


class DB:

    def __init__(self, donors=None):

        if donors == None:
            self._donors = {}
        else:
            self._donors = donors

    @property
    def donors(self):
        return self._donors

    def update_donor(self, name, amount):
        '''
        gets donor's name and recent donation to update the donors database
        :param name: fullname of an existing donor
        :param amount: amount of the recent donation
        :returns: updated donors database
        '''
        donor = Donor(name, self.donors[name])
        donor.add_donation(amount)
        return self.donors.update({donor.name: donor.donations})

    def find_donor(self, name):
        '''
        finds if a donor is in the donors_names
        :param name: fullname of donor to find
        :returns: the donor if found, or None if not
        '''

        if name in self.donors:
            return name
        else:
            return None

    def add_donor(self, name, amount):
        '''
         If a donor doesn't exist in the donors, it add a
         new donor and his/her donation.

        :param name: fullname of a new donor
        :param amount: amount of the donation
        :returns: a new donor
        '''
        if self.find_donor(name) == None:
            self.donors[name] = amount

    @property
    def list_donors(self):
        '''
        Lists donors
        :returns: a string with donors
        '''
        list = [d for d in self.donors]
        return '\n'.join(list)

    @property
    def report(self):
        '''
        creates a report
        :returns: a string
        '''
        report_rows = []
        for name in self.donors:
            donor = Donor(name, self.donors[name])
            name = donor.name
            num_donation = len(donor.donations)
            total_donations = donor.total_donations
            avg_donation = donor.average_donations
            report_rows.append((name, total_donations, num_donation, avg_donation))
            report = []
            report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                    "Total Given",
                                                                    "Num Gifts",
                                                                    "Average Gift"))
            report.append("-" * 66)
            for row in report_rows:
                report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
            return "\n".join(report)


    def save_data(self):
        '''Makes files for donors'''
        for donor in self.donors:
            print("Saving the letter for", donor)
            letter = Donor(donor).gen_letter
            # I don't like spaces in filenames...
            filename = donor.name.replace(" ", "_") + ".txt"
            open(filename, 'w').write(letter)
