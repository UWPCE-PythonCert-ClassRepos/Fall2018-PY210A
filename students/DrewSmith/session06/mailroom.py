#!/usr/bin python3
"""
Mailroom part 4
"""
import tempfile
import pathlib
from collections import namedtuple

donation = namedtuple("donations", "name amounts")
donors = {"fred_jones": donation("Fred Jones", [100, 200, 300]),
    "amy_shumer": donation("Amy Shumer", [1000, 2000, 3000]),
    "bill_gates": donation("Bill Gates", [200, 400, 750, 400]),
    "john_smith_jr": donation("John Smith Jr.", [200, 400, 9050.20, 30]),
    "jeff_bezos": donation("Jeff Bezos", [200, 225.50, 10000, 30])
    }

file_dir = pathlib.Path(tempfile.gettempdir())

def thank_you():   
    name_entered = user_get_donor()  
    if name_entered is None:
        return None
    donor_amount = user_get_donation_amount(name_entered)
    if donor_amount is None:
        return None
    add_donation(name_entered, donor_amount)

    print(get_thank_you_text(name_entered, donor_amount), end='\n\n')


def translate_donor_name(name):
    """Translate donor name into key value"""
    return name.replace(" ", "_").replace(".", "").lower()


def add_donation(name, amount):
    """Add dononation to a donor entry"""
    donors.setdefault(translate_donor_name(name), donation(name, [])).amounts.append(amount)


def print_donors():
    """Print full list of donor names"""
    print_list((f"- {donor.name}" for donor in donors.values()))


def get_thank_you_text(name, amount):
    return f"""
Dear {name},
Thank you for your ${amount:.2f} donation to our charity.
    
Sincerely,
CEO Bob Newsenbaumerson"""


def print_list(iterable):
    for item in iterable:
        print(item)


def get_report():
    rows = ["{:<20}|{:^13}|{:^11}|{:>13}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")]
    rows.append("-" * 60)
    for v in sorted(donors.values(), key=report_sort, reverse=True):
        rows.append("{:<21}${:>11.2f}{:>12}  ${:>12.2f}".format(v.name,sum(v.amounts),len(v.amounts), sum(v.amounts) / len(v.amounts)))
    return rows


def report_sort(item):
    return sum(item[1])


def make_report():
    print()
    print_list(get_report())


def get_thank_you_file_path(donor):
    return file_dir /  f"{donor}.txt"


def all_thank_yous_to_files():
    for donor, donation in donors.items():
        with open(get_thank_you_file_path(donor), 'w') as f:
            f.write(get_thank_you_text(donation.name, donation.amounts[-1]))
    print(f"Files generated at: {file_dir}")


def exit_app():
    return "quit"

def unknown_command():
    return None

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
        answer = safe_input("Enter a donor name => ")
        if answer.strip().lower() == "list":
            print_donors()
        elif answer.strip().lower() == "e":
            return None
        else:
            return answer

def user_get_donation_amount(name):
    return safe_input_float(f"How much did {name} donate? ", 'e')


def user_main():
    commands = {
        "1": {"command": thank_you, "text": "Send Thank You to single donor"},
        "2": {"command": make_report, "text": "Create a Report"},
        "3": {"command": all_thank_yous_to_files, "text": "Send letters to all donors"},
        "Q": {"command": exit_app, "text": "Quit"}}

    print("*** Welcome to Mailroom! ***")
    interface_text = ["Please select from the following:"]
    interface_text.extend([f"{key}. {value['text']}" for key, value in commands.items()])
    while True:
        print()
        print_list(interface_text)
        answer = safe_input(" => ")[0:1].upper().strip()
        if commands.get(answer, {"command": unknown_command})["command"]() == 'quit':
            break

if __name__ == "__main__":
    user_main()