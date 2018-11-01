#Establish some data to work with in a dictionary
from datetime import datetime

donors = {"Timothy Tander": [100, 200, 300],
           "Tara Towers": [200, 400, 600],
           "Charlie Day": [700, 100, 2000],
           "Sandra Connors": [1800, 2300, 7000],
           "Betsy Hammond": [500, 190, 212, 55]}

donors["Timothy Tander"].append(800)

def thank_you(full_name, donation):
    now = datetime.now().strftime("%Y-%m-%d")
    with open(f"{full_name}_{now}", 'w') as f:
        f.write(f"Dear {full_name}\n\n")
        f.write(f"\tThank you so much for your generous donation of {donation}!\n\n")
    
def make_report():

    print("{:^20}|{:^20}|{:^20}|{:^20}".format("Donor Name", "No. Donations","Avg. Donation", "Total Donations"))
    for k,v in donors.items():
        print("{:<20}|{:>20}|{:>20}|{:>20}".format(k, len(v), sum(v)/len(v),
                                                   sum(v)))
 
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



