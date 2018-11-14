#Lesson03
#Mailroom Part 1 Project
#
#!/usr/bin/env python3

#define variables - create donor list

donor1 = ("Anna Fang", [23.53, 5000])
donor2 = ("Tom Natsworthy", [99, 783, 3])
donor3 = ("Hester Shaw", [5, 92, 101.23])
donor4 = ("Katherine Valentine", [1000, 2000, 3000])
donor5 = ("Grike", [1])
donors = [donor1] + [donor2] + [donor3] + [donor4] + [donor5]

#define function
def mainmenu():
    """This is the main menu of the mailroom project part 1"""
    print(" \n\nHello and Welcome to MAILROOM!\n",
           "{:-<30}".format("-"))
    choice = ""
    while choice != "q":
        print("\n\nWould you like to (S)end a Thank You, Run a (R)eport or (Q)uit?")
        choice = input(": ")
        #removes any spaces in the choice
        choice = choice.strip()
        #takes the first letter of the choice and makes it lower case
        choice = choice[0:1].lower()
        if choice == "s":
            thankyou()
        elif choice == "r":
            report()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
             print("\nPlease enter 'S', 'R' or 'Q'")

def thankyou():
    """This is the thank you menu that routes to the listuser or donor_update function"""
    print("Please enter the name of the donor or type 'list' to list current donors.")
    name = input(": ")
    if name == "list":
        list_users()
    else:
        donor_update(name)

def list_users():
    """A simple function that lists donor names"""
    print("\nDonors\n", "{:-<60}".format(""))
    for i in donors:
        print(i[0])

def compose_email(name, amount):
    """This function will compose the thank you email"""
    print("\n\nEMAIL SENT:\n'Thank you, {}, for your generous contribution of ${}! We will be sure to ask you for more money again soon.'\n\n".format(name, amount))
    print("Sincerely,\nDonations, Inc.\n\n")

def donor_update(name):
    """This function will update the donor list with a new donor or a new amount given by a current donor"""
#    l = len(donors)
#    print(name)
#variable if a name is found in the search. default is 0 / False
    found = 0
#for loop to search for a donor name in the database. If found it will flag the found variable as True and add the addtional amount
    for i in range(len(donors)):
        if name in donors[i]:
            print("How much $$ did they donate this time?: ")
            amount = int(input(": "))
            donors[i][1].append(amount)
            found = True
            break
        else:
            continue
    if not found:
        #if the name was not found then add the name to the list of donors as well as the amount donated
        print("\n\nA new donor!! Adding {} to the list of donors".format(name))
        print("\n\nHow much $$ did they donate?: ")
        amount = float(input(": "))
        add_donor = (name, [amount])
        donors.append(add_donor)
#after adding the information to the database, send to function to send the thank you
    compose_email(name, amount)

def report():
    """This is the reporting function"""
    #
    sorted_list = sorted(donors, key=sort_key, reverse = True)
    print("\n", "\n", "{:<25}{:5}{:5}{}".format("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"))
    print("{:-<80}".format(""))
<<<<<<< HEAD
    for i in range(len(sorted_list)):
        print("{:<26} ${:<11.2f} {:<11} ${:.2f}".format(sorted_list[i][0], sum(sorted_list[i][1]), len(sorted_list[i][1]), sum(sorted_list[i][1]) / len(sorted_list[i][1])))
=======
    for i in range(len(donors)):
        print("{:<26} ${:<11.2f} {:<11} ${:.2f}".format(donors[i][0], sum(donors[i][1]), len(donors[i][1]), sum(donors[i][1]) / len(donors[i][1])))
>>>>>>> 2847109129e4b6fde58ceb6042412c146c5adc3e
    # for i in range(len(donors)):
    #     print("{} ${}".format(donors[i][0], sum(donors[i][1])))

def sort_key(donor):
    """function key used for donation totals"""
    tot = sum(donor[1])
    return tot

#for testing
if __name__=="__main__":
    mainmenu()
    #listusers()
