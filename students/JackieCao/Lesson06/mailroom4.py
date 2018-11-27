#!/usr/bin/env python3
"""
mailroom3
Improve mailroom by adding exceptions and comprehensions.
"""
import os
donors = {"Fred Jones":[100, 200, 100],
        "Bean Shing": [20, 400],
        "Ann Shaw": [100, 400],
        "King May": [200, 400]
        }

# print donor names
def return_donors_list():
    donors_list = [i for i in donors]
    return donors_list

def update_donors(name, dollar):
    # add new name and donation amount to the donors history
    if name.title() in donors:
        # use comprehensions
        who = [i for i in donors if name.lower() == i.lower()]
        donors[''.join(who)].append(dollar)
    else:
        l_dollar = [dollar]
        donors[name] = l_dollar
    return donors

def print_thank_you_letter(name, dollar):
    d = {'d_name': name, 'd_dollar': dollar}
    letter_text = "Dear {d_name},\n\n    Thank you for your donation of ${d_dollar}.\n\nBest,\nDonation Group".format(**d)
    return letter_text

def get_letter_context(name):
    with open(name + '.txt', 'r') as f:
        return f.read()

def get_letter_name(name):
    if name + '.txt' in os.listdir("."):
        return name + ".txt"

def get_report():
    # use comprehensions
    total_donated = [sum(donors[name]) for name in donors]
    number_of_donations = [len(donors[name]) for name in donors]
    average_donation = [t/d for t, d in zip(total_donated,
                                            number_of_donations)]
    names = [name for name in donors]
    data = [(name, dollar, num, ave) for name, dollar, num, ave in zip(names,
                                                                       total_donated,
                                                                       number_of_donations,
                                                                       average_donation)]
    # sort the data
    data.sort(key=lambda tup: tup[0])
    # format
    rows = "{:15s} | {:11s} | {:9s} | {:12s}".format(
             "Donor's Name", "Total Donated", "Number of Donations", "Average$")
    for row in data:
        a_row = "{:15s}   {:11.2f}   {:9d}   {:18.2f}".format(*row)
        rows = (rows + "\n" +  a_row)
    return rows

def thank_you():
    # ask user for donor's name
    while True:
        # add exception
        try:
            name = input("Enter a donor's name "
                        "(or 'list' to see all donors or 'menu' to exit)>")
        except (KeyboardInterrupt, EOFError):
            return None
        if name == "list":
            print(return_donors_list())
        elif name == "menu":
            return
        else:
            break

    # ask user for donation amount
    while True:
        # add exception
        try:
            dollar = input("Enter a donation amount (or 'menu' to exit)>")
        except (KeyboardInterrupt, EOFError):
            return None
        if dollar == "menu":
            return
        # add exception
        try:
            dollar = float(dollar)
        except ValueError:
            print("Input must be a number")
        else:
            break

    # add new name and donation amount to the donors history
    donors = update_donors(name, dollar)
    # print the thank you letter
    letter_text = print_thank_you_letter(name, dollar)
    print(letter_text)

def thank_to_all():
    for name in donors:
        total_donated = sum(donors[name])
        d = {'d_name': name, 'd_dollar': total_donated}
        letter = "Dear {d_name},\n\n    Thank you for your donation of ${d_dollar}.\n\nBest,\nDonation Group".format(**d)
        with open(name + '.txt', 'w') as f:
            f.write(letter)
        print("The thank you letter for {d_name} has been sent".format(**d))

def make_report():
    # use comprehensions
    total_donated = [sum(donors[name]) for name in donors]
    number_of_donations = [len(donors[name]) for name in donors]
    average_donation = [t/d for t, d in zip(total_donated,
                                            number_of_donations)]
    names = [name for name in donors]
    data = [(name, dollar, num, ave) for name, dollar, num, ave in zip(names,
                                                                       total_donated,
                                                                       number_of_donations,
                                                                       average_donation)]
    # sort the data
    data.sort(key=lambda tup: tup[0])
    print(get_report())
def main():
    print("hello")
    answer = ""
    while answer != "q":
        print("Please select from the following")
        print("Quit: 'q',\nSend a Thank You to a single donor : 't',\nReport: 'r',\nSend letters to all donors: 's'")
        try:
            answer = input(" => ")
        except (KeyboardInterrupt, EOFError):
            return None
        answer = answer.strip()
        answer = answer[:1].lower()
        if answer == 't':
            thank_you()
        elif answer == 'r':
            make_report()
        elif answer == 's':
            thank_to_all()


if __name__ == "__main__":
    main()

