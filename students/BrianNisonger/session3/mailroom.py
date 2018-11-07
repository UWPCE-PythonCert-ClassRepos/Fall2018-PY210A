#usr/bin/env python3

"""
mailroom assignment"
"""

donor_names=("Fred Jones","Amy Shumer")
donor_donations=([100,200,300],[400,400,400])

def thank_you(donor_names,donor_donations):
    full_name="list"
    while full_name == "list":
        full_name=input("Please enter full name==>")
        if full_name=="list":
            for name in (donor_names):
                print(name)
        else:
            flag=0
            for i in range(len(donor_names)):
                    if donor_names[i]==full_name and flag==0:
                        donations=float(input("Please enter a donation==>"))
                        donor_donations[i].append(donations)
                        flag=1
        if flag==0:
            donor_names=donor_names+(full_name,)
            donations=float(input("Please enter a donation==>"))
            donor_donations=donor_donations+([donations,],)
        thank_you_string=f'Dear {full_name}, Thank you so much for your generous donation of {donations}.  We appreciate you very much.'
        print(thank_you_string)

def report():
    return 0
    
def main():
    print("Welcome to mailroom")
    answer=""
    while (answer !='q'):
        print("Please select from the following")
        print("Enter t for Thank You\n"
              "Enter r for Report\n"  
              "Enter q to quit")
        answer=input("==>")
        answer.strip()
        answer=answer[:1].lower()
        if answer == 't':
            thank_you(donor_names,donor_donations)
        if answer == 'r':
            report()

if __name__ == "__main__":
    main()