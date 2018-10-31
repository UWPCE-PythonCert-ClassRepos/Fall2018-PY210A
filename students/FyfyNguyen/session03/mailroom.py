#!/usr/bin python3

"""
mailroom assignment
"""

donors = [("Fred Jones", [100, 200, 300]),
        ("Amy Schumer", [2000, 4000, 1000])
        ]

def thank_you():
    print("do the thank you think now")

def make_report():
    print("put report here")

def main():
    print("Welcome to Mailroom!")
    answer = ""
    while answer != "q":
        print("Please select from the following")
        print("Quit: 'q' \n"
            "Thank you: 't' \n"
            "Report: 'r'")
        answer = input(" => ")
        answer = answer.strip()
        answer = answer[0].lower()
        if answer == 't':
            thank_you()
        elif answer == 'r':
            make_report()


if __name__ == "__main__":
    main()