#!/usr/bin/env python3

"""
mailroom assignment
"""

donors = [("Fred Jones", [100, 200, 300]),
    ("Amy Shumer", [2000, 4000, 1000])]

def thank_you():
    print('do the thank you thing now!')

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
    print("Hello, Hi!")
    main()
