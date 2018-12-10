# Lesson 09 Assignment: Mailroom - Object Oriented
# Command Line Interface - main program flow and user interaction functions

from donor_models import Donor, DonorCollection
import os

# Make a DonorCollection object
charity = DonorCollection()


def check_menu_answer(answer):
    """
    Validates menu selection. Gets first character of user input. Checks for empty string or invalid letter/number.
    :param answer: capitalized user input
    :param menu_dict: main menu dictionary
    :return: if valid, calls corresponding function from dictionary, else returns error message
    """
    try:
        answer = answer[0]
        menu_options.get(answer)()

    except (IndexError, TypeError):
        print("That is not a valid selection. Please try again.")


def display_menu():
    """
    Displays menu options until user selects "Q" for quit
    :param menu_dict: main menu dictionary
    """
    answer = ""

    while answer != "Q":
        print("\nMAIN MENU"
              "\nType T to Send a Thank You to a Single Donor"
              "\nType A to Send Thank You Letters to All Donors"
              "\nType R to Create a Report"
              "\nType Q to Quit")

        answer = input("\nPlease enter a command: ").capitalize()

        check_menu_answer(answer)

def list_donors():
    """
    Lists existing donors.
    :return: printed list of donors
    """
    print("\nPREVIOUS DONORS")
    existing = charity.list_donors()
    for donor in existing:
        print(donor)
    print()


def check_name(name):
    """
    Validates donor name. Checks if name is blank or is a number.
    :param name: user input
    :return: Returns True for valid name, False for invalid name, or None if user wants to exit.
    """
    if name == "" or name.isdigit():
        return False
    elif name == "E":
        return
    elif name == "L":
        list_donors()
        return False
    else:
        return True


def check_donation(donation):
    """
    Verifies donation amount.
    :param donation: integer or float
    :return: Returns True if donation is valid, False if it is invalid, or None if user wants to exit.
    """
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

def thank_one():
    """
    Sends a thank you to a single donor.
    """
    while True:
        name = input("Please enter the donor's full name, type L to see a list of previous donors, "
                     "or type E to exit to main menu: ").title()

        test = check_name(name)

        if test:
            break
        elif test is None:
            return

    while True:
        donation = input("Please enter the donation amount or type E to exit: ")

        test = check_donation(donation)

        if test:
            donation = round(float(donation), 2)
            break
        elif test is None:
            return

    donor = charity.find_donor(name)
    donor.add_donation(donation)

    print()
    print(donor.thank_you_letter())







def check_directory(directory):
    """
    Checks file directory
    """
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


def save_letters(directory):
    """
    Creates and saves thank you letters for all donors.
    :param directory: path to save files
    """
    for donor in charity.donors_dict.values():
        path = os.path.join(directory, donor.name + " " + datetime.datetime.now().strftime("%m-%d-%Y") + ".txt")

        with open(path, "w") as outfile:
            name = donor.name
            donation = donor.donations[-1]
            letter = thank_you_letter(name, donation)
            outfile.write(letter)


def thank_all():
    """
    Sends thank you letters to all donors for their most recent donation.
    """
    while True:
        directory = input("Enter the path where you want the letters saved (Example: C:\\Users\\dtingg\\) "
                          "or press Enter to use the default directory: ").strip()

        test = check_directory(directory)

        if test:
            break

    save_letters(directory)
    print("Thank you letters have been generated for all donors.")


def print_report():
    """
    Prints a report.
    """
    headers = ["Donor Name", "Total Given", "Times Donated", "Average Gift"]
    print()
    print("{:17} | {:>20} | {:>15} | {:>19}".format(headers[0], headers[1], headers[2], headers[3]))
    print("-" * 80)

    donor_data = charity.create_report()

    for row in donor_data:
        print("{:17} |  ${:>18,.2f} | {:>15} |  ${:>17,.2f}".format(row[0], row[1], row[2], row[3]))


def exit_program():
    """
    Exits the program.
    """
    print("Goodbye!")


# Make a dictionary for menu options
menu_options = {"T": thank_one, "R": print_report, "A": thank_all, "Q": exit_program}


def main():
    print("Welcome to Dianna's Mailroom Program!")

    display_menu()


if __name__ == "__main__":
    main()
