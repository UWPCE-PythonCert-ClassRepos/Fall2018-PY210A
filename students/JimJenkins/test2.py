
"""
Send a Thank You

    If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
        If the user types list show them a list of the donor names and re-prompt.
        If the user types a name not in the list, add that name to the data structure and use it.
        If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
        Convert the amount into a number; it is OK at this point for the program to crash if someone types a bogus amount.
        Add that amount to the donation history of the selected user.
    Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.

It is fine (for now) for the program not to store the names of the new donors that had been added, in other words, to forget new donors once the script quits running.
"""
from typing import List


def main():
    pass


def show_list(a):
    """
    if the user types list, show them a list of the donors names.
    :param a: list (0,1)
    :return: donor's list
    """
    if a == 'yes':
        print('Donor List:')
        for donor in donor_list:
            print('- ', donor)
    elif a == 'no':
        print('No donor list requested.')


def search_donors(a):
    """
    search the donors list for the donors name in the list.
    :param a: donor's name (a)
    :return:
    """
    if a.lower() in donor_list_lower:
        print('Found the donor', a, '.')
    else:
        print('No donor found.')
    return


def add_donor(a):
    """
    if the name of the donor is NOT on the list, add it.
    :param a: donor's name (a)
    :return: success note
    """
    if a not in donor_list:
        donor_list.append(a)
        print('Added', a, 'to the donors list.')


def get_donation_amount(a):
    """
    prompt the user for the donation amount.
    :param a: donation amount (a)
    :param b: donor's name (str)
    :return: confirmation message
    """
    a = float(input('How much would you like to contribute?: '))
    print('You would like to donate: ${:,.2f}'.format(a))

donors = {'John Roberts': [100, 200, 300],
          'Clarence Thomas': [200, 400, 600],
          'Ruth Bader-Ginsberg': [700, 100, 2000],
          'Elena Kagen': [1800, 2300, 7000],
          'Sonia Sotomayor': [500, 190, 212, 55],
          'Neil Gorsuch': [100, 3000],
          'Brett Kavanaugh': [400, 4500],
          'Samuel Alito': [1000, 1000, 1000],
          'Stephen Breyer': [200, 300, 10000]}

print(donors)

donor_list = ['Jim Jenkins', 'Elaine Jenkins']
donor_list_lower = [item.lower() for item in donor_list]
success = 'successful execution'

show_donors = input('show list? : ')
if show_donors == 'list':
    show_donors = 'yes'
else:
    show_donors = 'no'



if __name__ == '__main__':
    #main()
    print('<<<<< unit tests >>>>>>')
    assert show_list('yes') is None
    assert show_list('no') is None
    assert search_donors('Jim Jenkins') is None
    assert search_donors('jim Jenkins') is None
    assert search_donors('Tom Jenkins') is None
    assert search_donors('Elaine Jenkins') is None
    assert add_donor('Nathan Jenkins') is None
    print(donor_list)
    assert get_donation_amount(200.00)is None
