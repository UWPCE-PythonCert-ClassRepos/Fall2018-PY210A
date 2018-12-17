import os
import mailroom4


def test_donor_name():
    donor = Donor("Fred Flinstones")

    assert donor.name == "Fred Flinstones"


def test_add_donation():
    donor = Donor("Fred Flinstones")

    donor.add_donation(500)

    assert donor.num_donations == 1


def test_donor_thank_you():
    pass


def test_donor_collection():
    dc = DonorCollection()

    dc.add_donor(Donor("Bob"))

    dc.find_donor()

    dc.list_donors()

    dc.thank_donors()

    dc.create_report()