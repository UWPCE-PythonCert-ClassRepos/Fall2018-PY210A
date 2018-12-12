#!/usr/bin/env python3
import sys
'''
Goal:
You work in the mail room at a local charity. Part of your job is to write \
incredibly boring, repetitive emails thanking your donors for their generous \
gifts. You are tired of doing this over and over again, so you’ve decided to \
let Python help you out of a jam and do your work for you.
'''
'''
It should have a data structure that holds a list of your donors and a history of \
the amounts they have donated. This structure should be populated at first with at \
least five donors, with between 1 and 3 donations each.
'''
DATA_STRUCTURE = [('Jeff Bezos', [200, 500, 1000]), \
                    ('Bill Gates', [1000]), \
                    ('Steve Jobs', [20, 50, 100])]
DATA_STRUCTURE_DICTS = [{'name': name, 'donation': donation} for name, donation in DATA_STRUCTURE]
# DATA_STRUCTURE_DICT = [ \
#                         {'name': 'Jeff Bezos', 'donation': [200, 500, 1000]},\
#                         {'name': 'Bill Gates', 'donation': [1000]},\
#                         {'name': 'Steve Jobs', 'donation': [20, 50, 100]}\
#                         ]

def thank_you(full_name='', donation_amount=int()):
    '''
    If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
        If the user types a name not in the list, add that name to the data structure and use it.
        If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
        Turn the amount into a number – it is OK at this point for the program to crash if \
        someone types a bogus amount.
    Once an amount has been given, add that amount to the donation history of the selected user.
    Finally, use string formatting to compose an email thanking the donor for their generous \
    donation. Print the email to the terminal and return to the original prompt.
    '''
    '''
    Collect, Format and Validate Full name
    '''
    #full_name = ''
    while not full_name:
        full_name_input = input('Please enter full name of the recipient: ').split()
        full_name = name_response_valid(full_name_input)
    '''
    Process Full Name
    '''
    ds_names = [name for name, donation in DATA_STRUCTURE]

    if full_name in ds_names:
        full_name_index = ds_names.index(full_name)
        print(f'Found {full_name} in data_structure')
        while not donation_amount:
            donation_amount = int(input('Please enter a donation amount: '))
        DATA_STRUCTURE[full_name_index][1].append(donation_amount)
        print(output_string().format(name=full_name, donation=donation_amount))
    else:
        while not donation_amount:
            donation_amount = int(input('Please enter a donation amount: '))
        DATA_STRUCTURE.append((full_name, [donation_amount]))
        print(output_string().format(name=full_name, donation=donation_amount))
    return output_string().format(name=full_name, donation=donation_amount)

def list_donors():
    '''
    If the user types ‘list’, show them a list of the donor names and re-prompt
    '''
    for entry in DATA_STRUCTURE:
        print(entry[0])
    return [entry[0] for entry in DATA_STRUCTURE]

def create_a_report():
    '''
    Creating a Report
    If the user (you) selected “Create a Report”, print a list of your donors, \
    sorted by total historical donation amount.
    '''
    print('Menu: Create a Report')
    top_row = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    format_header = '{:<30} | {:<15} | {:<10} | {:<15}\n'
    format_data = '{:<30} $ {:<15.2f}   {:<10} $ {:<15.2f}\n'
    format_string = format_header.format(*top_row)
    for i in sorted(DATA_STRUCTURE, key=key_index, reverse=True):
        name, total_given, num_gifts, avg_gift = i[0], sum(i[1]), len(i[1]), sum(i[1]) / len(i[1])
        format_string += format_data.format(name, total_given, num_gifts, avg_gift)
    print(format_string)
    return format_string

def key_index(item):
    '''Sort by total sum of donation amount'''
    return sum(item[1])

def send_letters():
    '''
    Try to use a dict and the .format() method to do the letter as one big \
    template rather than building up a big string in parts.
    In this version, add a function (and a menu item to invoke it), that goes \
    through all the donors in your donor data structure, generates a thank you \
    letter, and writes it to disk as a text file.
    '''
    for entry in DATA_STRUCTURE_DICTS:
        filename = '_'.join(entry.get('name').split())+'.txt'
        filenames = []
        with open(filename, 'w') as outfile:
            outfile.write(output_string().format(**entry))
            print(f'Writing: {filename}')
            filenames.append(filename)
    return filenames

def output_string():
    '''Output string for letters'''
    format_string = 'Dear {name},\n\nThank you for your generous donation of ' \
                    '${donation}. Please send us more money at your earliest ' \
                    'convenience.'
    return format_string

#Function to Process Menu Options
def menu(options_dict):
    '''
    The script should prompt the user (you) to choose from a menu of 3 actions: \
    “Send a Thank You”, “Create a Report” or “quit”)
    '''
    options = [option[0:2] for option in enumerate(options_dict.keys(), 1)]
    while True:
        print('Please select a number from the list of the following options: \n')
        for option in options:
            print(option)
        response = menu_response_valid(options)
        response_selection = options[response-1][1]
        options_dict[response_selection]()

#Main Menu
def main_menu():
    'Create Main Menu'
    program_options_dict = {'Send a Thank You': thank_you_menu, \
                            'Create a Report': create_a_report, \
                            'Send Letters to Everyone': send_letters, 'quit': sys.exit}
    menu(program_options_dict)

#Thank You Menu
def thank_you_menu():
    '''
    Sending a Thank You
    If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
    If the user types ‘list’, show them a list of the donor names and re-prompt
    '''
    program_options_ty = {'Send a Thank You': thank_you, \
                        'Action: List': list_donors, \
                        'quit': main_menu}
    menu(program_options_ty)

#Menu Option Validation
def menu_response_valid(options):
    'Validate Menu Options'
    try:
        response = int(input())
        assert response in [option[0] for option in options]
    except ValueError:
        print('Non-integer value entered. Please try again.')
    except AssertionError:
        print('This number does not exist in the list of options. Please try again.')
    else:
        return response
#Name Validation
def name_response_valid(full_name):
    'Validate and Return Name Input'
    full_name_cap = ''
    try:
        for name in full_name:
            assert name.isalpha()
            full_name_cap += f'{name.capitalize()} '
        full_name = full_name_cap.strip()
    except AssertionError:
        print('Invalid Name. Found non-alphabetic characters')
    else:
        return full_name

if __name__ == '__main__':
    main_menu()