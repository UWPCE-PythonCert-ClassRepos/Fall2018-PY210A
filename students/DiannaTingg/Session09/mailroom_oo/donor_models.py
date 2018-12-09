# Lesson 09 Assignment: Mailroom - Object Oriented
# Donor and DonorCollection Classes


class Donor:
    """
    This class holds all the info about a single donor
    """
    def __init__(self, name, initial_donation):
        self.name = name
        self.donations = [initial_donation]

    def add_donation(self, new_donation):
        self.donations.append(new_donation)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def avg_donation(self):
        return self.total_donations/self.num_donations


# This class holds all of the donor objects as well as methods to add a new donor, search for a donor, etc
# Has a method to save/reload data
# Generates reports about all donors
class DonorCollection:
    """
    This class holds all of the donor objects
    """
    def __init__(self):
        self.donors_dict = {}

    def add_donation(self, donor_name, donation):
        if donor_name in self.donors_dict:
            self.donors_dict[donor_name].add_donation(donation)
            return
        else:
            new_donor = Donor(donor_name, donation)
            self.donors_dict[donor_name] = new_donor

    def list_donors(self):
        donor_list = [donor.name for donor in self.donors_dict.values()]
        sorted_donors = sorted(donor_list)
        return sorted_donors

    # Create sort key to return total donated
    @staticmethod
    def sort_key(donor_stats):
        return donor_stats[1]

    # Create a report of all donors
    def create_report(self):
        summary = [[donor.name, donor.total_donations, donor.num_donations, donor.avg_donation]
                   for donor in self.donors_dict.values()]

        # Sort Summary by total given in descending order
        sorted_summary = sorted(summary, key=self.sort_key, reverse=True)

        return sorted_summary
