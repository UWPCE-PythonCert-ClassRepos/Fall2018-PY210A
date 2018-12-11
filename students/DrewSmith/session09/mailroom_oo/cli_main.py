#!/usr/bin python3
"""
OOO Mailroom - Console Application
"""
import tempfile
import pathlib
from donor_models import Donor
from donor_models import DonorCollection

# Mailroom - Console User Interaction
file_dir = pathlib.Path(tempfile.gettempdir())
DONORS = DonorCollection()


def all_thank_yous_to_files():
    try:
        DONORS.generate_donor_files(file_dir)
    except IOError:
        print("An error occured writing donor files")
    else:
        print(f"Files generated at: {file_dir}")


def print_donors():
    """Print full list of donor names"""
    print_list(DONORS.list_donors())


def print_report():
    """Prints a console formatted report of all Donors"""
    rows = DONORS.generate_report()
    print("{:<20}|{:^13}|{:^11}|{:>13}".format(*rows[0]))
    print("-" * 60)
    for donor_row in rows[1:]:
        print("{:<21}${:>11.2f}{:>12}  ${:>12.2f}".format(*donor_row))


def print_list(iterable):
    """
    Prints each item in an iterable to the console

    :param iterable: an iterable of values to print
    """
    print()
    for item in iterable:
        print(item)


def safe_input(prompt):
    """
    Return user input or None if error occurs

    :param prompt: User prompt to display
    """
    while True:
        try:
            return input(prompt)
        except (EOFError, KeyboardInterrupt):
            print("Error! Please try again.")


def safe_input_float(prompt, escape_character):
    """
    Return user input converted to a float. None if user exits

    :param prompt: User prompt to display
    :param escape_character: single character used by the user to escape entering this command
    """
    while True:
        try:
            response = safe_input(prompt)
            if response[:1].lower().strip() == escape_character.lower():
                break
            return float(response)
        except OverflowError:
            print("That number is too big, pease try again")
        except ValueError:
            print("Not a valid dollar value. Please enter a decimal number.")


def user_get_donor():
    while True:
        answer = safe_input("Enter a donor name, 'list' for donor list, or 'e' to exit => ")
        if answer.strip().lower() == "list":
            print_donors()
        elif answer.strip().lower() == "e":
            return None
        else:
            if answer not in DONORS:
                verify = input(f"{answer} is not an existing donor, would you like to add a new donor (Y/N)?")
                if verify[:1].lower() == "n":
                    continue
            return answer


def user_get_donation_amount(name):
    while True:
        result = safe_input_float(f"How much did {name} donate? ", 'e')
        if result is None or result > 0:
            return result
        print("Invalid Donation amount. Please enter a dontation greater than 0.")


def thank_you():
    """User interaction for adding donor and/or donation"""
    name_entered = user_get_donor()
    if name_entered is None:
        return None
    donor_amount = user_get_donation_amount(name_entered)
    if donor_amount is None:
        return None
    donor = Donor(name_entered.strip(), [donor_amount])
    DONORS.add_donor(donor)
    print(donor.get_thank_you_text(), end='\n\n')


def exit_app():
    return "quit"


def unknown_command():
    return None


def user_main():
    commands = {
        "1": {"command": thank_you, "text": "Send Thank You to single donor"},
        "2": {"command": print_report, "text": "Create a Report"},
        "3": {"command": all_thank_yous_to_files, "text": "Send letters to all donors"},
        "Q": {"command": exit_app, "text": "Quit"}}

    print("*** Welcome to Mailroom! ***")
    interface_text = ["Please select from the following:"]
    interface_text.extend([f"[{key}] {value['text']}" for key, value in commands.items()])
    while True:
        print_list(interface_text)
        answer = safe_input(" => ")[:1].upper().strip()
        if commands.get(answer, {"command": unknown_command})["command"]() == 'quit':
            break


if __name__ == "__main__":
    user_main()
