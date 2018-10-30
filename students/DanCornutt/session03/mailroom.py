#!/usr/bin/env python3

"""
mailroom assignment
"""
from operator import itemgetter

donors = [("Fred Jones", [100.01, 200, 300]),
    ("Amy Shumer", [2000, 4000, 1000]),
    ("Billy Bills", [1020, 20440.55, 300]),
    ("Bob Sherlock", [10, 20, 30]),
    ("Tom Johnson", [100, 200, 900])]


def thank_you():
    print('do the thank you thing now!')
    answer = ""
    while answer != "Q":
        print("Please input a full name of donor or type 'list' if you would like to see the entire list")
        answer = input("=> ")
        answer = answer.strip()
        answer = answer.title()
        if answer == 'List':
            for k in donors:
                print(k[0])
        else:
            if answer not in donors:
                donors.append((answer, []))
            donation = input("Please enter the donor amount => $")
            add_money(answer, donation)
            break
    email_body = "Thank you {} for your donation of ${:,.2f} dollars!".format(answer, float(donation))
    print(email_body)

def add_money(donor, donation):
    for d in donors:
        if d[0] == donor:
            d[1].append(donation)


def report():
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


def main():
    print("Welcome to Mailroom!")
    answer = "s"
    while answer != "q":
        print("Please select from the following")
        print("Quit: 'q'\n"
                "Thank you: 't'\n"
                "Report: 'r'\n")
        answer = input("=> ")
        answer = answer.strip()
        answer = answer[0:1].lower()
        if answer == 't':
            thank_you()
        elif answer == 'r':
            report()

if __name__ == "__main__":
    main()
