import statistics 

donors={
"Bill Gates":[100.00,200.00,300.00],
"Jack Frost":[2.00,5.00,200.00],
"Maya Angelou":[20000.00,20.00,1234.56]
}   



def make_headers_string():
    headers=("Donor Names","Total Given","Num Gifts","Average Gifts")
    header_string=f'{headers[0]:<20} {headers[1]:<15} {headers[2]:<15} {headers[3]:<15}'
    return header_string
    
def make_sum_donors(d_donors):
    sum_donors=[[k,[average_donations(v),total_donations(v),count_donations(v)]] for (k,v) in d_donors.items()]
    return sum_donors
        
def average_donations(amount):
    return statistics.mean(amount)

def total_donations(amount):
    return sum(amount)

def count_donations(amount):
    return len(amount)

def make_report_strings(sum_donors):
    report_strings=[f'{donor[0]:<20} ${donor[1][1]:<15.2f} {donor[1][2]:<15} ${donor[1][0]:<15.2f}' for donor in sum_donors]
    return report_strings   

def sort_key(item):
    return item[1][1]
    
def make_total_donors(d_donors):   
    return [[k,total_donations(v),make_filename(k)] for (k,v) in d_donors.items()]

def make_filename(name):    
    return f'{name.replace(" ","_")}.txt'

def make_thank_you_list(total_donors):
        return [[thank_donor_msg(donor[0],donor[1]),donor[2]] for donor in total_donors]
    

def send_file(msg,filename):
    print("Here")
    with open(filename,"w") as outfile:
        outfile.write(msg)

def thank_donor_msg(donor_name,donation):
    return (f'Dear {donor_name}, Thank you for your donation of ${donation:.2f}.'
    'These funds help save the migratory butterflies of New South East.Thank you')

def list_donors(d_donors):
    return [donor for donor in d_donors]
    
def add_donation(full_name,d_donors):
    if full_name not in d_donors:
        d_donors[full_name]=[]
    while True: 
        try:
            donation=float(input("Please enter a donation==>"))
        except ValueError:
            print("Please enter a numerical donation")
        else:
            d_donors[full_name].append(donation)
            return donation
                
def thank_you():
    while True:
        full_name=input("Please enter a Full Name==>")
        if full_name.lower()=="list":
            print(list_donors(donors))
        else:
            donation=add_donation(full_name,donors) 
            send_file(thank_donor_msg(full_name,donation),make_filename(full_name))
            break
    
def report():
    print(make_headers_string())
    report_strings=make_report_strings(sorted(make_sum_donors(donors), key=sort_key,reverse=True))
    for report_string in report_strings:
        print(report_string)    

def send_donors():
    total_donors=make_total_donors(donors)
    thank_you_lists=make_thank_you_list(make_total_donors(donors))
    for thank_you_list in thank_you_lists:
        send_file(thank_you_list[0],thank_you_list[1])
            


def unknown():
    print("Please enter a valid response")
    return None 

def main():
    menu={
    "t":thank_you,
    "r":report,
    "s":send_donors,
    }
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