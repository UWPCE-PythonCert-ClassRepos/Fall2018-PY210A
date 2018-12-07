#Data structure that holds a 
#list of donors an a history 
#list of the amounts 
#Populate at least five donors with between 1 and 3 donations each

import sys  # imports go at the top of the file
import math # imports math to get sum and average
import os #
from pathlib import Path 


#Title from the table
title = ("Donor Name", "Total given", "Num Gifts", "Average Gift")

#database that hold person name and amount of donation
donor_dict = { "William Gates, III": [653772.32, 12.17],
             "Jeff Bezos": [877.33],
             "Paul Allen": [663.23, 43.87, 1.32],
             "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]
            }

#menu display from the selection
prompt = "\n".join(("Please choose from below options:",
          "1 - Send a Thank You to a single donor",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - Quit ",
          ">>> "))

DIR_NAME = "D_letter"

def send_thankyou():
    """
    This method is prompting enter to enter donor name, list from database, or return to menu

    params:  none - continue prompt user enter data from menu 
    It generate letter when user input amount of donation.
    """

    while True: 
    
        name = input(">Enter first and last name \n >"
            " or 'list' to see all donors name  \n >"
            " or 'menu' return to menu > ")
 
        if (name.lower() == 'list'):    
            print(chk_exist_donor())
        elif (name.lower() == 'menu'):
         	return
        else:
            dn = validate_name(name) #dn - donor name
            if dn is False:
                print ("Invalid Entry - Please re-enter first and last name")
            elif dn is True:
                ln = lookup_name(name) #ln - lookup donor
                amount = input ("\n Enter amount you want to donate > :")                
                money_input_ps = ck_dollar(amount)           
                if (money_input_ps == True):
                    amount_flt = float(amount)
                    add_donation(ln, name, amount_flt)
                    print(create_letter(name, amount_flt))
        break
       
def chk_exist_donor():    
    return [person_name for person_name in donor_dict]

def ck_dollar(amount):
    try:      
        amount_flt = round(float(amount), 2)
        if amount_flt <= 0.00:
            return False
        else:
            return True
    except ValueError:
        print("Input must be number, try again.  \n")
        return False

def add_donation(ln, name, amount):
    if (ln is None):
        donor_dict[name] = [amount]
    else:
        donor_dict[name].append(amount)

def validate_name(name):
    """
    This method is looking up user name

    params:  verify user input
    returns true or false for data entry
    """

    if (name == " " or name.isdigit()):
        return False

    str_name = name.rstrip()
    # #parse first and last name into string
    try:
        str_name = str_name.split(' ') 
        if (str_name[1] == ' '):    
            return False
    except IndexError:
        print ("Need to have first and last name within space between")
        return False

    #Validate user not to enter digit  
    print(str_name)
    for char in str_name:  
        for i in char:
            if (i.isnumeric() == True):
                print("Must be Character")
                return False
    return True


def lookup_name(name):
    """
    This method is looking up user name

    params:  take name of the user
    returns when user is found from the list or None
    """
    #Set to lower case for comparison

    for x in donor_dict.keys():
        if (x.split(' ')[0].lower() == name.split(' ')[0].lower() and 
            x.split(' ')[1].lower() == name.split(' ')[1].lower()):
            return x
    
    return None


def create_letter(name, amount):
    """
    This method is generating template letter to who addressing to 
    and the amount of donation

    params:  take user donor dictionary data
    returns whole string of the template letter
    """
    strLetter = """
            Dear {},
            Thank you  for your very kind donation of ${:.2f}
            It will be put to very good use.

                            Sincerely,
                            - The Team   
	        """.format(name, amount)
    return strLetter

def str_lname(rpt_donor):
    """
    This method is to return the last name from the string

    params:  string value of person last name
    returns whole string of the template letter
    """
    print (rpt_donor[0].split(' ')[1])
    return rpt_donor[0].split(' ')[1]


def create_report():

	# Create new list that contain name, amount, donate how many times, average
    
    report_donor = []

    for key, values in donor_dict.items():    
        name = "{}".format(key)
        total_cost = sum(values)
        n_time = len(values)
        average = total_cost/n_time
        report_donor.append([name, round(total_cost, 2), n_time, round(average, 2)])

    print (report_donor)
    #sort the report
    report = sorted(report_donor, key=str_lname, reverse=False)

    print("{:20}|  {:<10s}|  {:<10s}|  {:<10s} ".format(*title))
    print("".join(["-"] * 62))
    for x in range (len(report)):
    	print("{:20} $ {:10.2f} {:>12d} $ {:>12.2f}".format(*report[x]))
    
    return report_donor
 
def quit_program():
    print("Good Bye!")
    sys.exit()  # exit the interactive script

def ck_dir():
    if not os.path.isdir(DIR_NAME):
        os.mkdir(DIR_NAME)
        return False
    return True

def ss_letterall():
#     """
#     This method write letter to disk as txt file

#     params:  none
#     will check and generate directory
#     will write all txt file in the directory
#     """

	#writes each letter to disk as txt file
	#open ("./thankyou.txt", "w")
	# tempfile.gettempdir() 

    for key, values in donor_dict.items():    
        letter = create_letter(key, sum(values))
        filename = key + ".txt"
        ck_dir()    
        try:
            print(filename)
            filename = os.path.join(DIR_NAME, filename)
            open(filename, 'w').write(letter)
        except FileNotFoundError:
            print("couldn't open missing.txt")
        finally:
            pass


def default():
	print("Invalid options")

#switch to execute function
switch_fnc_dict = {
	                '1': send_thankyou,
	                '2': create_report,
	                '3': ss_letterall,
	                '4': quit_program,	                
                }


def main():
    """
    Start main program to prompt user select from main menu
    Continue prompt user until decide to quit program 
    from switch function dictionary
    returns None
    """
    print("Welcome to mailroom")
    
    while True:
        try:
            response = input(prompt) 
            switch_fnc_dict.get(response, default)()
        except NameError:
            print ("Must enter number from 1-4 from the menu")

if __name__ == '__main__':
	main()
