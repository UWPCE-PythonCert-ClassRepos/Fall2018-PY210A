#!/usr/bin python3
"""
Mailroom part 2
"""
import tempfile
import pathlib

donors = {"Fred Jones": [100, 200, 300], 
    "Amy Shumer": [1000, 2000, 3000],
    "Bill Gates": [200, 400, 750, 400],
    "John Smith Jr.": [200, 400, 9050.20, 30],
    "Jeff Bezos": [200, 225.50, 10000, 30]}

file_dir = pathlib.Path(tempfile.gettempdir())

def thank_you():
    name_entered = "list"
    while name_entered == "list":
        name_entered = input("Enter a donor name => ")
        if name_entered.lower().strip() == "list":
            print_donors()
            continue
        if name_entered[:1].lower() == "e":
            return None
    
    name_entered = name_entered.strip()    
    donor_amount = get_donation_amount(name_entered)
    if donor_amount is None:
        return None
    add_donation(name_entered, donor_amount)

    print(get_thank_you(name_entered, donor_amount), end='\n\n')

def add_donation(name, amount):
    donors.setdefault(name, []).append(amount)

def get_donation_amount(name):
    response = input(f"How much did {name} donate? ")
    if response[:1].lower() == 'e':
        return None
    return float(response)

def print_donors():
    for donor in donors:
        print(f"- {donor}")

def get_thank_you(name, amount):
    return f"""Dear {name},

    Thank you for your ${amount:.2f} donation to our charity.
    
    Sincerely,
    CEO Bob Newsenbaumerson"""

def make_report():
    print()
    print("{:<20}|{:^13}|{:^11}|{:>13}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 60)
    
    for k, v in sorted(donors.items(), key=report_sort, reverse=True):
        print("{:<21}${:>11.2f}{:>12}  ${:>12.2f}".format(k,sum(v),len(v), sum(v) / len(v)))

def report_sort(item):
    return sum(item[1])

def all_thank_yous():
    for donor in donors:
        file_path = file_dir /  f"{donor.replace(' ', '_')}.txt"
        with open(file_path, 'w') as f:
            f.write(get_thank_you(donor, donors[donor][-1]))
    print(f"Files generated at: {file_dir}")

def quit():
    return "quit"

def unknown_command():
    return None

def main():
    commands = {
        "1": {"command": thank_you, "text": "Send Thank You to single donor"},
        "2": {"command": make_report, "text": "Create a Report"},
        "3": {"command": all_thank_yous, "text": "Send letters to all donors"},
        "4": {"command": quit, "text": "Quit"}}

    print("*** Welcome to Mailroom! ***")
    interface_text = ["Please select from the following:"]
    interface_text.extend([f"{key}. {value['text']}" for key, value in commands.items()])
    interface_text = "\n".join(interface_text)
    while True:
        print()
        print(interface_text)
        answer = input(" => ")[0:1].lower().strip()
        if commands.get(answer, {"command": unknown_command})["command"]() == 'quit':
            break

if __name__ == "__main__":
    main()