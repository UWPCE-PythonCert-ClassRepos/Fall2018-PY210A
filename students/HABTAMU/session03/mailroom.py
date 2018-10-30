#!/usr/bin/env python3

import sys

donors_info = [("Bill Gates", 3500, 5500, 7500), ("Paul Alen", 3000, 3700, 3900), ("Jeff Benzo", 3300, 5000, 7500)]
t = tuple(donors_info[:])
# donors_name = donors_info[i][0]
# for i in range(len(t)):
#     print(donors_info[i][0])
        
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

def send_thankyou():

    name = input("What is donors name? Type list if you don't know the name \n:> ").strip()
    
    if name == 'list':
        list()
    
    # elif name == 


    # elif name in donors_info[0]:
    #     print("No donor name exist with that name:")
    else:
        return 0
        # new_donor = input.print("No in donor list, do you want to add?: y/N")

def exit_program():
    print("Bye!")
    sys.exit() # exit the interactive script


def main():
    while True:
        response = input(prompt)

        if response == "1":
            send_thankyou()

        elif response == "2":
            create_report()

        elif response == "3":
            exit_program()
            
        else:
            print("No a valid option")

if __name__ == '__main__':
    main()
