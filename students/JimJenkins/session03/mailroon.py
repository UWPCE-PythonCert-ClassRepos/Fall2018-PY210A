
key_list = ['name', 'donation_amount']
donor_list = ['John Doe', 'Tom Tinker', 'David Goliath', 'Billy Joel', 'Mona Liza', 'Dire Straits', 'Alice Cooper', 'Steve Perry', 'Sting', 'Jim Jenkins']
donation_amount_list = [1000, 2000, 3000, 400, 500, 60, 7000, 8000, 900, 9000]

donations = [{key_list[0]:a, key_list[1]:b}
              for a, b in zip(donor_list, donation_amount_list)]

def send_thankyou():
    print(menu['1'])
    action = str(input('Enter a full name: '))
    if action == 'list':
        donor_list()
    elif action == 'Jim Jenkins':
        print('individual')
    return

def create_report():
    print(menu['2'])
    return

def quit():
    print(menu['3'])
    return

def donor_list():
    donor_list = [{key_list[0]: a} for a, b in zip(donor_list, donation_amount_list)]

    print("{:<15} | {:^12} ".format('Name:', 'Donation Amount:'))
    for donor in donations:
        print('{:<15}   ${:>9,.2f}'.format(donor['name'], donor['donation_amount']))


#menu options
menu = {}
menu['1'] = 'Send a thank you'
menu['2'] = 'Create a Report'
menu['3'] = 'Quit'

#menu
print('MAILROOM')
print(' ')

#menu logic
while True:
    options = menu.keys()

    for entry in options:
        print(entry, menu[entry])
    print(' ')
    selection = input("Please select an option number: ")
    print(' ')
    if selection == '1' :
        send_thankyou()
        break
    elif selection == '2':
        create_report()
        break
    elif selection == '3':
        quit()
        break
    else:
        print('Unknown option selected')
        print(' ')


key_list = ['name', 'donation_amount']
donor_list = ['John Doe', 'Tom Tinker', 'David Goliath', 'Billy Joel', 'Mona Liza', 'Dire Straits', 'Alice Cooper', 'Steve Perry', 'Sting', 'Jim Jenkins']
donation_amount_list = [1000, 2000, 3000, 400, 500, 60, 7000, 8000, 900, 9000]

donations = [{key_list[0]:a, key_list[1]:b}
              for a, b in zip(donor_list, donation_amount_list)]

print ("{:<15} | {:^12} ".format('Name:', 'Donation Amount:'))
for donor in donations:
    print('{:<15}   ${:>9,.2f}'.format(donor['name'], donor['donation_amount']))

