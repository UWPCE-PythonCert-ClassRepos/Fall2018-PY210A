import os
from mailroom_oo import Donor

def test_create_donor():
    donor = Donor("Fred Flintstone")
    assert donor.name == "Fred Flintstone"

def test_add_donation():
    donor = Donor("Fred Flintstone")
    donor.add_donation(500)
    assert donor.num_donations == 1

def test_last_donation():
    donor = Donor("Fred Flintstone")
    donor.add_donation(500)
    assert donor.last_donation == 500

def test_num_donations():
    donor = Donor("Fred Flintstone")
    donor.add_donation(500)
    donor.add_donation(10)
    assert donor.num_donations == 2

def test_donor_thank_you_letter():  #donor class
    pass

# def test_donor_collection():
#     dc = DonorCollection()
#
#     dc.add_donor(Donor("Bob"))
#     dc.find_donor()
#     dc.list_donors()
#     dc.thank_donors()
#     dc.create_report()
