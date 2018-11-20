#!/usr/bin/env python3

from textwrap import dedent  

# Create donors
donors ={ 'fred jones': ("Fred Jones", [100, 200, 300]),
        'amy schumer': ("Amy Schumer", [2000, 4000, 1000]),
        'bill gates': ("Bill Gates", [5000, 10000, 30000]),
        'chris fermstad' : ("Chris Fermstad", [300, 1000, 750]),
        'ryan simmers': ("Ryan Simmers", [100000, 50000, 100]),
        }

        
# Returns a list of current donors
def print_donors():
    print("Donor List:\n")
    for donor in donors:
        print(donors[0])

# See if donor is in the list. Use case sensitive compare
def find_donor(name):
    for donor in donor_db:
        
        if name.strip().lower() == donor[0].lower():
            return donor
    return None


# Command Script that gives user options
def main():
    print("Welcome to MailRoom!\n")
    """Main menu selection for"""
    action = input(dedent('''
         Choose an action:

         't' - Send a Thank You
         'r' - Create a Report
         'q' - Quit

         > '''))
    return action.strip()
    


def gen_letter(donor):
    return dedent('''
          Dear {}

          Thank you for your very kind donation of ${:.2f}.
          It will be put to very good use.

                         Sincerely,
                            -The Team
          '''.format(donors[0], donors[1][-1]))



# Function that sends new_donor or returning donor who donates more a Thank You email
def send_email(name, amount):
    """This function will compose the thank you email"""
    print("Thank you, {}, for your donation of ${}!"
    "Your contributions are always welcome and look forward to future donations.".format(name, amount))


# Thank you function either prints current donors, calls function for current donor to re-donate, or prompts new donor function
def thank_you(answer):
    while True:
        if answer == 't':
          name = input("Please enter a donors full name, 'list' to view list of donor names, or 'menu' to return to menu options?").strip()
            if name == 'list':
                print(donors)
            elif name == 'menu':
                return 
            elif name in donors:
                """This part will not launch returning_donor function. Not mater which name is enterer,
                even if it is in the donors list, it launches new_donor()"""
                returning_donor(name)
            elif name != donors:
                new_donor(name)

        else:
           print("You seem to not want to donate....but you")

def new_donations():
    while True:
        amount = input("How much would you like to donate at this time? Every bit helps!! Or you can select 'list' or 'menu'")
        if amount == 'menu':
            return
        elif amount == 'list':
            return print_donors()
        else:
            break
    donor = find_donor(name)
    if donor is None:
        new_donor

    # Append new donation
    donor[1].append(amount)
    # Print a thank you letter
    print(gen_letter(donor))

# Function for returning donor to donate again. Sends thank you email
def returning_donor():
    if name in donors:
        print("{}, Welcome back! How much would you like to donate?:".format(name))
        amount = int(input(":"))
        donors.append(amount)
        send_email(name, amount)

# Creates new donar and prompts donation. Sends thank you email
def new_donor():
    print("A new donor! We are adding {} to list of donors".format(name))
    print("How much would you like to donate?:")
    amount = int(input(":"))
    add_new_donor = (name, [amount])
    donors.append(add_new_donor)
    send_email(name, amount)

# Write a letter to file
def save_letters_to_file():
    for donor in donors.values():
        letter = gen_letter(donor) # Create variable to return letter function
        filename = donor[0].replace(" ", "_") + ".txt" # Convert empty spaces
        print("writting letter to:", donor[0]) # Name of letter indexed donor
        open(filename, 'w').write(letter) # 'w' writes to a blank new file

# Creates report of current donors, total given, total donations, avg donation
def donor_report():
    """I used your create_report function since I couldnt space mine properly"""
    """print("{:<15}{:5}{:5}{}".format("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"))
    print("{:-<70}".format(""))
    
    for i in range(len(donors)):
        print("{:25s} ${:11.2f} {:9s} ${:12.2f}".format((donors[i][0]), sum(donors[i][1]), len(donors[i][1]),
            sum(donors[i][1]) // len(donors[i][1])))"""


report_rows = []
    for (name, gifts) in donors:
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    
    report_rows.sort(key=sort_key)
    
    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 66)
    for row in report_rows:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))


if __name__ == "__main__":
running = True
    while running:
        selection = main_menu()
        if selection == "t":
            thank_you(answer)
        elif selection == "r":
            donor_report()
        elif selection == "q":
            running = False
        else:
            print("error: menu selection is invalid!")















