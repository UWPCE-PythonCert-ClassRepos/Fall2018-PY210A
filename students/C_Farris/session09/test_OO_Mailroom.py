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
    donor = Donor("Pippy Longstocking")
    dc = DonorCollection()
    print(dc.donor_dict)
    donor.add_donation(25)
    print("donor name", donor.name)
    print("donor donations", donor.donations)

    dc.addDonor(donor.name, donor)
    print(dc.donor_dict[donor.name])
   
    donor2 = Donor("Manu Chow")
    donor2.add_donation(500)
    dc.addDonor(donor2.name, donor2)
    print(dc.donor_dict[donor2.name])
    print(dc.donor_dict)

    assert  2 == 25

def test_get_donor_Object():
    pass    



#def test_get_last_donation():
#    pass


#def test_get_sum_of_donations():
#    pass


#def test_search_donor():
#    pass

#def test_donor_thank_your_letter():
#    pass