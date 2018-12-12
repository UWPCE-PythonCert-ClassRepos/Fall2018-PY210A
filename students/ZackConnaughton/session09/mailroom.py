"""
mailroom assignment
"""

class Donor():
    """
    Name, donations list, method for average, number and total of avg_of_donations
    """
    def __init__(self, name):
        self.name = name
        self.donation_list = []

    @property
    def donation_count(self):
        return len(self.donation_list)

    @property
    def donation_total(self):
        return sum(self.donation_list)

    @property
    def donation_average(self):
        return self.donation_total / self.donation_count

    def add_donation(self, donation):
        self.donation_list.append(donation)

    @property
    def latest_donation(self):
        return self.donation_list[-1]

class donor_list():


    def __init__(self):
        pass


donors_list = {'Jimmy John': [100, 200, 300],
               'Amy Shumer': [2000, 4000, 1000],
               'Parker Pony': [2000, 10000],
               'Cher': [900, 9000, 2000],
               'Legolass Mario': [4000, 50]
               }

def get_donors():
    """
    Takes a dictionary of donor information and returns a list of just the donor names
    """
    return list(donors_list.keys())


def print_donors():
    l = get_donors()
    output = 'List of current donors:\n'
    output += '\n'.join(l)
    output += '\n'
    return output


def enter_donation(response, money):
    if not response in donors_list:
        donors_list[response] = []
    donors_list[response].append(money)
    return None


def save_thank_you_letter(donor, letter_text):
    f = open('./thank_you_letters/' + donor + '.txt', 'w')
    f.write(letter_text)
    f.close()


def thank_you_letter(donor):
    """
    returns a formatted letter for the donor passed in.
    """
    output = "Dear {}\n\n".format(donor)
    output += "{:<10}Thank you for your kind donation of ${:.2f}.\n\n".format(" ", donors_list[donor][-1])
    output += "{:10}It will be put to very good use.\n\n".format(" ")
    output += "{fill:<15}Sincerely,\n{fill:<18}-Everyone here at Company Spot".format(fill=" ")
    #print(donors_list[donor][-1:])
    save_thank_you_letter(donor, output)
    return output


def thank_you():
    """
    prompts for a donor, and a donation, enters that donation for the donor.
    saves and prints a thank you letter
    """
    response = ""
    while response != 'Q':
        print("Enter the full name of donor:")
        print("(Type list to see a full list of donors)")
        response = input(' => ').title()
        if response == "List":
            print(print_donors())
        else:
            print("Enter the donation amount for " + response + ":")
            try:
                money = input(' => ')
                enter_donation(response, int(money))
                ty_letter = thank_you_letter(response)
                print(ty_letter)
            except ValueError:
                print("\nInvalid entry for donation\nDONATION NOT ENTERED\n")
            finally:
                response = "Q"


def stats(donor_info):
    """
    takes in donor information and returns the name of donor and the total,
    number and average of donations
    """
    name = donor_info
    total = 0
    for d in donors_list[donor_info]:
        total += (d)
    num_of_donations = len(donors_list[donor_info])
    avg_of_donations = '{:.2f}'.format(total / num_of_donations)
    return [name, total, num_of_donations, avg_of_donations]


def second(element):
    """
    takes in a list and returns the second element
    """
    return element[1]


def widths(values, min_width=12):
    output = []
    for x in range(len(values[0])):
        maximum_width = max(([len(str(item[x])) for item in values]))
        output.append(max(maximum_width, min_width))
    return output

def data_header(widths):
    """
    takes in column widths and outputs a data header for a donor report in a
    string format for printing
    """
    output_string = "\n"
    output_string += '{:<{width0}}|{:<{width1}}|{:^{width2}}|{:^{width3}}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift', width0=widths[0], width1=widths[1], width2=widths[2], width3=widths[3])
    output_string += '\n' + '-' * (sum(widths)+3)
    return output_string


def data_print(info, widths):
    """
    takes in donor information and widths and returns a string formatted for
    printing for a donor report.
    """
    output_string = ""
    output_string += '{:<{width0}} ${:>{width1}.2f} {:^{width2}} ${:>{width3}}'.format(info[0], info[1], info[2], info[3], width0=widths[0], width1=widths[1]-1, width2=widths[2], width3=widths[3]-1)
    return output_string


def report():
    """
    Prints a report to the terminal with the
    donors name, total given, number of donations and average donations.
    Returns a list of donor info.
    """
    output = []
    for i in donors_list:
        output.append(stats(i))
    output.sort(reverse=True, key=second)
    column_widths = []
    column_widths = widths(output)
    print(data_header(column_widths))
    for j in output:
        print(data_print(j, column_widths))
    print("")
    return output


def all_letters():
    try:
        for donor in donors_list:
            thank_you_letter(donor)
        print("Saved donor letters")
    except FileNotFoundError:
        print("\nFile Not Found\nLETTERS NOT SAVED\n")


def unknown():
    print("That is an invalid entry\n")
    return None


def quit_menu():
    return 'quit'


def main():
    print("Welcome to the Mailroom, you lucky duck!")
    print("")
    menu_dict = {'t': thank_you,
                 'r': report,
                 'l': all_letters,
                 'q': quit_menu
                 }
    response = ' '
    while True:
        print('Select from the following')
        print('Send single thank you: "t"\n'
              'Create a Report: "r"\n'
              'Send letters to all donors: "l"\n'
              'Quit: "q"')
        response = input(' => ')[:1].lower()
        if menu_dict.get(response, unknown)() == "quit":
            break


if __name__ == '__main__':
    main()
