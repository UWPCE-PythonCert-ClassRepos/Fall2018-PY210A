# Lesson 05 Assignment: Mailroom, Part 3

# Import module
import datetime

# Make a dictionary that holds donor names and a history of the amounts they donated
donors = {"Jimmy Fallon": [500.00, 700.00], "Taylor Swift": [1000.00], "Dan White": [200.00, 300.00, 400.00],
          "Trevor Noah": [750.00, 850.00], "Elon Musk": [3000.00], "Selena Gomez": [100.00, 150.00, 200.00]}


# Display menu options
def display_menu(menu_dict):
    answer = ""

    # Until the user selects Q for quit
    while answer != "Q":
        print("\nMAIN MENU"
              "\nType T to Send a Thank You to a Single Donor"
              "\nType R to Create a Report"
              "\nType A to Send Thank You Letters to All Donors"
              "\nType Q to Quit")

        answer = input("\nPlease enter a command: ")

        # Get first character of user input and capitalize it
        try:
            answer = answer[0].capitalize()

        # If user enters an empty string
        except IndexError:
            pass

        # Get menu selection from dictionary
        try:
            menu_dict.get(answer)()

        # If user types an invalid letter or number
        except TypeError:
            print("That is not a valid selection. Please try again.")


# Send a Thank You to a Single Donor
def thank_one():
    name = ""

    while name == "" or name == "L" or name.isdigit():
        name = input("Please enter the donor's full name, "
                     "type L to see a list of previous donors, "
                     "or type E to exit to main menu: ").title()

        # Exit if the user types "E"
        if name == "E":
            return

        # If user types "L" show them a list of the donor names
        elif name == "L":
            for x in donors:
                print(x)

    donation = 0

    while donation <= 0:
        donation = input("Please enter the donation amount or type E to exit: ")

        if donation == "":
            donation = 0

        elif donation[0].capitalize() == "E":
            return

        try:
            donation = float(donation)
        except ValueError:
            donation = 0

    # Set default for new_donor to True
    new_donor = True

    # If donor exists in dictionary, they are not new
    for x in donors:
        if x == name:
            donors[x].append(donation)
            new_donor = False
            break

    # Add donor to dictionary if they are new
    if new_donor:
        donors[name] = [donation]

    # Print thank you e-mail
    print()
    personal_dict = make_personal_dict(name, donation)
    print(thank_you(personal_dict))


# Make a personal dictionary for one person's donation
def make_personal_dict(name, donation):
    d = {"date": datetime.datetime.now().strftime("%B %d, %Y"), "name": name, "donation": "{:,.2f}".format(donation)}
    return d


# Print thank you e-mail using personal dictionary
def thank_you(personal_dict):
    letter = "{date}\n\nDear {name}:\n\nThank you so much for the generous donation of ${donation}.\n" \
             "We will use the money to provide tiny cars to clowns in need.\n\nBest regards,\n" \
             "Dianna Tingg\nTiny Clown Car Foundation".format(**personal_dict)
    return letter


# Send Thank You Letters to All Donors for their most recent donation
def thank_all():
    path = input("Enter the path where you want the letters saved (Example: C:\\Users\\dtingg\\)"
                 "or press Enter to use the default directory: ")

    for person in donors:
        with open(path + person + " " + datetime.datetime.now().strftime("%m-%d-%Y")+".txt", "w+") as outfile:
            donor_dict = make_personal_dict(person, donors[person][-1])
            donor_letter = thank_you(donor_dict)
            outfile.write(donor_letter)

    print("Thank you letters have been generated for all donors.")


# Create sort key to return total given
def sort_key(person):
    return person[1]


# Create a report
def create_report():

    # donor_summary = []
    #
    # for person in donors:
    #     name = person
    #     total_given = sum(donors[person])
    #     times_donated = len(donors[person])
    #     avg_gift = total_given / times_donated
    #     donor_summary.append([name, total_given, times_donated, avg_gift])

    # Using list comprehension: name, total given, times donated, average gift
    donor_summary = [[person, sum(donors[person]), len(donors[person]), sum(donors[person]) / len(donors[person])] for
                     person in donors]

    # Sort Donor Summary by total given in descending order
    donor_summary = sorted(donor_summary, key=sort_key, reverse=True)

    headers = ["Donor Name", "Total Given", "Times Donated", "Average Gift"]

    print()
    print("{:17} | {:>20} | {:>15} | {:>19}".format(headers[0], headers[1], headers[2], headers[3]))
    print("-"*80)

    for x in donor_summary:
        print("{:17} |  ${:>18,.2f} | {:>15} |  ${:>17,.2f}".format(x[0], x[1], x[2], x[3]))


# Exit program
def exit_program():
    print("Goodbye!")
    return


# Make a dictionary for menu options
menu_options = {"T": thank_one, "R": create_report, "A": thank_all, "Q": exit_program}


# Main function
def main():
    print("Welcome to Dianna's Mailroom Program!")

    display_menu(menu_options)


if __name__ == "__main__":
    main()
