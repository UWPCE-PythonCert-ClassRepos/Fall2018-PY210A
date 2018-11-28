#!/usr/bin/env python3

"""
Mailroom 1
"""
import sys

donors = [("Robyn Rihanna", [100, 200, 300]),
          ("Ariana Grande", [2250, 4000, 1000]),
          ("Beyonce Carter-Knowles", [150000, 3500, 25000]),
          ("Aubrey Drake Graham", [15000, 5500.25, 1200]),
          ("Justin Bieber", [2500, 250, 750.50])
          ]


def print_donors():
    for donor in donors:
        print(donor[0])


def find_donor(name_entered):
    for donor in donors:
        if name_entered.strip().lower() == donor[0].lower():
            return donor
    return None


def send_email(name_entered, donation):
    print(
        """Dear {},

Your generous ${:,.2f} donation just made our day!

Thank you!
-The Charity""".format(name_entered.title(), donation)
    )


def thank_you():
    while True:
        name_entered = input("Enter the name of a donor or 'list' to view "
                             "donors >>> ").lower().strip()
        if name_entered == "list":
            print_donors()
        else:
            break

    donation = float(input("Enter donation amount >>> "))
    donor = find_donor(name_entered)
    if donor is None:
        donor = (name_entered.title(), [])
        donor[1].append(donation)
        donors.append(donor)
        print("Successfully added new donor to database")
    else:
        donor[1].append(donation)
        print("Successfully updated existing donor.")

    send_email(name_entered, donation)


def sort_key(donors):
    return donors[1]


def create_report():
    print("{:30s} | {:11s} | {:9s} | {:12s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 72)
    donors.sort(key=sort_key, reverse=True)
    for donor in donors:
        print("{:30s}  $ {:11,.2f}  {:9d}  $ {:12,.2f}".format(
              donor[0], sum(donor[1]), len(donor[1]),
              sum(donor[1]) / len(donor[1])))


def exit_program():
    print("Exiting Program. Goodbye!")
    sys.exit()


def main():
    print("Welcome to Mailroom!")
    while True:
        print("Select an option:")
        print("'r' - Create Report \n"
              "'t' - Send Thank You \n"
              "'q' - Quit")
        action = input(" >>> ")
        action = action.strip()
        action = action[0].lower()
        if action == 'r':
            create_report()
        elif action == 't':
            thank_you()
        elif action == 'q':
            exit_program()
        else:
            print("Not a valid option. Please select 't', 'q', or 'r'")


if __name__ == "__main__":
    main()
