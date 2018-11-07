#!/usr/bin/env python3

"""
PY210A-Session03
Cheng Liu
Mailroom Part 1
"""

donors = [("Fred Jones", [100, 200, 300]), ("Amy Shume", [2000, 1000, 3000])]


def thank_you():
    FN = ""
    selection = None
    while True:
        FN = input("Type 'list' to show the donor names, or enter the Full Name to send a Thank You: ")
        FN = FN.lower()
        if FN == "list":
            for donor in donors:
                print(donor[0])
        elif FN not in donors:
            donors.append(FN)
            selection = FN
        else:
            selection = FN







        else:
            print("If tuypes a name not in the list, add the name; if in the list, use it")

        dollar = input("Enter the donation amount: $")
        dolloar = float(dollar)

        donors = donors.append(FN, dollar)

        print(FN + ", Thank you for your donations!")







def report():
    print('Donor Name' + ' ' * 20 +' | ' + 'Total Given' + ' | ' + 'Num Gifts' + ' | ' + 'Average Gift')
    print('-' * 71)
    for donor in donors:
        print(donor[0] + ' ' *(32-len(donor[0]))+ '$' 
              + ' ' * (12 - len(str(donor[1][0])))+str(donor[1][0]) 
              + ' ' * (12 - len(str(donor[1][1])))+ str(donor[1][1]) + '  $'
              + ' ' * (11 - len(str(donor[1][2])))+ str(donor[1][2]))

def main():
    print("Welcome to Mailroom!")
    answer = ""
    while answer != "Q":
        print("Please select from the following:")
        print("Quit: 'Q'"
              "\nSend a Thank You: 'T'"
              "\nCreate a Report: 'R'")
        answer = input("=> ")
        answer = answer.strip()  # in case entering the space at the beginning
        answer = answer[0:1].lower()  # in case only enter key, no values
        if answer == "t":
            thank_you()
        elif answer == "r":
            report()


if __name__ == "__main__":
    main()
