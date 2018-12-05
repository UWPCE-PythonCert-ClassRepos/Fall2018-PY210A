#!/usr/local/bin/python3
from datetime import datetime
import csv

# Establish some data to work with in a dictionary
donors = {"Timothy Tander": [100, 200, 300],
          "Tara Towers": [200, 400, 600],
          "Charlie Day": [700, 100, 2000],
          "Sandra Connors": [1800, 2300, 7000],
          "Betsy Hammond": [500, 190, 212, 55]}

prompt = ("Please enter one of the following: \n 1: Send a thank you note\n 2: Create a report\n 3: Quit\n")


def thank_you():
    now = datetime.now().strftime("%Y-%m-%d")
    full_name = input("Please enter a name (list for full list of donors): ")
    while True:
        if full_name == 'list':
            for i in donors:
                print(i)
            break
        elif full_name in donors:
            donation = float(input('How much would you like to donate? '))
            donors[full_name].append(donation)
        else:
            donation = float(input('How much would you like to donate? '))
            donors[full_name] = [donation]

        with open(f"{full_name}_{now}.txt", 'w') as f:
            f.write(f"Dear {full_name},\n\n")
            f.write(f"\tThank you so much for your generous donation of {donation}!\n\n")
            f.write("\t\t\t\t\tSincerely, Donor Team")

        print("\nThank you! A thank you letter has been generated and will be emailed to you shortly!\n")
        break


def make_report():
    print("{:^20}|{:^20}|{:^20}|{:^20}".format("Donor Name", "No. Donations", "Avg. Donation", "Total Donations"))
    for k, v in donors.items():
        print("{:<20}|{:>20}|{:>20}|{:>20}".format(k, len(v),
                                                   "$" + str(round(sum(v)/len(v), 2)),
                                                   "$" + str(sum(v))))

    # Create csv file for report data
    now = datetime.now().strftime("%Y-%m-%d")
    with open(f"report_{now}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Donor Name", "No. Donations", "Avg Donation", "Total Donations"])

        # Zip lists of values to pass to writerow
        names = [k for k in donors.keys()]
        no_dons = [len(v) for v in donors.values()]
        avg_don = [round(sum(v)/len(v), 2) for v in donors.values()]
        total_dons = [sum(v) for v in donors.values()]
        zipped = zip(names, no_dons, avg_don, total_dons)

        for i in zipped:
            writer.writerow(i)


# Do not name this function quit, it leads to stack overflow...
def exiting():
    print("Quitting program!")
    quit()


def main(prompt, options_dict):
    print('Welcome to the mailroom')
    while True:
        # Run appropriate function based on user input, or ask for valid input
        answer = input(prompt)
        if answer in options_dict:
            options_dict[answer]()
        else:
            print("Please make a valid selection")


# Dispatch dictionary to handle possible user input
options_dict = {"1": thank_you, "2": make_report, "3": exiting}


if __name__ == '__main__':
    main(prompt, options_dict)
