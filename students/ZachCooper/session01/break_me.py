#!/usr/bin/env python

# I tried a couple of error exceptions that I commonly ran into during my Foundations class
# Example of ZeroValueError
def divide_things(num1, num2):
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("Ummm...You totally can't divide by 0")
        raise ZeroDivisionError


divide_things(12, 0)

# Example of ValueError
try:
    num = float(input("Enter a number: "))
except ValueError:
    print("That was not a number!!")
else:
    print("Your number is:")

# Example of FileError
try:
    fakefile = open('fake.txt', 'r')
    fakefile.read()
except FileNotFoundError:
    print("Sorry your file doesn't exist...")
except Exception as e:
    print(e)
    print("Unknown error, sorry!")

# Example of KeyError
seahawks_dict = {'Russell Wilson': 'Quarterback', 'Doug Baldwin': 'Wide Receiver', 'Pete Carrol': 'Coach',
                 'BobbyWagner': 'Linebacker'}


def seahawks_exception():
    try:
        print(seahawks_dict[1])
        print(seahawks_dict[2])
        print(seahawks_dict[4])
    except KeyError:
        print("That is not a key in the Seahawks Dictionary!")


seahawks_exception()
