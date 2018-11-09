#!/usr/bin/env python3
"""
mailroom3
Improve mailroom by adding exceptions and comprehensions.
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
    if name.title() in donors:
        # use comprehensions
        who = [i for i in donors if name.lower() == i.lower()]
        donors[''.join(who)].append(dollar)
    else:
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
    # use comprehensions
    total_donated = [sum(donors[name]) for name in donors]
    number_of_donations = [len(donors[name]) for name in donors]
    average_donation = [t/d for t, d in zip(total_donated,
                                            number_of_donations)]
    names = [name for name in donors]
    data = [(name, dollar, num, ave) for name, dollar, num, ave in zip(names,
                                                                       total_donated,
                                                                       number_of_donations,
                                                                       average_donation)]
    # sort the data
    data.sort(key=lambda tup: tup[0])
    # format
    print("{:15s} | {:11s} | {:9s} | {:12s}".format(
          "Donor's Name", "Total Donated", "Number of Donations", "Average$"))
    for row in data:
        print("{:15s}   {:11.2f}   {:9d}   {:18.2f}".format(*row))

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

