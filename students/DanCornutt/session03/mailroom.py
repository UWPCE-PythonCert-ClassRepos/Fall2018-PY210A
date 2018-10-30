#!/usr/bin/env python3

"""
mailroom assignment
"""
from operator import itemgetter

donors = [("Fred Jones", [100, 200, 300]),
    ("Amy Shumer", [2000, 4000, 1000]),
    ("Billy Bills", [1020, 20440, 300]),
    ("Bob Sherlock", [10, 20, 30]),
    ("Tom Johnson", [100, 200, 900])]


def thank_you():
    print('do the thank you thing now!')
    answer = ""
    while answer != "Q":
        print("Please input a full name of donor or type 'list' if you would like to see the entire list")
        answer = input("=> ")
        answer = answer.strip()
        answer = answer.title()
        if answer == 'List':
            for k in donors:
                print(k[0])
        else:
            if answer not in donors:
                donors.append((answer, []))
            donation = input("Please enter the donor amount => $")
            add_money(answer, donation)
            break
    email_body = "Thank you {} for your donation of ${:,.2f} dollars!".format(answer, float(donation))
    print(email_body)

def add_money(donor, donation):
    for d in donors:
        if d[0] == donor:
            d[1].append(donation)






def report():
    print('do the report thing now!')


def main():
    print("Welcome to Mailroom!")
    answer = "s"
    while answer != "q":
        print("Please select from the following")
        print("Quit: 'q'\n"
                "Thank you: 't'\n"
                "Report: 'r'\n")
        answer = input("=> ")
        answer = answer.strip()
        answer = answer[0:1].lower()
        if answer == 't':
            thank_you()
        elif answer == 'r':
            report()

if __name__ == "__main__":
    main()
