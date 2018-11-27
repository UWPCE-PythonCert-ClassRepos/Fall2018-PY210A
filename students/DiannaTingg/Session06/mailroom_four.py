# Lesson 06 Assignment: Mailroom, Part 4

# Import modules
import datetime
import os

# Make a dictionary that holds donor names and a history of the amounts they donated
donors = {"Jimmy Fallon": [500.00, 700.00], "Taylor Swift": [1000.00], "Dan White": [200.00, 300.00, 400.00],
          "Trevor Noah": [750.00, 850.00], "Elon Musk": [3000.00], "Selena Gomez": [100.00, 150.00, 200.00]}


# Validate menu selection
def check_menu_answer(answer, menu_dict):
    # Get first character of user input and capitalize it. Use that to get function from dictionary
    try:
        answer = answer[0]
        menu_dict.get(answer)()

    # If user enters an empty string or types an invalid letter/number
    except (IndexError, TypeError):
        print("That is not a valid selection. Please try again.")


# Display menu options
def display_menu(menu_dict):
    answer = ""

    # Until the user selects Q for quit
    while answer != "Q":
        print("\nMAIN MENU"
              "\nType T to Send a Thank You to a Single Donor"
              "\nType A to Send Thank You Letters to All Donors"
              "\nType R to Create a Report"
              "\nType Q to Quit")

        answer = input("\nPlease enter a command: ").capitalize()

        check_menu_answer(answer, menu_dict)


# List existing donors
def existing_donors():
    return [person for person in donors]


# Validate donor name
def check_name(name):
    if name == "" or name.isdigit():
        return False
    elif name == "E":
        return
    elif name == "L":
        print("\nPREVIOUS DONORS")
        existing = existing_donors()
        for x in existing:
            print(x)
        print()
        return False
    else:
        return True


# Verify donation amount
def check_donation(donation):
    if donation and donation[0].capitalize() == "E":
        return
    try:
        donation = round(float(donation), 2)

        if donation <= 0.00:
            return False
        else:
            return True
    except ValueError:
        return False


# Add donor/donation to dictionary
def add_donation(name, donation):
    # Set new donor as the default
    new_donor = True
    # If donor exists in dictionary, they are not new
    for x in donors:
        if x == name:
            donors[x].append(donation)
            new_donor = False
            break
    # Otherwise they are new, so add them to the dictionary
    if new_donor:
        donors[name] = [donation]


# Generate thank you letter
def thank_you_letter(name, donation):
    date = datetime.datetime.now().strftime("%B %d, %Y")
    letter = f"{date}\n\nDear {name}:\n\nThank you so much for the generous donation of ${donation:,.2f}.\n" \
             f"We will use the money to provide tiny cars to clowns in need.\n\n" \
             f"Best regards,\nDianna Tingg\nTiny Clown Car Foundation"
    return letter


# Send a Thank You to a Single Donor
def thank_one():
    while True:
        name = input("Please enter the donor's full name, type L to see a list of previous donors, "
                     "or type E to exit to main menu: ").title()

        test = check_name(name)

        if test:
            break
        elif test is None:
            return

    # Ask user for donation amount
    while True:
        donation = input("Please enter the donation amount or type E to exit: ")

        test = check_donation(donation)

        if test:
            donation = round(float(donation), 2)
            break
        elif test is None:
            return

    # Add name/donation to donor dictionary
    add_donation(name, donation)

    # Print thank you e-mail
    print()
    print(thank_you_letter(name, donation))


# Check directory
def check_directory(directory):
    if directory == "":
        return True
    else:
        if not os.path.isdir(directory):
            try:
                os.mkdir(directory)
                return True
            except (FileNotFoundError, PermissionError):
                print("Sorry, that directory doesn't exist.")
                return False


# Create/save thank you letters for all donors
def save_letters(directory):
    for person in donors:
        path = os.path.join(directory, person + " " + datetime.datetime.now().strftime("%m-%d-%Y") + ".txt")

        with open(path, "w") as outfile:
            name = person
            donation = donors[person][-1]
            letter = thank_you_letter(name, donation)
            outfile.write(letter)


# Send thank you letters to all donors for their most recent donation
def thank_all():
    while True:
        directory = input("Enter the path where you want the letters saved (Example: C:\\Users\\dtingg\\) "
                          "or press Enter to use the default directory: ").strip()

        test = check_directory(directory)

        if test:
            break

    save_letters(directory)
    print("Thank you letters have been generated for all donors.")


# Create sort key to return total given
def sort_key(person):
    return person[1]


# Create a report
def create_report():
    # Using comprehension: name, total given, times donated, average gift
    donor_summary = [[person, sum(donations), len(donations), sum(donations) / len(donations)]
                     for person, donations in donors.items()]

    # Sort Donor Summary by total given in descending order
    donor_summary = sorted(donor_summary, key=sort_key, reverse=True)

    return donor_summary


# Print the report
def print_report():
    headers = ["Donor Name", "Total Given", "Times Donated", "Average Gift"]
    print()
    print("{:17} | {:>20} | {:>15} | {:>19}".format(headers[0], headers[1], headers[2], headers[3]))
    print("-" * 80)

    donor_data = create_report()

    for x in donor_data:
        print("{:17} |  ${:>18,.2f} | {:>15} |  ${:>17,.2f}".format(x[0], x[1], x[2], x[3]))


# Exit program
def exit_program():
    print("Goodbye!")


# Make a dictionary for menu options
menu_options = {"T": thank_one, "R": print_report, "A": thank_all, "Q": exit_program}


# Main function
def main():
    print("Welcome to Dianna's Mailroom Program!")

    display_menu(menu_options)


if __name__ == "__main__":
    main()
