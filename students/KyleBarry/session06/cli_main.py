from mailroom_04 import Donor, DonorManager

dm = DonorManager()
a = Donor("Susan")
b = Donor("Betsy")
c = Donor("Gary")
d = Donor("Mary")


def nothing():
    pass


def exiting():
    """Return exiting, which breaks out of loops"""
    print("Goodbye!")
    quit()


def donor_input():
    while True:
        answer = input(info_prompt)
        try:
            info_dispatch[answer]()
            break
        except KeyError:
            print("Please make a valid selection")


def print_donors():
    for donor in dm.donors.values():
        print(donor.name)


def generate_report():
    dm.make_report()
    format_string = "{:<20}|{:>20}|{:>20}|{:>20}"
    print("{:^20}|{:^20}|{:^20}|{:^20}".format("Donor Name",
                                               "No. Donations",
                                               "Avg. Donation",
                                               "Total Donations\n"))

    for k, v in dm.donors.items():
        print(format_string.format(k,
                                   str(v.num_donations),
                                   "$" + str(round(v.average_donation)),
                                   "$" + str(v.total_donations)))

    print('\n')


def display_prompter():
    while True:
        person = input("Which donor would you like statistics on? ")
        try:
            print(dm.display_donor(person))
            break
        except KeyError:
            print("That donor is not in our registry")
            break

def make_donation_prompter():
    answer = input("On behalf of which donor would you like to donate? ")
    donation = input("How much would you like to donate? ")
    try:
        donation = int(donation)
        try:
            dm.donors[answer].add_donation(donation)
            dm.donors[answer].make_thank_you_file()
            print("Thank you! A confirmation email will be sent shortly")
        except KeyError:
            print("That donor is not in our registry")
    except ValueError:
        print("Please enter a whole number")


def add_donor():
    answer = input("Please enter the name of the new donor: ")
    if answer in dm.donors:
        print("A donor with that name already exists")
    else:
        Donor(answer)
        print("Successfully added new donor!")


def main(prompt, options_dict):
    """Get input from user and call appropirate function"""
    print("Welcome to the mailroom!")
    while True:
        answer = input(prompt)
        try:
            options_dict[answer]()
        except KeyError:
            print("Please make a valid choice")


"""Establish dispatch dictionaries and prompts"""
options_dict = {"1": donor_input, "2": make_donation_prompter, "3": exiting}

info_dispatch = {"1": print_donors, "2": display_prompter, "3": add_donor,
                 "4": generate_report, "5": nothing}


info_prompt = """Please select one of the following
(1): Display list of donors
(2): Get details about donors
(3): Add new donor
(4): Make donor report (csv format)
(5): Back to main menu
"""


prompt = """Please enter one of the following:
(1): Donor Information
(2): Make Donation
(3): Quit
"""

if __name__ == '__main__':
    main(prompt, options_dict)

