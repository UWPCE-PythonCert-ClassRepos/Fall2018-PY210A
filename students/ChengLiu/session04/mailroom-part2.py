#!/usr/bin/env python3

"""
PY210A-Session 04
Cheng Liu
Mail-room Part 2
"""


import sys

donors = {'fred jones': ("Fred Jones", [100, 200, 300]),
          'amy shume': ("Amy Shume", [2000, 1000, 3000]),
          'david cool': ("David Cool", [1000]),
          }


def show_donors():
    current_donor = []
    for donor in donors.values():
        current_donor.append(donor[0])
    return "\n".join(current_donor)


def find_donors(name):
    key = name.strip().lower()
    return donors.get(key)


def menu():
    print("\n\n\n" + "Choose an action:")
    print("1 - Send a Thank You to a single donor."
          "\n2 - Create a Report."
          "\n3 - Send letters to all donors."
          "\n4 - Quit.")
    selection = input("=> ")
    selection = selection.strip().lower()
    selection = selection[0:1]  # in case only enter key, no values
    return selection


def email_note(name):
    key = name.strip().lower()
    return ("-" * 55 + "\nHello {}! Thank you for your donation of ${:.2f}.".format(donors.get(key)[0].capitalize(), donors.get(key)[1][-1]) + "\n" + "-" * 55)


def thank_you():
    name = ""
    while True:
        name = input("Enter 'list' to show the donors "
                     "or enter a Name to send a Thank You note, "
                     "or 'q' to quit.")
        name = name.strip().lower()
        donor = find_donors(name)
        if name == "list":
            print(show_donors())
        elif name == 'q':
            break
        elif donor is None:
            donation = float(input("Enter the amount: "))
            donors[name] = (name.capitalize(), [donation])
            print(email_note(name))
        else:
            print(email_note(name))


def report():
    report_rows = []
    for (donor, donation) in donors.values():
        total_given = sum(donation)
        num_gifts = len(donation)
        avg_gift = total_given / num_gifts
        report_rows.append((donor, total_given, num_gifts, avg_gift))

    print("{:<25s} | {:>11s} | {:>9s} | {:>12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 70)

    for row in report_rows:
        print("{:<25s}   {:>11.2f}   {:>9d}   ${:>12.2f}".format(row[0], row[1], row[2], row[3]))


def save_to_disk():
    for donor in donors.values():
        letter = email_note(donor[0])
        open('letters.txt', 'a').write(letter)


def quit():
    sys.exit(0)


if __name__ == "__main__":
    running = True
    selection_dict = {"1": thank_you,
                      "2": report,
                      "3": save_to_disk,
                      "4": quit}
    while running:
        selection = menu().strip()
        selection_dict.get(selection)()
