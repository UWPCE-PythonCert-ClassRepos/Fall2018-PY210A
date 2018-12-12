#Data structure that holds a 
#list of donors an a history 
#list of the amounts 
#Populate at least five donors with between 1 and 3 donations each

import sys  # imports go at the top of the file
import math # imports math to get sum and average
import os #
from pathlib import Path 


#title from the table
title = ("Donor Name", "Total given", "Num Gifts", "Average Gift")

#database that hold person name and amount of donation
donor_db = [("William Gates, III", [653772.32, 12.17]),
             ("Jeff Bezos", [877.33]),
             ("Paul Allen", [663.23, 43.87, 1.32]),
             ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
             ]

#dictionary list for first name, last name, donation container
donor_dict = []

#menu display from the selection
prompt = "\n".join(("Please choose from below options:",
          "1 - Send a Thank You to a single donor",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - Quit ",
          ">>> "))

"""
    This method will send a thank you to a person
		If the user types list show them a list of the donor names and re-prompt.
		If the user types a name not in the list, add that name to the data structure and use it.
		If the user types a name in the list, use it.
    returns None
"""
DIR_NAME = "D_letter"

def send_thankyou():
    """
    This method is prompting enter to enter donor name, list from database, or return to menu

    params:  none - continue prompt user enter data from menu 
    It generate letter when user input amount of donation.
    """

    # print(donor_dict[1].keys())
    # print(donor_dict[1].values())

    for x in donor_dict:
        print("test", x)

    while True:       
        name = input("Enter first and last name \n > "
         	        " or 'list' to see all donors name > \n "
     	 	        " or 'menu' return to menu >")
        
        if (name == 'list'):
            print("x", donor_dict)
            for x in donor_dict:
                print (x["uid"],x["fname"], x["lname"])
            # print ("{uid} {fname} {lname}".format(**donor_dict))
        elif (name == 'menu'):
         	return
        else:
            fn_str = name.split(' ')[0]
            ln_str = name.split(' ')[1]
            dn = lookup(name)
            
            amount_str = input ("\n Enter amount you want to donate > :")
            amount_flt = float (amount_str)
            
            if dn is None:
                donor_dict.extend([{'uid': len(donor_dict) + 1, 
                                    'fname':  fn_str,
                                    'lname':  ln_str,
                                    'd_amount': [amount_flt],
                                    }])
                dn = donor_dict[-1]
            else:           
                dn["d_amount"].append(amount_flt)
        print(create_letter(dn))
        break
       
def lookup(name):
    """
    This method is looking up user name

    params:  take name of the user
    returns when user is found from the list or None if not found
    """

    #print ("test", name.split(' ')[0], name.split(' ')[1])
    fname_str = name.split(' ')[0].lower()
    lname_str = name.split(' ')[1].lower()

    for x in donor_dict:
        if (x['fname'].lower() == fname_str and x['lname'].lower() == lname_str):
            print("pass value ", x)
            return x

    # for x in range (len(donor_db)):
    #         if (donor_db[x][0].split()[:1][0].lower() == donor_dict['fname'].lower()
    #             and donor_db[x][0].split()[:2][1].lower() == donor_dict['lname'].lower()):
    #            print ("pass value ", x)
    #            return x
    return None


def create_letter(d_dict):
    """
    This method is generating template letter to who addressing to 
    and the amount of donation

    params:  take user donor dictionary data
    returns whole string of the template letter
    """

    strLetter = """
    	    Dear {} {},
            Thank you  for your very kind donation of ${:.2f}
             It will be put to very good use.

                            Sincerely,
                             - The Team
  		  """.format(d_dict["fname"], d_dict["lname"], d_dict["d_amount"][-1])
        #   """.format(**d_dict)
	
    return strLetter


def sec_letter(string):
    """
    This method is to return the last name from the string

    params:  string value of person name
    returns whole string of the template letter
    """
    return string[0].split()[:2][1]

def create_report():

	# Create new list that contain name, amount, donate how many times, average
    
    report_donor = []
    for d in donor_dict:
        name = d['fname'] + " " + d['lname']
        total_cost = sum(d['d_amount'])
        n_time = len(d['d_amount'])
        average = total_cost/n_time
        report_donor.append([name, total_cost, n_time, average])

    #sort the report
    report_donor.sort(key=sec_letter)

    #report_list.sort()
    print("{:20}|  {:<10s}|  {:<10s}|  {:<10s} ".format(*title))
    print("".join(["-"] * 62))
    for x in range (len(report_donor)):
    	print("{:20} $ {:10.2f} {:>12d} $ {:>12.2f}".format(*report_donor[x]))

 
def quit_program():
    print("Good Bye!")
    sys.exit()  # exit the interactive script

def ck_dir():
    if not os.path.isdir(DIR_NAME):
        os.mkdir(DIR_NAME)

def ss_letterall():
    """
    This method write letter to disk as txt file

    params:  none
    will check and generate directory
    will write all txt file in the directory
    """
	#writes each letter to disk as txt file
	#open ("./thankyou.txt", "w")
	# tempfile.gettempdir() 
    for d in donor_dict:
        # print(create_letter(d))
        letter = create_letter(d)
        filename = d['fname'] + "_"  + d['lname'] + ".txt"
        ck_dir()
        filename = os.path.join(DIR_NAME, filename)
        # print("Test ", filename)
        open(filename, 'w').write(letter)

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
    Continue prompt user until user quit program
    returns None
    """
    print("Welcome to mailroom")

    for x in range (len(donor_db)):
        donor_dict.extend([{'uid': x, 
                     "fname": donor_db[x][0].split()[:1][0],
                     'lname': donor_db[x][0].split()[:2][1],
                     'd_amount': donor_db[x][1]}, 
        ])

    while True:
        response = input(prompt) 
        switch_fnc_dict.get(response, default)()


if __name__ == '__main__':
	main()
