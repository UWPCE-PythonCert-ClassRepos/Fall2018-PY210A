# Lesson 03 Assignment: Mailroom, Part 1

# Make a list that holds donor names and a history of the amounts they donated
donors = [("Jimmy Fallon", [500.00, 700.00]), ("Taylor Swift", [1000.00]), ("Dan White", [200.00, 300.00, 400.00]),
          ("Trevor Noah", [750.00, 850.00]), ("Elon Musk", [3000.00]), ("Selena Gomez", [100.00, 150.00, 200.00])]


# Display menu options
def display_menu():

    # Set answer as an empty string
    answer = ""

    # Until the user selects Q for quit
    while answer != "Q":
        print("\nMAIN MENU")
        print("Type T to Send a Thank You")
        print("Type R to Create a Report")
        print("Type Q to Quit")

        answer = input("\nPlease enter a command: ")
        answer = answer[0].capitalize()

        if answer == "Q":
            break
        elif answer == "T":
            send_thank_you()
        elif answer == "R":
            create_report()
        else:
            print("That is not a valid option.  Please try again.")


# Send a Thank You
def send_thank_you():
    name = ""

    while name == "" or name == "E" or name == "L":
        name = input("Please enter the donor's full name, "
                     "type L to see a list of previous donors, "
                     "or type E to exit to main menu: ").title()

        # Exit if the user types "E"
        if name == "E":
            return

        # If user types "L" show them a list of the donor names
        elif name == "L":
            for x in donors:
                print(x[0])

    donation = 0

    while donation <= 0:
        donation = input("Please enter the donation amount or type E to exit: ")

        if donation[0].capitalize() == "E":
            return
        else:
            donation = float(donation)

    # Set default for new_donor to True
    new_donor = True

    for i in range(len(donors)):
        if donors[i][0] == name:
            donors[i][1].append(donation)
            new_donor = False
            break

    if new_donor:
        donors.append((name, [donation]))

    # Print thank you e-mail
    print_thank_you(name, donation)


# Print thank you e-mail
def print_thank_you(name, donation):
    print()
    print(f"Dear {name}:")
    print(f"\nThank you so much for the generous donation of ${donation:,.2f}.")
    print("We will use the money to provide tiny cars to clowns in need.")
    print("\nBest regards,")
    print("Dianna Tingg")
    print("Tiny Clown Car Foundation")


# Create a report
def create_report():

    donor_summary = []

    for person in donors:
        name = person[0]
        total_given = sum(person[1])
        times_donated = len(person[1])
        avg_gift = total_given / times_donated
        donor_summary.append([name, total_given, times_donated, avg_gift])

    # Sort Donor Summary by total given in descending order
    donor_summary.sort(key=lambda d: d[1], reverse=True)

    headers = ["Donor Name", "Total Given", "Times Donated", "Average Gift"]

    print()
    print("{:17} | {:>20} | {:>15} | {:>19}".format(headers[0], headers[1], headers[2], headers[3]))
    print("-"*80)

    for x in donor_summary:
        print("{:17} |  ${:>18,.2f} | {:>15} |  ${:>17,.2f}".format(x[0], x[1], x[2], x[3]))


# Main function
def main():
    print("Welcome to Dianna's Mailroom Program!")

    display_menu()

    print("Goodbye!")


if __name__ == "__main__":
    main()
