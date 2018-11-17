#!/usr/bin/env python3

"""
PY210A-Session03
Cheng Liu
Mailroom Part 1
"""

donors = [("Fred Jones", [100, 200, 300]),
          ("Amy Shume", [2000, 1000, 3000]),
          ("David Cool", [1000])]


def show_donors(donors):
    print("Current donors: ")
    for donor in donors:
        print(donor[0])


def find_donors(name):
    for donor in donors:
        if name.strip().lower() == donor[0].lower():
            return donor
    return None


def menu():
    print("\n\n\n" + "-" * 25 + "\nWelcome to Mail-room!")
    print("Please select an option from the following:")
    print("Quit: 'Q'"
          "\nSend a Thank You: 'T'"
          "\nCreate a Report: 'R'")
    selection = input("=> ")
    selection = selection.strip().lower()
    selection = selection[0:1]  # in case only enter key, no values
    return selection


def email_note(donor):
    return ("-" * 55 + "\nHello {}! Thank you for your donation of ${:.2f}.".format(donor[0].capitalize(), donor[1][-1]) + "\n" + "-" * 55)


def thank_you():
    name = ""
    while True:
        name = input("Enter 'list' to show the donors or enter a Name to send a Thank You note: ")
        name = name.lower()
        donor = find_donors(name)
        if name == "list":
            show_donors(donors)
        elif donor is None:
            donation = float(input("Enter the amount: "))
            new_donor = (name.capitalize(), [donation])
            donors.append(new_donor)
            print(email_note(new_donor))
        else:
            print(email_note(donor))
            break


def report():
    report_rows = []
    for (donor, donation) in donors:
        total_given = sum(donation)
        num_gifts = len(donation)
        avg_gift = total_given / num_gifts
        report_rows.append((donor, total_given, num_gifts, avg_gift))

    print("{:<25s} | {:>11s} | {:>9s} | {:>12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 70)

    for row in report_rows:
        print("{:<25s}   {:>11.2f}   {:>9d}   ${:>12.2f}".format(row[0], row[1], row[2], row[3]))


if __name__ == "__main__":
    running = True
    while running:
        selection = menu()
        if selection == "t":
            thank_you()
        elif selection == "r":
            report()
        elif selection == "q":
            running = False
        else:
            print("please select the right option.")
