import sys

#Create a list of data of donors
donors = [("Fred Jones", [100, 20]), 
("Amy Shumer", [2000, 99]),
("Yu Wang",[5]),
("Jin Liu",[520]),
("Doron Levy",[3]) ]

#prompt structure learned from the mailroom tutorial
prompt = "\n".join(("Welcome to the mailroom!", 
	      "please choose from the following:", 
	      "t - Thank You Email", 
	      "c - Create a Report",
	      "q - Quit", 
	      ">>>  "))

def get_length_a():
	ls = []
	ls2 = []
	for donor in donors:
		i = len(str(sum(donor[1])))
		ls.append(i)
		ls2.append(len(donor[0]))
		width1 = max(ls2) + 8
		width2 = max(ls) + 8
	return width1, width2

def in_list(donor_name):
	for names in donors:
		if donor_name in names:
			return True
	return False

def update_donor(response_donor, response_amount):
	index = 0
	for names in donors:
		if response_donor in names:
			index = donors.index(names)
			break
	lst = list(donors[index])
	lst[1].append(int(response_amount))
	#massages sent in the email
	print('{:20}'.format("Dear " + response_donor + ":"))
	print("Thank you for donating " + response_amount + "!")
	print()

def thank_you():
	while True:
		response_donor = input("Please provide the donar's full name or type list to see the full history: \n")
		if response_donor == "list":
			print(donors)
		else:
			response_amount = input("Please provide the donation amount: \n")
			if in_list(response_donor):
				update_donor(response_donor, response_amount)
				break
			else:
				donors.append((response_donor,[int(response_amount)]))
				print('{:20}'.format("Dear " + response_donor + ":"))
				print("Thank you for donating " + response_amount + "!")
				print()
				break


def creat_a_report():
	new_donors = sorted(donors,key=lambda x: sum(x[1]))
	width1,width2 = get_length_a()
	print("{:{width1}}{}{:^{width2}}{}{:^10}{}{:^{width2}}".format("Donor Name", "|", "Total Given", "|", "Num Gifts", "|", "Average Gift", width1 = width1, width2 = width2))	
	print("-" * (width1 + width2*2 + 15))
	for donor in new_donors:
		print('{:{width1}}'.format(donor[0], width1 = width1), end="")
		print('{:1}'.format('$'),end="")
		print('{:{width2}}'.format(sum(donor[1]), width2=width2), end="")
		print('{:>12}'.format(len(donor[1])),end=" ")
		print('{:1}'.format('$'),end="")
		print('{:>{width2}.2f}'.format(round(sum(donor[1])/len(donor[1]),2), width2 = width2), end="")

		print()


def exit_program():
	print("Thank you for using")
	sys.exit()

def main():
	while True:
		response = input(prompt)
		if response == "t":
			thank_you()
		elif response == "c":
			creat_a_report()
		elif response == "q":
			exit_program()
		else:
			print("Not a valid option!")

if __name__ == "__main__":
	main()