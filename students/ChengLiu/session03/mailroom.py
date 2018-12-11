#!/usr/bin/env python3

"""
PY210A-Session03
Cheng Liu
Mailroom Part 1
"""

donors = [("Fred Jones", [100, 200, 300]), ("Amy Shume", [2000, 1000, 3000])]

def thank_you():
    print("Do the Tahnk_you function here")

def report():
    print("Do the report function here")

def main():
    print("Welcome to Mailroom!")
	answer = ""
	while answer != "q":
		print("Please select from the following:")
		print("Quit: 'q'" 
			"\nThank you: 't'"
			"\nReport: 'r'"
			 )
		answer = input("=> ")
		answer = answer.strip() # in case entering the space at the beginning
		answer = answer[0:1].lower() # in case only enter key, no values
		if answer == "t":
			thank_you()
		elif answer == "r":
			report()


if __name__ == "__main__":
	main()


