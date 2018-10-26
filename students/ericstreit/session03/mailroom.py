#Lesson03
#Mailroom Part 1 Project
#
#!/usr/bin/env python3

#define variables - the donor list
donor1 = ("Anna Fang", [23, 5000])
donor2 = ("Tom Natsworthy", [99, 783, 3])
donor3 = ("Hester Shaw", [5, 92, 101])
donor4 = ("Katherine Valentine", [1000, 2000, 3000])
donor5 = ("Grike", [1])
donors = [donor1] + [donor2] + [donor3] + [donor4] + [donor5]
l = len(donors)
print(donors)
print(l)
#define function
def mainmenu():
    """This is the main menu of the mailroom project part 1"""
    print(" \n\nHello and Welcome to MAILROOM!\n",
           "{:-<30}".format("-"))
    choice = ""
    while choice != "q":
        print("\n\nWould you like to (S)end a Thank You, Run a (R)eport or (Q)uit?")
        choice = input(":")
        choice = choice.strip()
        choice = choice[0:1].lower()
        if choice == "s":
            thankyou()
        elif choice == "r":
            report()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
             print("Please enter 'S', 'L' or 'Q'")

def thankyou():
    """This is the thank you menu"""
    name = input("Please enter the name of the donor or type 'list' to list current donors.")
    if name == "list":
        listusers()
    else:
        donorupdate(name)

def compose_email(name, amount):
    """This function will compose the thank you email"""
    print("\n\nEMAIL SENT:\n'Thank you, {}, for your generous contribution of ${}! We will be sure to ask you for more money again soon.'\n\n".format(name, amount))

def donorupdate(name):
    """This function will update the donor list with a new donor or a new amount given by a current donor"""
    l = len(donors)
    print(name)
    found = 0
    for i in range(len(donors)):
        if name in donors[i]:
            amount = int(input("How much $$ did they donate this time?: "))
            donors[i][1].append(amount)
            found = 1
            break
        else:
            continue
    if not found:
        print("\n\nAdding {} to the list of donors".format(name))
        amount = int(input("\n\nHow much $$ did they donate?: "))
        add_donor = (name, [amount])
        donors.append(add_donor)
        print(donors)

    compose_email(name, amount)




def report():
    """This is the reporting function"""
    print("\n", "\n", "{:<25}{:5}{:5}{}".format("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"))
    print("{:-<80}".format(""))
    for i in range(len(donors)):
        print("{} ${} {} {}".format(donors[i][0], sum(donors[i][1]), len(donors[i][1]), sum(donors[i][1]) // len(donors[i][1])))
    # for i in range(len(donors)):
    #     print("{} ${}".format(donors[i][0], sum(donors[i][1])))
def listusers():
    """A simple function that lists the donors"""
    print("{:-<60}\n", "Donors\n", "{:-<60}".format("",""))
    for i in donors:
        print(i[0])
# input
# choice = int(input("(1) Send a Thank You (2) Create a Report or (3) Quit - (1,2,or 3) : "))
# if choice == "1":
#     name = input("Please enter the full name (or 'list' to list current names): ")





#for testing
if __name__=="__main__":
    mainmenu()
    #listusers()
