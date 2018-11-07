#Establish some data to work with in a dictionary
donors = {"Timothy Tander": [100, 200, 300],
           "Tara Towers": [200, 400, 600],
           "Charlie Day": [700, 100, 2000],
           "Sandra Connors": [1800, 2300, 7000],
           "Betsy Hammond": [500, 190, 212, 55]}

donors["Timothy Tander"].append(800)

def thank_you(full_name, donation):
   print("\n Dear {}, thank you so much for your generous donation of ${}!\n".format(full_name, donation))

def make_report():
    total = [round(sum(i)) for i in donors.values()]
    num_donations = [len(i) for i in donors.values()]
    avg_donations = [round(sum(i)/len(i),2) for i in donors.values()]
    zipped = list(zip(list(donors.keys()), total, num_donations, avg_donations))
    print("Donor Name | Total Given | Num Donations | Average Donation")
    zipped = [list(i) for i in zipped]
    for i in zipped:
        print(i)
# TypeError: unsupported format string passed to list.__format__]
# I can't seem to figure out why I'm getting this error when the below is
# uncommented

#    for i in range(len(zipped)):
#        print('{:>20s}{:<12d}{:<10f}{:>12f}'.format(zipped[i][0],zipped[i][1], zipped[i],[2], zipped[i][3]))

def main():
    print('Welcome to the mailroom')
    answer = ' '
    while answer[0].lower() != 'q':
        print("Please select one of the following options:")
        print("Quit: 'q' \n"
              "Thank you: 't' \n"
              "Report: 'r' \n")
        answer = input(' ')
        answer = answer[:1].lower().strip()
        if answer == 't':
            full_name = input('Please enter a full name (list for donors) ')
            if full_name == 'list':
                for i in donors.keys():
                    print(i)
            elif full_name in donors.keys():
                donation = float(input('How much would you like to donate? '))
                donors[full_name].append(donation)
                thank_you(full_name, donation)
            elif full_name not in donors.keys():
                donation = float(input('How much would you like to donate? '))
                donors[full_name] = [donation]
                thank_you(full_name, donation)
        elif answer == 'r':
            make_report()

if __name__ == '__main__':
    main()



