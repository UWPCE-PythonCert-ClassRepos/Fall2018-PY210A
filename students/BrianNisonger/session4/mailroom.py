import statistics 

donors={
"Bill Gates":[100.00,200.00,300.00],
"Jack Frost":[2.00,5.00,200.00],
"Maya Angelou":[20000.00,20.00,1234.56]
}   

def sort_key(item):
    return item[1][1]
    
def thank_you():
    full_name="list"
    while full_name=="list":
        full_name=input("Please enter a Full Name==>")
        if full_name=="list":
            for donor in donors:
                print (donor)
        else:
            if full_name not in donors:
                donors[full_name]=[]
            while True: 
                try:
                    donation=float(input("Please enter a donation==>"))
                except ValueError:
                    print("Please enter a numerical donation")
                else:
                    break
            donors[full_name].append(donation)
            thank_you_string=f'Dear {full_name}, Thank you for your donation of {donation:.2f}.  These funds help save the migratory butterflies of New South East.  Thank you'
            file_name=full_name.replace(" ","_")
            file_name=f'{file_name}.txt'
            with open(file_name,"w") as outfile:
                outfile.write(thank_you_string)

def report():
    headers=("Donor Names","Total Given","Num Gifts","Average Gifts")
    header_string=f'{headers[0]:<20} {headers[1]:<15} {headers[2]:<15} {headers[3]:<15}'
    print(header_string)
    sum_donors=[[k,[average_donations(v),total_donations(v),count_donations(v)]] for (k,v) in donors.items()]
    sum_donors=sorted(sum_donors, key=sort_key,reverse=True)
    report_strings=[f'{donor[0]:<20} ${donor[1][1]:<15.2f} {donor[1][2]:<15} ${donor[1][0]:<15.2f}' for donor in sum_donors]
    for string in report_strings:
        print(string)
    
def average_donations(amount):
    return statistics.mean(amount)

def total_donations(amount):
    return sum(amount)

def count_donations(amount):
    return len(amount)

def send_donors():
    total_donors=[[k,total_donations(v),f'{k.replace(" ","_")}.txt'] for (k,v) in donors.items()]
    thank_you_string=[[f'Dear {donor[0]}, Thank you for your donation of {donor[1]:.2f}.  These funds help save the migratory butterflies of New South East.  Thank you',donor[2]] for donor in total_donors]
    for t_string in thank_you_string:
        with open(t_string[1],"w") as outfile:
            outfile.write(t_string[0])


def unknown():
    print("Please enter a valid response")
    return None 

def main():
    menu={
    "t":thank_you,
    "r":report,
    "s":send_donors,
    }
    answer=""
    while True:
        print("Please enter one of the following")
        try:
            answer=input("t to Thank a Single Donor\n"
                         "r to Send a Report\n"
                         "s to Send all Donors a Thank You Email\n"
                          "q to Quit:")
            answer=answer[0].lower()
            if answer=="q":
                break
            menu.get(answer,unknown)()
        except KeyboardInterrupt:
            break
            
           

if __name__ == "__main__":
    main()