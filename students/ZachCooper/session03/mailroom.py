#!/usr/bin/env python3



# Create donors
donors = [("Fred Jones", [100, 200, 300]),
		("Amy Schumer", [2000, 4000, 1000]),
        ("Bill Gates", [5000, 10000, 30000]),
        ("Chris Fermstad", [300, 1000, 750]),
        ("Ryan Simmers", [100000, 50000, 100])]

# Command Script that gives user options
def main():
	print("Welcome to MailRoom!")
    answer = ""
    while answer != "q":
        print("Please select from the following")
        print("Quit: 'q', \n"
            "Thank You: 't'\n"
            "Report: 'r'")
        answer = input("=>")
        answer = answer.strip()
        answer = answer[:1].lower()
        if answer == 't':
            thank_you(answer)
        elif answer == 'r':
            create_report()
        elif answer == 'q':
            print("Goodbye!!!")
            break
        else:
            print("Invalid choice. Please select 'T', 'Q', or 'R' ")

# Function that sends new_donor or returning donor who donates more a Thank You email
def send_email(name, amount):
    """This function will compose the thank you email"""
    print("Thank you, {}, for your donation of ${}!"
    "Your contributions are always welcome and look forward to future donations.".format(name, amount))

# Thank you function either prints current donors, calls function for current donor to re-donate, or prompts new donor function
def thank_you(answer):
    if answer == 't':
		name = input("Please enter a donors full name or type 'list' to view list of donor names?")
        if name == 'list':
            print(donors)
        elif name == donors:
            """This part will not launch returning_donor function. Not mater which name is enterer,
            even if it is in the donors list, it launches new_donor()"""
            returning_donor(name)
        elif name != donors:
            new_donor(name)

# Function for returning donor to donate again. Sends thank you email
def returning_donor(name):
    if name in donors:
        print("How much would you like to donate?:")
        amount = int(input(":"))
        donors.append(amount)
        send_email(name, amount)

# Creates new donar and prompts donation. Sends thank you email
def new_donor(name):
    print("A new donor! We are adding {} to list of donors".format(name))
    print("How much would you like to donate?:")
    amount = int(input(":"))
    add_new_donor = (name, [amount])
    donors.append(add_new_donor)
    send_email(name, amount)

# Creates report of current donors, total given, total donations, avg donation
def create_report():
    """Created a reporting function"""
    print("{:<15}{:5}{:5}{}".format("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"))
    print("{:-<70}".format(""))
    """How can I get the below seq to line up with headers???"""
    for i in range(len(donors)):
        print("{} ${} {} ${}".format(donors[i][0], sum(donors[i][1]), len(donors[i][1]),
            sum(donors[i][1]) // len(donors[i][1])))




if __name__ == "__main__":
    main()
    















