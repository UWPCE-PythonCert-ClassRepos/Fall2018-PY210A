#!/usr/bin/env Python3


######
#Created by: Carol Farris
#Name: test_OO_Mailroom.Python.py
#Purpose: Create an object oriented Mailroom
#Progress:
#Working on getting the tests up and running
#####

from mailroom import *


def test_donor_name():
    donor = Donor("A Person")

    assert donor.name == "A Person"


def test_add_donation():
    donor = Donor("Yo Mama")
    donor.add_donation(500)

    assert donor.donation == 500
    assert donor.num_donations == 1


def test_donor_collection():
    dc = DonorCollection()


def test_get_last_donation():
    pass


def test_get_sum_of_donations():
    pass


def test_search_donor():
    pass

def test_donor_thank_your_letter():
    pass