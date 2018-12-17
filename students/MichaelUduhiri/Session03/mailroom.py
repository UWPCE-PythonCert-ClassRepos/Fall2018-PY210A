#List of donors
donors = [("Steve Rogers", [100, 200, 300]),
        ("Peter Parker", [200, 400, 600]),
        ("Natasha Romanoff", [550, 1100, 2200]),
        ("Scott Lang", [1345, 5090, 10500]),
        ("Tony Stark", [20000, 40000, 60000]),
        ]

def print_donors():
    print("Donor list:\n")
    for donor in donors:
        print(donor[0])

def find_donor(donorname):
    for donor in donors:
        if name.strip().lower() == donor[0].lower():
            return donor
        return None



def thankyou():
    while True:
        donorname = input("Please enter a donor's name")
        if donorname == "list":
            print_donors()
    elif donorname not in donors:
        donors.append(donorname)
    else:
        print("\n".join(donors))
        return donation()
        break

    while True:
        donation_amount = int(input("Please enter a donation amount"))
        print(" Thank you")
    #donors.append(donation_amount)

def generate_letter(donorname):
    return dedent('''
        Dear {}

        Thank you for your donation of ${:.2f}.

        '''.format(donor[0], donor[1][-1]))

def create_report():
#List view of the report data
    report_rows = []
    for (name, gifts) in donors:
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))
#Sort the report data
    report_rows.sort(key=sort_key)
    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
        print("-" * 66)
        for row in report_rows:
            print("{:25s}     {:11.2f}     {:9d}     {:12.2f}".format(*row))




def quitprogram():
    print("Goodbye!")
    sys.exit()


def main_menu():
    print ("Welcome to the Mailroom!")
    menu_select = input('''
        Please select from one of the following:

        't' - Send a Thank you
        'r' - Create a report of the donor list
        'q' - Quit

    > '''))

if __name__ == "__main__":
    running = True
    while running:
        selection = main_menu_selection
        if selection == "t":
            thank_you()
        elif selection == "r":
            print donorreport
        elif selection == "q":
            running = False
        else:
            print("error: Your selection is invalid!")
