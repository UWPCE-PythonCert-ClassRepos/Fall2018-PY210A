#!/usr/bin/env python3

"""
mailroom assignment
"""

players = {
    "LeBron James": [1000000, 2000000, 3000000],
    "Dwyane Wade": [100000, 20000, 30000],
    "Carmelo Anthony": [1],
    "Kevin Durant": [1, 2],
    "Michael Jordan": [2]
}

def thank_you(name):
    if name.lower() == "list":
        for player in players:
            print(player, players[player])

        print("\n")
    elif name not in players:
        print("Enter a donation for " + name)
        donation = int(input(" => "))
        players[name] = [donation]
        print("Hi {},\n\n"
              "Thank you for your donation of {} to the research center.\n\n"
              "Have a great day!".format(name, donation))

def make_report():
    print("Donor Name                | Total Given   | Num Gifts   | Average Gift\n"
"-------------------------------------------------------------------------")

    format = "%-20s  $ % 16f% 14i  $% 16f"

    for player in players:
        print(format % (player, sum(players[player]), len(players[player]), (sum(players[player]) / len(players[player]))))

def main():
    print("Welcome to Mailroom!")
    answer = ""
    while  answer != "q":
        print("Please select from the following")
        print("Quit: 'q', \n"
              "Thank you: 't'\n"
              "Report: 'r'")
        answer = input(" => ")
        answer = answer.strip()
        answer = answer[0:1].lower()
        if answer == 't':
            print("Enter a name:")
            name = input(" => ")

            thank_you(name)
        elif answer == 'r':
            make_report()


if __name__ == "__main__":
    main()