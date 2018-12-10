"""
mailroom assignment
"""

import yaml

class Donor():
    """
    Name, donations list, method for average, number and total of avg_of_donations
    """
    save_path = './thank_you_letters/'

    def __init__(self, donor_info_dict):
        self.name = donor_info_dict['name']
        self.donation_list = donor_info_dict['donation_list']

    @property
    def donation_count(self):
        return len(self.donation_list)

    @property
    def donation_total(self):
        return round(float(sum(self.donation_list)), 2)

    @property
    def donation_average(self):
        return round(self.donation_total / self.donation_count, 2)

    def add_donation(self, donation):
        self.donation_list.append(donation)

    @property
    def latest_donation(self):
        return self.donation_list[-1]

    def thank_you_letter(self):
        """
        returns a formatted letter for the donor
        """
        output = "Dear {}\n\n".format(self.name)
        output += "{:<10}Thank you for your kind donation of ${:.2f}.\n\n".format(" ", self.latest_donation)
        output += "{:10}It will be put to very good use.\n\n".format(" ")
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
        print(donor_list_dict)
        for key, donor in donor_list_dict.items():
            print(donor)
            self.donors.append(Donor(donor))

    def report(self):
        donor_report_list = []
        for d in sorted(self.donors, key=Donor.donor_sort_key, reverse=True):
            donor_report_list.append([d.name,d .donation_total,
                                      d.donation_count, d.donation_average])
        print(donor_report_list)
        return donor_report_list

    def all_thank_you_letters():
        pass

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

def initial_donor_load(donor_file=None):
    if donor_file:
        file=open(donor_file, 'r')
        donor_list_dict = yaml.load(file.read())
        file.close()
        return donor_list_dict


def unknown():
    print("That is an invalid entry\n")
    return None


def quit_menu():
    return 'quit'

def new_donation_sub_menu():
    """
    prompts for a donor, and a donation, enters that donation for the donor.
    saves and prints a thank you letter
    """
    response = ""
    while response != 'Q':
        print("Enter the full name of donor:")
        print("(Type 'list' to see a full list of donors)")
        response = input(' => ').title()
        if response == "List":
            print('\n'.join(DC.list_donors()))
        else:
            if not DC.find_donor(response):
                print(response + ' is not currently in the database.')
                print('Please confirm you would like to add this donor?')
                response_add = input('(y/n)=> ').lower().strip()
                if response_add == 'y':
                    DC.add_donor(response)
                else:
                    print("Donation NOT added\n")
                    return
            try:
                print("Enter donation amount for " + response + ":")
                money = input(' => ')
                cur_donor = DC.find_donor(response)
                cur_donor.add_donation(int(money))
                print("\nDonation of ${:.2f} added to {}\n"
                      .format(cur_donor.latest_donation, cur_donor.name))
            except ValueError:
                print("\nInvalid entry for donation\nDONATION NOT ENTERED\n")
            finally:
                response = "Q"


def report():
    """
    generates a list of donor information from the donor Donor_Collection.
    determines the smallest width that can display and returns a string with
    the header and donor information properly formatted for printing
    """
    donor_report_list = DC.report()
    print(DC.report())
    widths = []
    for x in range(len(donor_report_list[0])):
        max_width = max(([len(str(item[x])) for item in donor_report_list]))
        widths.append(max_width + 4)
    print(widths)
    output_string = '{:<{width0}} {:>{width1}} {:^{width2}} {:>{width3}}\n'.format('Name', 'Total', 'Count', 'Average', width0=widths[0], width1=widths[1], width2=widths[2], width3=widths[3])
    output_string += "-" * (sum(widths) + 3) + "\n"
    for entry in donor_report_list:
        output_string += '{:<{width0}} ${:>{width1}.2f} {:^{width2}} ${:>{width3}.2f}\n'.format(entry[0], entry[1], entry[2], entry[3], width0=widths[0], width1=widths[1]-1, width2=widths[2], width3=widths[3]-1)
    print(output_string)
    return output_string


def all_letters_sub_menu():
    """
    prompts for single letter or all letters
    """
    menu_dict = {'s': single_letter,
                 'a': all_letters,
                 'q': quit_menu
                 }
    response = ""
    while response != 'q':
        print("Would you like to output a single letter or all letters?:")
        print('Single Letter: "s"\n'
              'All Letters: "a"\n'
              'Quit: "q"')
        response = input(' => ').lower()
        if menu_dict.get(response, unknown)() == "quit":
            break


def single_letter():
    """
    prompts for a donor, checks if the donor exists, if the donor does exist
    passes the donor to a function to create the letter
    """
    while True:
        print("Enter the donor name you would like to save a letter for:")
        print("(Type 'list' to see a full list of donors)")
        response = input(' => ').title()
        if response == "List":
            print('\n'.join(DC.list_donors()))
        else:
            if DC.find_donor(response):
                DC.find_donor(response).save_thank_you_letter()
                print("Donor Letter Saved\n")
            else:
                print("\n" + response + ' is not a current donor')
                print("NO LETTER SAVED. Please try again\n")
            return

def all_letters():
    """
    for each donor in the donor collection, saves a thank you letter
    """
    for d in DC.donors:
        d.save_thank_you_letter()
    return "quit"


def main():
    #print(initial_donor_load('donor_database.yaml'))
    print("Welcome to the Mailroom, you lucky duck!")
    print("")
    menu_dict = {'n': new_donation_sub_menu,
                 'r': report,
                 'l': all_letters_sub_menu,
                 'q': quit_menu
                 }
    response = ' '
    while True:
        print('Select from the following')
        print('Enter a New Donation: "n"\n'
              'View the Report: "r"\n'
              'Send letters to donors: "l"\n'
              'Quit: "q"')
        response = input(' => ')[:1].lower()
        if menu_dict.get(response, unknown)() == "quit":
            break

DC = Donor_Collection(initial_donor_load('donor_database.yaml'))

if __name__ == '__main__':
    main()
