#!/usr/bin/env Python3


######
#Created by: Carol Farris
#Name: test_OO_Mailroom.Python.py
#Purpose: Create an object oriented Mailroom
#Progress:
#Working on getting the tests up and running
#####

from OO_Mailroom import *


def test_donor_name():
    donor = Donor("A Person")

    assert donor.name == "A Person"


def test_add_donation():
    donor = Donor("Yo Mama")
    donor.add_donation(500)
    donor.add_donation(200)
    print('donor.donations[0]', donor.donations[0])
    assert donor.donations[0] == 500
    assert donor.num_donations == 2

"""
Test, donation is numerical to add donation
"""


def test_donor_collection():
    dc = DonorCollection()



def test_add_donor():
    """Tests that you can add a donor to the DonorCollection object. 
       Then add a donation, then confirm the name is they key in the
       dictionary."""
    donor = Donor("Pippy Longstocking")
    dc = DonorCollection()
    donor.add_donation(25)
    dc.addDonor(donor.name, donor)
    donor2 = Donor("Manu Chow")
    donor2.add_donation(500)
    dc.addDonor(donor2.name, donor2)

    assert "Manu Chow" in dc.donor_dict.keys()
    assert "Pippy Longstocking" in dc.donor_dict.keys()
   

def test_get_sum_of_donations():
    donor = Donor("Pippy Longstocking")
    donor.add_donation(25)
    donor.add_donation(300)
    donor.add_donation(500)

    assert donor.sum_donations() == 825


def test_get_last_donation():
    donor = Donor("Pippy Longstocking")
    donor.add_donation(25)
    donor.add_donation(300)
    donor.add_donation(500)
    print(donor.get_last_donation())
    assert donor.get_last_donation() == 500

def test_sum_thank_your_letter():
    """Returns a thank you letter that defaults to last value unless you indicate sum for the thank you to reference sum"""
    donor = Donor("Pippy Longstocking")
    donor.add_donation(25)
    donor.add_donation(300)
    donor.add_donation(500)

    print(donor.thank_your_letter())
    assert donor.thank_your_letter() == dedent(
        '''\tDear Pippy Longstocking,
        Thank you for your generous donation of $500 to our cause.
        
        Sincerely,
        The Team''')

    print(donor.thank_your_letter('sum'))
    assert donor.thank_your_letter('sum') == dedent(
        '''\tDear Pippy Longstocking,
        Thank you for your generous donation of $825 to our cause.
        
        Sincerely,
        The Team''')


#def test_get_donor_Object():



#def test_search_donor():
#    pass

