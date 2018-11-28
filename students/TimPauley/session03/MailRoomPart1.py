#Tim Pauley
#Python 201a HW3
#Date Oct 25 2018
#Mail Room Part 1

from textwrap import dedent 
import math

#Create Users in tuble
donor_database = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

#Print Donors
def print_donors():
    print("Donor list:\n")
    for donor in donor_db:
        print(donor[0])


def find_donor(name):
    for donor in donor_db:
        if name.strip().lower() == donor[0].lower():
            return donor
    return None


def main_menu():
    action = input(dedent('''
      Choose an action:
      't' - Send a Thank You
      'r' - Create a Report
      'q' - Quit
      > '''))
    return action.strip()


def create_letter(donor):
    return dedent('''
          Dear {}
          Thank you for your very kind donation of ${:.2f}.
          It will be put to very good use.
                         Sincerely,
                            -The Team
          '''.format(donor[0], donor[1][-1]))


def send_thank_you():
    while True:
        name = input("Enter a donor's name "
                     "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            print_donors()
        elif name == "menu":
            return
        else:
            break
    while True:
        amount_str = input("Enter a donation amount (or 'menu' to exit) > ").strip()
        if amount_str == "menu":
            return
        amount = float(amount_str)
        if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
            print("error: donation amount is invalid\n")
            continue  
        else:
            break

    donor = find_donor(name)
    if donor is None:
        donor = (name, [])
        donor_db.append(donor)
    donor[1].append(amount)

    print(crete_letter(donor))

#Sort Key
def sort_key(item):
    return item[1]

#print report
def print_donor_report():
    report_rows = []
    for (name, gifts) in donor_db:
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    report_rows.sort(key=sort_key)
    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 66)
    for row in report_rows:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))

#Main Method
if __name__ == "__main__":
    running = True
    while running:
        selection = main_menu_selection()
        if selection == "t":
            send_thank_you()
        elif selection == "r":
            print_donor_report()
        elif selection == "q":
            running = False
        else:
            print("error: menu selection is invalid!")
