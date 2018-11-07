#!/usr/bin/env python3

"""
mailroom assignment part 2 & 3
"""
from operator import itemgetter

# donors = [("Fred Jones", [100.01, 200, 300]),
#     ("Amy Shumer", [2000, 4000, 1000]),
#     ("Billy Bills", [1020, 20440.55, 300]),
#     ("Bob Sherlock", [10, 20, 30]),
#     ("Tom Johnson", [100, 200, 900])]

donors = {"Fred Jones": [100.01, 200, 300], "Amy Shumer": [2000, 4000, 1000],
"Billy Bills": [1020, 20440.55, 300], "Bob Sherlock": [10, 20, 30],
 "Tom Johnson": [100, 200, 900]}


def thank_you():
    answer = "s"
    while answer != "Q":
        print("Please input:\n"
        "A full name of donor\n"
        "Or type 'list' if you would like to see the entire list\n"
        "Or type 'Q' to quit.")
        answer = input("=> ").strip().title()
        if answer == 'List':
            print(donors.keys())
        elif answer.isalnum and answer != 'Q':
            add_donor(answer)
            break
        else:
            print("I am sorry, the name must be letters only")

def add_donor(donor_name):
    donation = add_money() # returns value or 0
    if donation >= 0.01:
        if donor_name in donors:
            donors[donor_name].append(add_money())
        else:
            donors[donor_name] = add_money()
        print("Thank you {} for your donation of ${:,.2f} dollars!".format(donor_name, float(donation)))
    else: print("Sorry donation must be larger than one cent!")

def add_money():
    donation = input("Please enter the donor amount => $")
    #TODO checks to make sure donation is greater than 0 and a number
    return donation

def report():
#TODO format with dictionary
    rpt_sheet = []
    name_max, give_max, count_max, avg_max = 0, 0, 0, 0
    for d in donors:
        if len(d[0]) > name_max:
            name_max = len(d[0])
        if len(str(sum(d[1]))) > give_max:
            give_max = len(str(sum(d[1])))
        if len((d[1])) > count_max:
            count_max = len((d[1]))
        if len(str(sum(d[1])/len(d[1]))) > avg_max:
            avg_max = len(str(sum(d[1])/len(d[1])))
        rpt_sheet.append((d[0], sum(d[1]), len(d[1]), sum(d[1])/len(d[1])))

    col1_size = int(max(len("Donor Name"), name_max) * 1.5)
    col2_size = int(max(len("Total Given"), give_max) * 1.25)
    col3_size = int(max(len("Num Gifts"), count_max) * 1.25)
    col4_size = int(max(len("Average Gift"), avg_max) * 1.25)

    print("Count max is: " + str(count_max))
    print(rpt_sheet)
    rpt_sheet.sort(key=return_total, reverse=True)
    print(rpt_sheet)
    sheet = "\n".join(("Donor Name" + (col1_size - len("Donor Name")) * " " +
     "| Total Given" + (col2_size - len("Total Given")) * " " +
     "| Num Gifts" + (col3_size - len("Num Gifts")) * " " +
     "| Average Gift" + (col4_size - len("Average Gift")) * " ",
     (col1_size + col2_size + col3_size + col4_size + 6) * "-"))

    for r in rpt_sheet:
        sheet = sheet + ("\n" + r[0] + (col1_size - len(r[0])) * " " +
        " $" + (col2_size - len(str(round(r[1], 2)))) * " " + str(round(r[1], 2)) +
        (col3_size - len(str(r[2]))) * " " + str(r[2]) +
        "   $" + (col4_size - len(str(round(r[3], 2))) - 3) * " " +  str(round(r[3], 2)))

    print(sheet)

def return_total(elem):
    return elem[1]

def main():
    print("Welcome to Mailroom!")
    answer = "s"
    menu = {'t': thank_you, 'r': report}
    while answer != "q":
        print("Please select from the following")
        print("Quit: 'q'\n"
                "Thank you: 't'\n"
                "Report: 'r'\n")
        answer = input("=> ").strip()[0:1].lower()
        if answer in menu:
            menu[answer]()

if __name__ == "__main__":
    main()
