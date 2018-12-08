import mailroom04


def exiting():
    """Return exiting, which breaks out of loops"""
    return "exiting"


def main(prompt, options_dict):
    """Get input from user and call appropirate function"""
    print("Welcome to the mailroom!")
    while True:
        answer = input(prompt)
        if options_dict[answer]() == "exiting":
            break
        else:
            print("Please make a valid selection")


"""Establish dispatch dictionaries and prompts"""
options_dict = {"1": thank_you_input, "2": make_report, "3": exiting}

thank_you_dispatch = {"1": make_list, "2": make_donation_input, "3": exiting}

thank_you_prompt = """Please select one of the following:
          (1): Display list of donors
          (2): Make a donation
          (3): Back to main menu
          """

prompt = """Please enter one of the following:
            (1): Send a thank you note
            (2): Create a report
            (3): Quit
            """

if __name__ == '__main__':
    main(prompt, options_dict)

