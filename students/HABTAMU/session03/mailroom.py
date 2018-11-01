#!/usr/bin/env python3

import sys

donors_info = [("Bill Gates", 3500, 5500, 7500), 
               ("Paul Alen", 3000, 3700, 3900), 
               ("Jeff Benzo", 3300, 5000, 7500),
               ("Mark Zuckerberg", 33565.37, 465.37, 545.37, 7506),
               ("Warren Buffett", 3303.17, 334.17, 5080, 7500)
              ]
t = tuple(donors_info[:]) 
name = []       
prompt = "\n".join(("\n Please choose what you intended to know!:",
           " Choices are ?:",
           " 1 - Send a Thank you!",
           " 2 - Create a Report" ,
           " 3 - Exit",
           " >>> "))
def list():
    for i in range(len(t)):
        print(t[i][0])

def create_report():
    """
    Let's choose an options from the list
    Args:
        num: options(1 - 4) to choose
    Returns:
        A list of str contain from the doc
    """
    print("What if?!")

def send_thankyou(name):

    name = input("What is donors name? Type list if you don't know the name \n:> ").strip()
    # Carlos Slim
    if name == 'list':
        list()

    elif name in donors_info:
        print("Hello Mr {}!".format(name))
        donation_amount = input("Hi, Mr {} how much would you like to donat".format(name).strip().lower())
        donors_info.append(tuple(name,donation_amount))
        print(donors_info)
        
    elif name not in donors_info:
        add_donor = input("Donor's name {} is not in the donors list, Would you like to add to the donors list (y/n)?:".format(name).strip().capitalize())
        if  add_donor == "y":
            donors_info.append(tuple([name]))
            print(donors_info)
        elif add_donor == "n":
            print("No problem, Next time!")

    # else:
    #     return 0

    # elif name Carlos Slimin donors_info[0]:
    #     print("No donor name exist with that name:")
    # else:
    #     return 0
        # new_donor = input.print("No in donor list, do you want to add?: y/N")

def exit_program():
    print("Bye!")
    sys.exit() # exit the interactive script


def main():
    while True:
        response = input(prompt)

        if response == "1":
            send_thankyou(name)

        elif response == "2":
            create_report()

        elif response == "3":
            exit_program()
            
        else:
            print("No a valid option")

if __name__ == '__main__':
    main()
