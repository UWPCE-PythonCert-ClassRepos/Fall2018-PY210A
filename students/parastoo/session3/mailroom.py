#!/usr/bin env python3
'''mailroom assignment.'''
from __future__ import division
import sys

# list of five donors and the amount of their donations
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Ellon Musk", [1000.05, 500.97, 150.30])]

'''
The prompt to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”
'''
prompt = '\n'.join(("Please choose one of the following options:",
                    "'q' - Quit",
                    "'r' - Create a Repot",
                    "'t' - Send a Thank you note",
                    ">>>"))

# the prompt for thank_you()
thank_you_prompt = '\n'.join(("\nPlease choose from the following options:",
                              "'l' - View the list of donors",
                              "'t' - Send a thank you note",
                              "'q' - Return to the main page",
                              ">>>"))

# a list of donors and a list of donations
donor_list = [donor_db[idx][0] for idx in range(len(donor_db))]
donation_list = [donor_db[idx][1] for idx in range(len(donor_db))]


def view_donors():
    '''shows the list of donors'''
    print('\n'.join(donor_list))


def add_donor(donor, donation):
    '''add a new donor to the donor_db)'''
    new_donor_pair = (donor, donation)
    donor_list.append(donor)
    donation_list.append(donation)
    donor_db.append(new_donor_pair)
    print('\n'.join(donor_list))


def add_donation(donor, donation):
    for row in donor_db:
        if row[0] == donor:
            row[1].append(donation)


def donation_sum(idx):
    total_donation = sum(donor_db[idx][1])
    return total_donation


def donation_average(idx):
    return donation_sum(idx) / (len(donor_db[idx][1]))


def thank_you():
    '''This function allow the user to:
    1) get a list of the donor names and re-prompt.
    2) add a new donor to the data structure and use it.
    3) choose a donor from the list and use it.
    4)'''

    print("\nYou can now send a thank you note.")

    answer = ""

    while answer != 'q':
        answer = input(thank_you_prompt)

        # make a list of donor names and re-prompt
        if answer == 'l':
            print('\n')
            view_donors()

        # send a thank you note
        elif answer == 't':
            donor = input("\nPlease Enter the donor's full name\n>>>")

            # send a thank you note to an already existing donor
            if donor in donor_list:
                print('\nA thank you note was sent to', donor)
                # add a donation
                donation = int(input('\nEnter the donation:\n>>>'))
                add_donation(donor, donation)

            # add a new donor and send a thank you note and add a new donation
            else:
                print('The donor was not found!')
                add_request = input(
                    "\nWould you like to add the donor to the donor names?(y/n)")
                if add_request == 'y':
                    donation_amount = int(input("\nThe amount of donation:"))
                    add_donor(donor, donation_amount)

        # quit the thank_you function
        elif answer == 'q':
            print('\n')
        else:
            print('Not a valid option!')


def make_report():

    print('Donar Name          |      Total Given    | Num Gifts | Average Gift')
    print('-----------------------------------------------------------------------------')
    for idx in range(len(donor_db)):
        format = "%-20s  $ % 16f% 14i  $% 16f"
        print(format % (donor_db[idx][0], donation_sum(
            idx), len(donor_db[idx][1]), donation_average(idx)))


def main():
    print("Welcome to the Mailroom!")
    answer = input(prompt)
    while answer != 'q':
        answer = answer[:1].lower()
        answer = answer.strip()
        if answer == 't':
            thank_you()
        elif answer == 'r':
            make_report()
        else:
            print("Bye!")
            sys.exit()
        answer = input(prompt)

if __name__ == '__main__':
    main()
