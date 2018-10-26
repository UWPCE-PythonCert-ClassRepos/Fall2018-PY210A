#!/usr/bin python3

"""
mailroom assignment
"""

donors = [("Fred Jones", [100, 200, 300]),
          ("Amy Shumer", [2000, 3000, 4000]),
          ]

def thank_you():
    print("Do the thank you think now.")

def make_report():
    print("Put report here.")

def main():
    print("Welcome to Mailroom!")
    answer = ''
    while answer != 'q':
        print("Please select from the following")
        print("Quit: 'q',\n"
            "Thank you:'t'\n"
            "Create a report: 'r'")
        answer = input(" => ")
        answer = answer.strip()
        answer = answer[:1].lower()
        if answer == 't':
            thank_you()
        elif answer == 'r':
            make_report()

if __name__ == "__main__":
    main()

