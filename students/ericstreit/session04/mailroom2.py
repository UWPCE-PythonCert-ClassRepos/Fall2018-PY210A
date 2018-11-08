#Lesson03
#Mailroom Part 2 Project
#
#!/usr/bin/env python3

#define variables -
# create donor list
donors = {"Anna Fang": [23.53, 5000],
          "Tom Natsworthy": [99, 783, 3],
          "Hester Shaw": [5, 92, 101.23],
          "Hester Shaw": [5, 92, 101.23],
          "Katherine Valentine": [1000, 2000, 3000],
          "Grike": [1]}


# create menu dictionaries ARE BOTTOM OF THE PAGE


#define function

def thankyou():
    """This is the thank you menu that routes to the listuser or donor_update function"""
    print("Type 'send' to send a Thank you to a single donor, 'all' to send a thank you to all donors or 'list' to list current donors.")
    choice = input(": ")
    thankyou_dict.get(choice, badchoice)()

def badchoice():
    """ returns if valid menu input is not given"""
    print("I did not understand, please try again!")

def send_all():
    print("send thank you to all")

def send_one():
    name = input("Enter name of the donor to thank: ")
    money = float(input("Enter how much money they donated: "))
    if donor_find(name) != True:
        donor_add(name, money)
    else:
        donor_contribute(name, money)
    compose_email(name, money)

def donor_contribute(name, money):
    """ updates the db with the money the donor contributed """
    money_list = [money]
    money_update = donors.get(name) + money_list
    donors[name] = money_update

def list_donors():
    """A simple function that lists donor names"""
    print("\nDonors\n", "{:-<60}".format(""))
    for donor in donors:
        print(donor)

def compose_email(name, amount):
    """This function will compose the thank you email"""
    print("\n\nEMAIL SENT:\n'Thank you, {}, for your generous contribution of ${}! We will be sure to ask you for more money again soon.'\n\n".format(name, amount))
    print("Sincerely,\nDonations, Inc.\n\n")

def donor_find(name):
    """This function will search for a donor in the db"""
    if name in donors:
        return True

def donor_add(name, money):
    """This function adds a donor to the db"""
    donors[name] = [money]

def report():
    """This is the reporting function"""
    print("\n", "\n", "{:<25}{:5}{:5}{}".format("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"))
    print("{:-<80}".format(""))
    for donor in donors:
        print("{:<26} ${:<11.2f} {:<11} ${:.2f}".format(donor, sum(donors[donor]), len(donors[donor]), sum(donors[donor]) / len(donors[donor])))
    # for i in range(len(donors)):
    #     print("{} ${}".format(donors[i][0], sum(donors[i][1])))
def quit():
    """function to quit the program"""
    print("Goodbye!")

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
        menu_dict.get(choice, badchoice)()
        #print("\nPlease enter 'S', 'R' or 'Q'")
        #not needed but entering options other than s,  r or q will generate an error. I'm thinking the best way to handle this would be configuring a try exception that we learn later



#define dictionaries
#note must have this AFTER the mainmenu function otherwise generates an error since the functions havne't been made yet
menu_dict = {'s':thankyou,'r':report,'q':quit}
thankyou_dict = {'list':list_donors, 'all':send_all, 'send': send_one, 'q':quit}

#for testing
if __name__=="__main__":
    #report()
    mainmenu()
    #listusers()
