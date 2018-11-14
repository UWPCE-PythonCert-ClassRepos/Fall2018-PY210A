#!/usr/bin python3
import sys

donors_info = [("Bill Gates", [3500, 5500, 7500]),
               ("Paul Alen", [3000, 3700, 3900]),
               ("Jeff Benzo", [3300, 5000, 7500]),
               ("Mark Zuckerberg", [33565.37, 465.37, 545.37, 7506]),
               ("Warren Buffett", [3303.17, 334.17, 5080, 7500])
               ]

prompt = "\n".join(("\n Please choose from the following!:",
                    " Choices are ?:",
                    " T - To Send a Thank you!",
                    " R - To Create a Report",
                    " Q - To Exit",
                    " >>> "))

def send_thankyou():
    d_name = "list"
    while d_name == "list":
        d_name = input("Enter a donor name Or Type \'list' if you don't know the name ?: ")
        if d_name == "list":
            for name in donors_info:
                print(f"- {name[0]}")
            continue

    for name in donors_info:
        if name[0] == d_name:
            new_name = name
            break
    else:
        print("New Donor added!")
        new_name = (d_name, [])
        donors_info.append(new_name)

    contribution = float(input(f"Enter {d_name} contribution :? "))
    new_name[1].append(contribution)
    print()
    print("""
    Dear {:<10}\n,
    Thank you for your generous donation ${:,.2f}.
    """.format(d_name, contribution))
    print("\n Best regards,\n Your Youth and Seniors Foundation \n")


def create_report():
    print()
    print("{:<20}| {:<10} | {:<10} | {:<10}".format("Donor Name", "Total Given", " Num Gifts", "Average Gift"))
    print("-" * 60)
    # donors_info.sort(key=report_sort, reverse=True)
    for name in donors_info:
        print("{:<21} ${:>11.2f} {:>12} ${:>12.2f}".format(
            name[0], sum(name[1]), len(name[1]), sum(name[1]) / len(name[1])))


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

def main():
    while True:
        response = input(prompt)

        if response == "T":
            send_thankyou()

        elif response == "R":
            create_report()

        elif response == "Q":
            exit_program()

        else:
            print("No a valid option")


if __name__ == '__main__':
    main()

