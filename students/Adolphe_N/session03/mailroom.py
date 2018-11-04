#!/usr/bin/env python3
import sys
"""
mailroom assignment
"""

donors = [("Fred Jones", [100, 200, 300]),("Bill Gates", [5000, 3000]), ("Denzel Washington", [4000,7000]),
          ("Lewis Hamilton", [2000, 4000, 1000])]
donor_names = ['Fred Jones', 'Bill Gates', 'Denzel Washington', 'Lewis Hamilton']

prompt = '\n'.join(('Please select from below options:',
        "1. - Send a thank you note",
        "2. -Create a report",
        "3. -Quit the program",
        ">>>"))
def thank_you():
    name = input('What is the donor full name: ')
    name.strip()
    name.lower()
    if name in donor_names:
        print("Thank you {} for your donation".format(name))
    else:
        print('the name entered is not found in the donors list')
        ask = input('Do you want add the name to list? y or n: ')
        if ask == 'y':
            donor_names.append(name)
            print (donor_names)
        else:
            prompt 
            
def make_report():
    
    print("put report here")
def quit():
    sys.exit()

def main():
    while True:
        response = input(prompt)
        response.strip()
        if response == "1":
            thank_you()    
        elif response == '2':
            make_report()
        elif response == '3':
            quit()
        elif response == 'list':
            print(donor_names)
            prompt
#         elif response == donor_names:
#             print(don)
            
        else:
            print('Your selection is invalid!')
        
            
    
    
    
    print("Welcome to Mailroom!")
#     answer = ""
#     while  answer != "q":
#         print("Please select from the following")
#         print("Quit: 'q', \n"
#               "Thank you: 't'\n"
#               "Report: 'r'")
#         answer = input(" => ")
#         answer = answer.strip()
#         answer = answer[0:1].lower()
#         if answer == 't':
#             thank_you()
#         elif answer == 'r':
#             make_report()




if __name__ == "__main__":
    main()