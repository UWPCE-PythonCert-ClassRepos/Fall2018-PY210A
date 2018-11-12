#Data structure that holds a 
#list of donors an a history 
#list of the amounts 
#Populate at least five donors with between 1 and 3 donations each


import sys  # imports go at the top of the file

title_db = ("Donor Name", "Total given", "Num Gifts", "Average Gift")

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

prompt = "\n".join(("Welcome to Mailroom",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit ",
          ">>> "))

def send_thankyou():
	print("")
	   #  input_name = input("Please the Full Name")
    # fruits.append(new_fruit)

def create_report():
	print("{:20}\t|  {:s}\t|  {:s}\t|  {:s} ".format(*title_db))
	print("".join(["-"] * 60))
	for x in range (len(donor_db) - 1):
		print("{:20}".format(donor_db[x][0]))

	    
	# for x in range(5):
    #print('{:20}'.format(donor_db[0][0]))
#print('{:20}{:10}{:10}{:14}'.format(listTuple[1][0], listTuple[1][1], listTuple[1][2], listTuple[1][3],))
#print('{:20}{:10}{:10}{:14}'.format(listTuple[2][0], listTuple[2][1], listTuple[2][2], listTuple[2][3],))


	# for x in range (len(donor_db)):
	# 	if x == len(donor_db)-1:
	# 		form_string += "{:d}"
	# 	else:
	# 		form_string += " {:d}, "
  

def quit_program():
    print("Good Bye!")
    sys.exit()  # exit the interactive script

def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            send_ThankYou()
        elif response == "2":
            create_report()
        elif response == "3":
            quit_program()
        else:
            print("Not a valid option!")


if __name__ == '__main__':
	main()


"Send a Thank You"
"Create a Report"
"Quit"