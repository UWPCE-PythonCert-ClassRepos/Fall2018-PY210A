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


def stats(donations):
    name = donations[0]
    total = 0
    for d in donations[1]:
        total += float(d)
    num_of_donations = len(donations[1])
    avg_of_donations = total / num_of_donations
    return [name, total, num_of_donations, avg_of_donations]


def longest(values, min=10):
    """
    takes a list of values and returns the length of the longest value
    """
    cur_longest = 10
    for i in values:
        if len(i) > cur_longest:
            cur_longest = len(i)
    return(cur_longest)


def second(element):
    return element[1]


def data_header(widths):
    output_string = ""
    output_string += '{:<{width0}}|{:<{width1}}|{:<{width2}}|{:<{width3}}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift', width0=widths[0], width1=widths[1], width2=widths[2], width3=widths[3])
    output_string += '\n' + '-' * (sum(widths)+3)
    return output_string


def data_print(info, widths):
    output_string = ""
    output_string += '{:<{width0}}|{:<{width1}}|{:<{width2}}|{:<{width3}}'.format(info[0], info[1], info[2], info[3], width0=widths[0], width1=widths[1], width2=widths[2], width3=widths[3])
    return output_string


def report(donors):
    output = []
    for i in donors:
        output.append(stats(i))
    output.sort(reverse=True, key=second)
    column_widths = []
    for x in range(len(output)-1):
        column_widths.append(longest(([str(item[x]) for item in output])))
    print(data_header(column_widths))
    for j in output:
        print(data_print(j, column_widths))



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
            report(donors)

if __name__ == '__main__':
    main()
