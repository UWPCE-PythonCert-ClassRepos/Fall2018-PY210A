#!/usr/bin/env python3

"""
mailroom assignment part 2 & 3
"""
from operator import itemgetter

DONORS = {
    "Fred Jones": [100.01, 200, 300], "Amy Shumer": [2000, 4000, 1000],
    "Billy Bills": [1020, 20440.55, 300], "Bob Sherlock": [10, 20, 30],
    "Tom Johnson": [100, 200, 900]
    }

WELCOME_PROMPT = (
    "Welcome, please select from the following\n"
    "Quit: 'q'\n"
    "Thank you: 't'\n"
    "Report: 'r'\n"
    )

THANK_YOU_PROMPT: (
    "Thank you menu, please select from the following:\n"
    "Type a full name of donor to see their donations or add new donor\n"
    "Type 'list' if you would like to see the entire donor list\n"
    "Type 'Q' to quit this menu."

)



def thank_you():
    """Prompts for user input thank you menu response. Validates repsonse is expected, repeats menu if not.
    """
    answer = "q"
    while answer != "Q":
        print(
            "Please input:\n"
            "A full name of donor\n"
            "Or type 'list' if you would like to see the entire list\n"
            "Or type 'Q' to quit.")
        answer = input("=> ").strip().title()
        if answer == 'List':
            donor_list()
        elif answer.isalnum and answer != 'Q':
            add_donation(answer)
            break
        else:
            print("I am sorry, the name must be letters only")


def add_donation(donor_name):
    """adds donation to donor records, adds donor if new donor

    :param1: donar name
    """
    donation = add_money()
    if not donation:
        if donor_name in DONORS.keys():
            DONORS[donor_name].append(donation)
        else:
            DONORS[donor_name] = donation
        print(
            "Thank you {} for your donation of ${:,.2f} dollars!".format(
                donor_name, float(donation))
        )
    else:
        print("Exiting donation menu.")
        quit_menu()


def add_money():
    """Takes input from user, validates donation

    :returns: donation amount or None if donation is invalid.
    """
    donation = input("Please enter the donor amount larger than 0.01 => $")
    try:
        if float(donation) < 0.01:
            raise ValueError
    except ValueError:
        print("Donation Error, numbers only. Value must be number greater than 0.01")
        return None
    else:
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


def donor_list():
    """prints donor in dict"""
    print(DONORS.keys())


def unknown():
    """Handles unknown user input"""
    print("That is not a valid response!")


def quit_menu():
    """Quits menu, returns 'exit menu'. """
    print("Quitting this menu now.")
    return "exit menu"


def menu_selection(prompt, dispatch_dict):
    """dispatch function for mailroom"""
    while True: #this loops forever, until quit is selected
        response = input(prompt).strip()
        response = response[:1].lower()
        if dispatch_dict.get(response, unknown)() == "exit menu":
            break

MAIN_DISPATCH = {
    "t": thank_you,
    "r": report,
    "q": quit_menu
    }

# THANK_YOU_DISPATCH = {
#     "l": donor_list,
#     "q": quit_menu
# }

if __name__ == "__main__":
    menu_selection(WELCOME_PROMPT, MAIN_DISPATCH)
