#!/usr/bin/env python3

"""
mailroom assignment part 2 & 3
"""
from operator import itemgetter
from collections import OrderedDict


DONORS = {
    "Fred Jones": [100.01, 200, 300], "Amy Shumer": [2000, 4000, 1000],
    "Billy Bills": [1020, 20440.55, 300], "Bob Sherlock": [10, 20, 30],
    "Tom Johnson": [100, 200, 900]
    }

WELCOME_PROMPT = (
    "Welcome to the main menu, please select from the following\n"
    "Quit: 'q'\n"
    "Thank you: 't'\n"
    "Report: 'r'\n"
    )

THANK_YOU_PROMPT: (
    "Welcome to the thank you menu, please select from the following:\n"
    "Type a full name of donor to see their donations or add new donor\n"
    "Type 'list' if you would like to see the entire donor list\n"
    "Type 'Q' to quit this menu."

)


def thank_you():
    """Prompts for user input thank you menu responseselfself.
    Validates repsonse is expected, repeats menu if not.
    """
    answer = "q"
    while answer != "Q":
        print(
            "Please input:\n"
            "A full name of donor\n"
            "Or type 'list' if you would like to see the entire list\n"
            "Or type 'Q' to quit this menu.")
        answer = input("=> ").strip().title()
        if answer == 'List':
            donor_list()
        elif not answer.isalnum or answer.upper() != 'Q':
            add_donation(answer)
            continue
        else:
            print("I am sorry, the name must be letters only")


def add_donation(donor_name):
    """adds donation to donor records, adds donor if new donor

    :param1: donar name
    """
    donation = add_money()
    if donation:
        DONORS.setdefault(donor_name, []).append(donation)
        print(
            "Thank you {} for your donation of ${:,.2f} dollars!".format(
                donor_name, float(donation))
        )


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
        return float(donation)

def report():
    rpt_sheet = []
    len_col = OrderedDict({
        "n_size": len("Donor Name"),
        "t_size" : len("Total Given"),
        "ng_size": len("Num Gifts"),
        "ag_size": len("Average Gift")
    })

    for d in DONORS.items():
        if len(d[0]) > len_col["n_size"]:
            len_col["n_size"] = len(d[0])
        if len(str(sum(d[1]))) > len_col["t_size"]:
            len_col["Tt_size"] = len(str(sum(d[1])))
        if len((d[1])) > len_col["ng_size"]:
            len_col["ng_size"] = len((d[1]))
        if len(str(sum(d[1])/len(d[1]))) > len_col["ag_size"]:
            len_col["ag_size"] = len(str(sum(d[1])/len(d[1])))
        rpt_sheet.append((d[0], sum(d[1]), len(d[1]), sum(d[1])/len(d[1])))
    rpt_sheet.sort(key=return_total, reverse=True)

    sheet = (
        "{nm:{mnm}} | {tot:<{mtot}} | {ng:<{mng}} | {ag:<{mag}}\n{header}".format(
            nm="Donor Name", mnm=len_col["n_size"],
            tot="Total Given", mtot=len_col["t_size"],
            ng="Num Gifts", mng=len_col['ng_size'],
            ag="Average Gift", mag=len_col["ag_size"],
            header=("-" * sum(len_col.values()))
        )
    )
    for d in rpt_sheet:
        sheet = sheet + (
            "\n{n:{n_size}} |${t:>{t_size},.2f} | {ng:>{ng_size}} |$ {avg_g:<{ag_size},.2f}"
            .format(
                n=d[0], n_size=len_col['n_size'],
                t=d[1], t_size=len_col['t_size'],
                ng=d[2], ng_size=len_col['ng_size'],
                avg_g=d[3], ag_size=len_col['ag_size']
                )
        )
    print(sheet)


def return_total(elem):
    """sorting function for list"""
    return elem[1]


def donor_list():
    """prints donor in dict"""
    for k in DONORS:
        print(k)


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
