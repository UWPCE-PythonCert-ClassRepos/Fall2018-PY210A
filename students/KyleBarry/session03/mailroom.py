donors = [('Fred', [100, 200, 300]),
           ("Tara", [200, 400, 600])]

donors[0][1].append(800)

list_of_donors = [d[0] for d in donors]

def thank_you(full_name, donation):
   print("Dear {}, thank you so much for your generous donation of {} dollars!".format(full_name, donation))

def make_report():
    pass

def main():
    print('Welcome to the mailroom')
    answer = ' '
    while answer[0].lower() != 'q':
        print("Please select one of the following options:")
        print("Quit: q, \n"
              "Thank you: 't' \n"
              "Report: 'r' \n")
        answer = input(' ')
        answer = answer[:1].lower().strip()
        if answer == 't':
            full_name = input('Please enter a full name: ')
            if full_name == 'list':
                for i in list_of_donors:
                    print(i)
            elif full_name in list_of_donors:
                donation = int(input('How much would you like to donate? '))
                for i in donors:
                    if i[0] == full_name:
                        i[1].append(donation)
                        thank_you(full_name, donation)
            elif full_name not in list_of_donors:
                donors.append((full_name,0))
        elif answer == 'r':
            make_report()

if __name__ == '__main__':
    main()




