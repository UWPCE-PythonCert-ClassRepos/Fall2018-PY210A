import tempfile
from donor_models import Donor, DonorCollection, get_donordb
from textwrap import dedent

donor_collection = DonorCollection(get_donordb())


def safe_input(message=""):
    try:
        get_input = input ("=> " + message)
    except KeyboardInterrupt:
        return None
    except EOFError:
        return None
    return get_input

def send_thank_you():
    print("Enter a name:")
    name = safe_input()

    if donor_collection.find_donor(name) is True:
        print(donor_collection.thank_you(name))
    else:
        print("Add a donation amount for {}:".format(name))
        donation_amt = int(input())
        new_donor = Donor(name, [donation_amt])
        donor_collection.add_donor(new_donor)

        print(donor_collection.thank_you(name))


def print_donor_report():
    print(donor_collection.make_report())


def save_letters_to_disk():
    donor_collection.send_all_donors()


def main():
    selection_dict = {"1": send_thank_you,
                      "2": print_donor_report,
                      "3": save_letters_to_disk,
                      "4": quit}

    while True:
        selection = main_menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")


def main_menu_selection():
    action = input(dedent('''
      Choose an action:
      1 - Send a Thank You
      2 - Create a Report
      3 - Send letters to everyone
      4 - Quit
      > '''))
    return action.strip()


if __name__ == "__main__":
    selection_dict = {"1": send_thank_you,
                      "2": print_donor_report,
                      "3": save_letters_to_disk,
                      "4": quit}

    while True:
        selection = main_menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")