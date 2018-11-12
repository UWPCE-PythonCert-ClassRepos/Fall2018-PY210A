#!/usr/bin/env python3
"""
mailroom2, use dicts
"""
donors = {"Fred Jones":[100, 200, 300],
        "Amy Shumer": [2000, 4000, 1000],
        "Bean Shing": [20, 400],
        "Ann Shaw": [2, 400],
        "King May": [200, 400, 100]
        }

# print donor names
def print_donors():
    for i in donors:
        print(i)


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
    if name in donors.keys():
        for i in donors:
            if name.lower() == i.lower():
                donors[i].append(dollar)
    elif name not in donors.keys():
        l_dollar = [dollar]
        donors[name] = l_dollar
    
    # print the thank you letter    
    d = {'d_name': name, 'd_dollar': dollar}

    print("Dear {d_name},\n\n    Thank you for your donation of ${d_dollar}.\n\nBest,\nDonation Group".format(**d))

def thank_to_all():
    for name in donors:
        total_donated = sum(donors[name])
        d = {'d_name': name, 'd_dollar': total_donated}
        letter = "Dear {d_name},\n\n    Thank you for your donation of ${d_dollar}.\n\nBest,\nDonation Group".format(**d)
        with open(name + '.txt', 'w') as f:
            f.write(letter)

def make_report():
    data = []
    for name in donors:
        total_donated = sum(donors[name])
        number_of_donations = len(donors[name])
        average_donation = total_donated/number_of_donations
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
        print("Quit: 'q',\nSend a Thank You to a single donor : 't',\nReport: 'r',\nSend letters to all donors: 's'")
        answer = input(" => ")
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

