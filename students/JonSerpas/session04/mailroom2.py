#this is the primary function for the program
def mailroom():
    while True:
        # data structure of donors
        donors = {'Bill Gates': [1000, 2000, 3000], 'Rick James': [5000, 5000, 6000, 3000],
        'James Brown': [4000, 10000, 9000, 12000], 'Prince': [5500, 6500, 7000, 12000],
        'Cat Williams': [2000, 3000, 1000]}

        #this is the thank you email function
        def thank_you(donors):
            #this function generates a list of donors and their amounts
            def list(donors):
                for i in donors:
                    print(i)
            #there we determine if the users choice is in the db
            mailto = input("To whom would you like to send a thank you letter? \nType 'List' for a list of donors: ")
            if mailto == "List":
                list(donors)
            elif mailto in donors:
                print("Dear {}, \n Thank you for your generous donation of ${}.".format(mailto, str(donors[mailto][-1:]).strip('[]')))
            else:
                #now we add the new donor to the db and send an email
                print("{} not found in donors.".format(mailto))
                user_choice = input("Would you like to add this name to the donor list? y/n ").lower()
                if user_choice == "y":
                    donation_amount = int(input("How much was the donation?: $"))
                    donors[mailto] = donation_amount
                    print("Dear {}, \n Thank you for your generous donation of ${}.".format(mailto, donation_amount))
                else:
                    pass

            # this sends out a list to all donors
        def everyone(donors):
            for mailto in donors:
                with open(f'{mailto}.txt' , 'w') as file:
                    file.write("Dear {}, \n Thank you for your generous donation of ${}.".format(mailto, str(donors[mailto][-1:]).strip('[]')))
                    file.close()

            # this creates a report for a donors and what they have spent
        def create_report(donors):
            print("-" * len(donors))
            for i in donors:
                print('{:<20}{:<10}{:<5}{:<20}'.format(i, sum(donors[i]), len(donors[i]), sum(donors[i]) / len(donors)))
            print("-" * len(donors) , '\n')

            # this exits the program
        def goodbye(*args, **kwargs):
            print("Goodbye")
            exit()

# this function will serve as the menu and prompt the user for choices

        def menu():
            functions_list = {"1":thank_you,
                              "2":create_report,
                              "3":everyone,
                              "4":goodbye}

            print('[1] Send a Thank You \n[2] Create a Report \n[3] Send Letters to everyone \n[4] Quit')
            user_choice = input('Enter the number for the required option: ')
            functions_list[user_choice](donors)



        menu()


if __name__ == '__main__':
    mailroom()



