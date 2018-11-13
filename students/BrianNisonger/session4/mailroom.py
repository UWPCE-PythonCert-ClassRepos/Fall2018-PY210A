import statistics 

def sort_key(item):
    return item[1]
    
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
            donation=input("Please enter a donation==>")
            donation=float(donation)
            donors[full_name].append(donation)
            thank_you_string=f'Dear {full_name}, Thank you for your donation of {donation:.2f}.  These funds help save the migratory butterflies of New South East.  Thank you'
            file_name=full_name.replace(" ","_")
            file_name=f'{file_name}.txt'
            with open(file_name,"w") as outfile:
                outfile.write(thank_you_string)

def report():
    sum_donor={}
    num_donations={}
    average_donor={}
    temp=[]
    sum_donors=[]
    headers=("Donor Names","Total Given","Num Gifts","Average Gifts")
    header_string=f'{headers[0]:<15} {headers[1]:<15} {headers[2]:<15} {headers[3]:<15}'
    print(header_string)
    for donor in donors:
        sum_donor[donor]=sum(donors[donor])
        num_donations[donor]=len(donors[donor])
        average_donor[donor]=statistics.mean(donors[donor])
    for donor_name in sum_donor:
        sum_donors_tuple=[donor_name,sum_donor[donor_name]]
        sum_donors.append(sum_donors_tuple)
    sum_donors=sorted(sum_donors, key=sort_key,reverse=True)
    for sorted_donors in sum_donors:
        report_string=f'{sorted_donors[0]:<15} ${sorted_donors[1]:<15.2f} {num_donations[sorted_donors[0]]:<15} ${average_donor[sorted_donors[0]]:<15.2f}'
        print(report_string)
      
        

def send_donors():
     sum_donors={}
     for donor in donors:
        sum_donors[donor]=sum(donors[donor])
     for sum_donor in sum_donors:   
        thank_you_string=f'Dear {sum_donor}, Thank you for your donation of {sum_donors[sum_donor]:.2f}.  These funds help save the migratory butterflies of New South East.  Thank you'
        file_name=sum_donor.replace(" ","_")
        file_name=f'{file_name}.txt'
        with open(file_name,"w") as outfile:
            outfile.write(thank_you_string)

def quit():
    pass


    
    
donors={
"Bill Gates":[100.00,200.00,300.00],
"Jack Frost":[2.00,5.00,200.00],
"Maya Angelou":[20000.00,20.00,1234.56]
}    

def main():
    menu={
    "t":thank_you,
    "r":report,
    "s":send_donors,
    "q":quit
    }
    answer=""
    while answer !="q":
        print("Please enter one of the following")
        answer=input("t to Thank a Single Donor\n"
                     "r to Send a Report\n"
                     "s to Send all Donors a Thank You Email\n"
                     "q to Quit:")
        answer=answer[0].lower()
        choices=("t","r","s","q")
        if answer in choices:
            menu.get(answer)()

if __name__ == "__main__":
    main()