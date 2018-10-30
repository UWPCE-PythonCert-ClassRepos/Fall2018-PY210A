#!/usr/bin/env python3

""" Mailroom exercise
"""
donors = [("Jim Rockford", [325, 300, 125]),
          ("Jed Clampet", [1555, 2000, 1200]),
          ("Tony Nelson", [75, 100, 105]),
          ("Marcia Brady", [15, 10]),
          ("Samantha Stevens", [105, 100, 200]),
         ]

def thank_you():
    inp = input("Please provide Full Name or 'list' to see donors")
    for name,donat in donors:
        if inp.lower() == "list":
            print("Current list of donors: ", name)
            thank_you()
        elif inp.lower() == name:
            print(name)
        

#    print("Many thanks for your generosity")

def make_report():
    print("Report summary: ")

def main():
    print("Greetings and Salutations. Welcome to the Mailroom!")
    answer = ""
    while answer != "q":
        print("Please select from the following")
        print("Quit: 'q', \n"
              "Thank you: 't'\n"
              "Report: 'r'")
        answer = input(" => ")
        answer = answer.strip()
        answer = answer[0:1].lower()
        if answer == 't':
            thank_you()
        elif answer == 'r':
            make_report()

if __name__ == "__main__":
    main()
