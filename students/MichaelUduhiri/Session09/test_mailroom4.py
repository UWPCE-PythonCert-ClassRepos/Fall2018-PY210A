import os
from mairoom4 import donor

def create_donor():
    donor = Donor("Fred Flintstone")

    assert donor.name == "Fred Flintstone"

def test_add_donation():
    donor = Donor("Fred Flintstone")

    donor.add_donation(500):

    assert donor.num_donations == 1

def test_donor_thank_you_letter():
    pass

def test_donor_colleciton():
    dc = DonorCollection()

    dc.add_donor(donor("Bob"))

    dc. find_donor()

    dc.list_donor()
