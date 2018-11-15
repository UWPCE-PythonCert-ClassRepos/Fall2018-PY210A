import tempfile

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


def safe_input(message=""):
    try:
        get_input = input ("=> " + message)
    except KeyboardInterrupt:
        return None
    except EOFError:
        return None
    return get_input


def thank_you(name):
    if name.lower() == "list":
        for player in players:
            print(player, players[player])

        print("\n")
    elif name not in players:
        print("Enter a donation for " + name)
        donation = safe_input()
        if donation == None:
            return
        players[name] = [int(donation)]
        print("Hi {},\n\n"
              "Thank you for your donation of {} to the research center.\n\n"
              "Have a great day!".format(name, donation))
    elif name in players:
        donation = sum(players[name])

        email = ("Hi {},\n\n"
              "Thank you for your donation of {} to the research center.\n\n"
              "Have a great day!".format(name, donation))

        print(email)


def send_all_donors():
    for player in players:
        donation_sum = sum(players[player])
        email_path = tempfile.gettempdir() + '\\' + player + ".txt"

        email_body =("Hi {},\n\n"
              "Thank you for your donation of {} to the research center.\n\n"
              "Have a great day!".format(player, donation_sum))

        file = open(email_path, 'w')
        file.write(email_body)
        file.close()

        print('Email saved to ', email_path)


def make_report():
    print("Donor Name                | Total Given   | Num Gifts   | Average Gift\n"
"-------------------------------------------------------------------------")

    format = "%-20s  $ % 16f% 14i  $% 16f"

    for player in players:
        print(format % (player, sum(players[player]), len(players[player]), (sum(players[player]) / len(players[player]))))


def main():
    print("Welcome to Mailroom!")
    answer = ""
    while answer != "4":
        print("Please select from the following")
        print("1 - Send a Thank You to a single donor.\n"
              "2 - Create a Report.\n"
              "3 - Send letters to all donors.\n"
              "4 - Quit")
        answer = safe_input()
        if answer == None:
            return
        answer = answer.strip()
        answer = answer[0:1].lower()
        if answer == '1':
            print("Enter a name:")
            name = safe_input()
            if name == None:
                return
            thank_you(name)
        elif answer == '2':
            make_report()
        elif answer == '3':
            send_all_donors()


if __name__ == "__main__":
    main()