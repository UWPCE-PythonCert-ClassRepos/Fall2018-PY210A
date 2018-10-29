#!/usr/bin python3

donors = [("Fred Jones", [100, 200, 300]), 
    ("Amy Shumer", [1000, 2000, 3000]),
    ("Bill Gates", [200, 400, 750, 400]),
    ("John Smith Jr.", [200, 400, 9050.20, 30]),
    ("Jeff Bezos", [200, 225.50, 10000, 30])]

def thank_you():
    name_entered = "list"
    while name_entered == "list":
        name_entered = input("Enter a donor name => ")
        if name_entered.lower().strip() == "list":
            for donor in donors:
                print(f"- {donor[0]}")
            continue
        
    for donor in donors:
        if donor[0].lower().strip() == name_entered.lower().strip():
            found = donor
            break
    else:
        print("New Donor added!")
        found = (name_entered, [])
        donors.append(found)
    
    donor_amount = float(input(f"How much did {name_entered} donate? "))
    found[1].append(donor_amount)
    print("""Dear {},

    Thank you for your ${:.2f} donation to our charity.
    
    Sincerely,
    CEO Bob Newsenbaumerson\n""".format(name_entered, donor_amount))

def make_report():
    print()
    print("{:<20}| Total Given | Num Gifts | Average Gift".format("Donor Name"))
    print("-" * 60)
    donors.sort(key=report_sort, reverse=True)
    for donor in donors:
        print("{:<21}${:>11.2f}{:>12}  ${:>12.2f}".format(donor[0],sum(donor[1]),len(donor[1]), sum(donor[1]) / len(donor[1])))

def report_sort(e):
    return sum(e[1])

def main():
    print("*** Welcome to Mailroom! ***")
    answer = "s"
    while answer != "q":
        print()
        print("\n".join([
            "Please select from the following:",        
            "1. Thank You: 't'",
            "2. Report: 'r'",
            "3. Quit: 'q'"]))
        answer = input(" => ")[0:1].lower().strip()
        if answer == 't':
            thank_you()
        elif answer == 'r':
            make_report()

if __name__ == "__main__":
    main()