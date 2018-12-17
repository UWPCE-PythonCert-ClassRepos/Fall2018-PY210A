import os
import sys
from donor_models import Donor
from donor_models import Donor_Collection

main_prompt = "\n".join(
    ("Welcome to the mailroom!", "Choose an action:",
     "1 - Input", "2 - Output", "e - Exit", ">>>  "))


err_prompt = "\n".join(
    ("Please provide a valid option!",
     "1 - Input", "2 - Output", "e - Exit", ">>>  "))


donor_in_prompt = "\n".join(
    ("Welcome to donor database!", "Choose an action:",
     "1 - Add a donation",  "e - Exit to main panel", ">>>  "))


donor_out_prompt = "\n".join(
    ("Welcome to donor database!", "Choose an action:",
     "1 - Generate thank you letter for last donation",  "2 - Generate donation report", "3 - Save all thank you to disk", "e - Exit to main panel", ">>>  "))

donorDb = Donor_Collection()
last_donor = ""
last_donation_amount = 0
OUT_PATH = "thank_you_letters"

def input_handler():
    while True:
        response = input(donor_in_prompt)
        # create a dictionary for user's selections
        switch_donorDB_dict = {
            "1": pre_add_donor,
            "e": main,
            "E": main,
        }
        # choose a function depending on response, if the choice is not in dict, catch exception
        try:
            switch_donorDB_dict[response]()
        except KeyError:
            print("Please provide a valid option!")


#Convert user input name to proper type
def convert_to_std(name):
    # Exception if the name is invalid
    lst = name.split(" ")
    lst2 = [x.capitalize() for x in lst]
    return ' '.join(lst2)


def add_donor(donor_name, donation_amount):
    donorDb.add_donor(donor_name,donation_amount)
    global last_donation_amount, last_donor
    last_donor =  donor_name
    last_donation_amount = donation_amount


def pre_add_donor():
    while True:
        response = input("Please provide donor's full name!\n")
        checked_response = input("You are creating a donation for " + convert_to_std(response) +"\n" + "Enter \"y\" or \"n\" >>>")
        
        if checked_response == "y" or checked_response == "Y":
            # need check validty for float() function
            try:
                amount = input("Please enter a number to indicate the donation amount:\n")
                if float(amount) < 0:
                    print("Please enter a positive number")
                    continue
                add_donor(convert_to_std(response), float(amount))
                input_handler()
            except ValueError:
                print("Please enter a number!")
        else:
            continue


def prepare_to_run():
    if not os.path.isdir(OUT_PATH):
        os.mkdir(OUT_PATH)


def pre_save_letter():
    prepare_to_run()
    donorDb.save_all("thank_you_letters")


def send_last():
    if last_donor == "":
        print("There is no latest donation made!")
    else:
        print(donorDb.send_single(last_donor, last_donation_amount))


def generate_report():
    print(donorDb.report_generator())


def out_handler():
    while True:
        response = input(donor_out_prompt)
        # create a dictionary for user's selections
        switch_donorDB_dict = {
            "1": send_last,
            "2": generate_report,
            "3": pre_save_letter,
            "e": main,
            "E": main,
        }
        # choose a function depending on response, if the choice is not in dict, catch exception
        try:
            switch_donorDB_dict[response]()
        except KeyError:
            print("Please provide a valid option!")


def kill_program():
    quit()


def main():
    err_in = 0
    while True:
        if err_in == 0:
            response = input(main_prompt)
        else:
            response = input(err_prompt)
            err_in = 0
        # create a dictionary for user's selections
        switch_main_dict = {
            "1": input_handler,
            "2": out_handler,
            "e": kill_program,
            "E": kill_program,
        }
        # choose a function depending on response, if the choice is not in dict, catch exception
        try:
            switch_main_dict[response]()
        except KeyError:
            err_in = 1
            


if __name__ == "__main__":
    main()