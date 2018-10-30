"""
mailroom assignment
"""

donors = [('Jimmy John', [100, 200, 300]),
          ('Amy Shumer', [2000, 4000, 1000]),
          ('Parker Pony', [2000, 10000]),
          ('Cher', [900, 9000, 2000]),
          ('Legolass Mario', [4000, 50])
          ]


def get_donors(donors):
    output = []
    for d in donors:
        output.append(d[0])
    return output


def add_money(person, money):
    for p in donors:
        if p[0] == person:
            p[1].append(money)


def thank_you():
    response = ""
    while response != 'Q':
        print("Enter the full name of donor:")
        print("(Type list to see a full list of donors)")
        response = input(' => ').title()
        if response == "List":
            print(get_donors(donors))
        else:
            if response not in donors:
                donors.append((response, []))
            print("Enter the donation amount for " + response + ":")
            money = input(' => ')
            add_money(response, money)
            print("\nThank you, {person} for your donation of {donation}. We couldn't do this without you!\n".format(person=response, donation='${:,.2f}'.format(float(money))))
            response = "Q"


def report():
    pass


def main():
    print("Welcome to the Mailroom, you lucky duck!")
    print("")
    response = ' '
    while response != 'q':
        print('Select from the following')
        print('Thank You: "t"\n' +
              'Report: "r"\n'
        'Quit: "q"')
        response = input(' => ')[:1].lower()
        if response == 't':
            thank_you()
        elif response == 'r':
            report()

if __name__ == '__main__':
    main()
