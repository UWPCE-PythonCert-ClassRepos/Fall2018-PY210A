import sys
import os


# Donor database(Dict Version)
# Full Name: [total amount, donation times]
donors_dict = {"Fred Jones": [500,2,250],
               "Amy Shumer": [600,3,200], 
               "Yu Wang": [6000,4,1500], 
               "Jin Liu": [3000,3,1000], 
               "Doron Levy": [900,9,100]}

#prompt structure learned from the mailroom tutorial
prompt = "\n".join(("Welcome to the mailroom!", 
	      "Choose an action", 
	      "1 - Send a Thank You to a single donor", 
	      "2 - Create a Report",
	      "3 - Send letters to all donors",
	      "4 - Quit", 
	      ">>>  "))

OUT_PATH = "thank_you_letters"

# method learned from lecture
def prepare_to_run():
	if not os.path.isdir(OUT_PATH):
		os.mkdir(OUT_PATH)

def send_single(donor, amount):
	letter = "Dear " + donor + ",\n" + "\tThank you for your very kind donation of $" + str(amount) 
	letter += ".\n" + "\tIt will be put to very good use.\n \t\tSincerely,\n \t\t-The Team"
	return letter

#Convert user input name to proper type
def convert_to_std(name):
	lst = name.split(" ")
	lst2 = [x.capitalize() for x in lst]
	return ' '.join(lst2)

def thank_you():
	while True:
		response = input("Provide donor's Full Name or Type \"list\" to get the full history\n")
		if response == "list":
			print(donors_dict)
		else:
			amount = input("Provide the donation amount: \n")
			response = convert_to_std(response)
			if response in donors_dict:
				donors_dict[response][0] += float(amount)
				donors_dict[response][1] += 1
				donors_dict[response][2] += donors_dict[response][0]/donors_dict[response][1]
				print(send_single(response, amount))
				break
			else:
			    donors_dict[response] = [float(amount),1,float(amount)]
			    print(send_single(response, amount))
			    break

def creat_a_report():
	# sort donor by total donation amount
	sorted_donors = sorted(donors_dict.items(), key=lambda x: x[1][0],reverse=True)
	sorted_name_length = sorted(donors_dict.items(), key=lambda x: len(x[0]),reverse=True)

	width = len(sorted_name_length[0][0]) + 8
	width2 = len(str(sorted_donors[0][1][0])) + 8
	
	print("{:{width}}{}{:^{width2}}{}{:^10}{}{:^{width2}}{}".format("Donor Name",
		"|"," Total Given","|"," Num Gifts","|"," Average Gift","|",width=width,width2=width2))
	print("-"*(width + width2*2 +15))

	[print("{:{width}}{:1}{:{width2}.2f}{:>11}{:>2}{:>{width2}.2f}".format(x[0],"$",
			x[1][0],x[1][1]," $",round(x[1][2],2),width=width,width2=width2))
	        for x in sorted_donors]

def save_to_disk(donor):
	donation = donors_dict[donor][0]
	ty_letter = send_single(donor,donation)
	filename = donor.replace(" ","_") + ".txt"
	print("writing to " + donor + "......\n")
	filename = os.path.join(OUT_PATH, filename)
	open(filename, "w").write(ty_letter)

def send_all():
	prepare_to_run()
	[save_to_disk(donor) for donor in donors_dict.keys()]


def exit_program():
	print("Thank you for using")
	sys.exit()

def main():
    while True:
        response = input(prompt)
        # create a dictionary for user's selections
        switch_main_dict = {"1": thank_you, 
                            "2": creat_a_report,
                            "3": send_all, 
                            "4": exit_program}
        # choose a function depending on response, if the choice is not in dict, catch exception
        try:
            switch_main_dict[response]()
        except KeyError:
            print("please provide a valid value\n")

if __name__ == "__main__":
	main()