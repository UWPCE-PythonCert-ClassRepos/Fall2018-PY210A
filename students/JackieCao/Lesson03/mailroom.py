#!/usr/bin/env python3
"""
mailroom
"""
donors = [("Fred Jones",[100, 200, 300]),
        ("Amy Shumer", [2000, 4000, 1000]),
        ("Bean Shing", [20, 400]),
        ("Ann Shaw", [2, 400]),
        ("King May", [200, 400, 100]),
        ]
# get a list of donor names
donor_names = []
for i in donors:
    donor_names.append(i[0])

# print donor names
def print_donors():
    for i in donors:
        print(i[0])


def thank_you():
# ask use for donor's name
    while True:
        name = input("Enter a donor's name " 
                "(or 'list' to see all donors or 'menu' to exit)>")
        if name == "list":
            print_donors()
        elif name == "menu":
            return
        else:
            break

# ask user for donation amount
    dollar = input("Enter a donation amount (or 'menu' to exit)>")
    if dollar == "menu":
        return
    dollar = float(dollar)

# add new name and donation amount to the donors history
    if name in donor_names:
        for i in donors:
            if name.lower() == i[0].lower():
                i[1].append(dollar)
    elif name not in donor_names:
        donors.append([name, dollar])

# print the thank you letter    
    print("Dear {},\n\n    Thank you for your donation of ${:.2f}.\n\nBest,\nDonation Group".format(name,dollar))


def make_report():
    data = []
    for (name, dollar) in donors:
        total_donated = sum(dollar)
        number_of_donations = len(dollar)
        average_donation = sum(dollar)/len(dollar)
        data.append((name,total_donated,number_of_donations,average_donation))
# sort the data
    data.sort(key=lambda tup: tup[0]) 
# format
    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
          "Donor's Name", "Total Donated", "Number of Donations", "Average$"))
    for row in data:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))

def main():
    print("hello")
    answer = ""
    while answer != "q":
        print("Please select from the following")
        print("Quit: 'q',\nSend a Thank you: 't',\nReport: 'r'")
        answer = input(" => ")
        answer = answer.strip()
        answer = answer[:1].lower()
        if answer == 't':
            thank_you()
        elif answer == 'r':
            make_report()


if __name__ == "__main__":
    main()

