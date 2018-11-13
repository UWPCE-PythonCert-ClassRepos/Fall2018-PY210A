#!/usr/bin/env python3
import sys

"""
mailroom assignment
"""

donors = [("Jeff Bezos", [1000.56, 2000, 3000]),("Bill Gates", [5000.50, 3000]), ("Denzel Washington", [4000,7000]),
          ("Lewis Hamilton", [2000, 4000, 1000])]


def main_menu():
    '''
    Prints out the menu where user has option to select from
    '''
    select_option = input('''
      Choose an action:

      't' - Send a Thank You
      'r' - Create a Report
      'q' - Quit

      > ''')
    return select_option.strip()


def display_donors():
    print('Donors list:\n')
    for donor_name in donors:
        donors_names = donor_name[0]
        print(donors_names)

def find_donor(name):
    for donor in donors:
        if name.strip().lower() == donor[0].lower():
            return donor
    return None

def thank_you():
    '''
    display a thank you message to the donor 
    '''
    while True:
        name = input('Enter the donor full name or "list" to see all donors or "quit" to exit: ').strip()
        if name == 'list':
            display_donors()
        elif name == 'q':
            return
        else:
            break
    # Here the user input the donation amount and store to donors list object
    while True:
        amount_donation = input('Enter a donation amount (or "q" to exit)> ').strip()
        if amount_donation == 'q':
            return
        else:
             amount = float(amount_donation)
        break
    donor = find_donor(name)
  
    
    if donor is None:
        donor = (name, [])
        donors.append(donor)
    donor[1].append(amount)
    print(donors)
    print("Thank you {} for your generous donation of $ {:.2f}".format(donor[0], sum (donor[1])))
         
def sort_key(item):
    return item[1]

def make_report():
    
    donor_summary = []
    
    for donation in donors:
        #print(donation[0])
        Donor_name = donation[0] 
        Total_donated = sum(donation[1])
        Num_Gifts = len(donation[1])
        Average_gift = Total_donated/Num_Gifts
        donor_summary.append([Donor_name, Total_donated, Num_Gifts, Average_gift])
    
    #sort the report by total donated
    donor_summary.sort(key = sort_key)
    
    #the header of the report
    Column_Header = ['Donor_name', 'Total_donated', 'Num_Gifts', 'Average_gift']
    
    #print out report in a nice format
    print('\n {:25s} | {:12s} | {:10s} | {:<12s}'.format(Column_Header[0],Column_Header[1], Column_Header[2], Column_Header[3]))
    print(70 * '-')
    
    for item in donor_summary:
        print ('{:25}  {:12.2f}  {:10d}  {:>12.2f}'.format(item[0],item[1], item[2], item[3]))
    

def quit():
    '''
    this terminates the program
    '''
    sys.exit()
 
if __name__ == "__main__":

    unit_testing = True
    while unit_testing:
        selection = main_menu()
        if selection == "t":
            thank_you()    
        elif selection == 'r':
            make_report()
        elif selection == 'q':
            unit_testing = False
        else:
            print('the selection is invalid')    
            
     