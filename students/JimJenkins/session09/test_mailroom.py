#!/usr/bin/env python3

from mailroom import Donor


def test_create_donor():
    donor = Donor('name')

    assert donor.name == 'name'

def test_add_donation():
    donor = Donor('name')

    donor.add_donation(500)

    assert donor.num_donations == 1

def test_donor_thank_you_letter():
    pass


def test_donation_collection():
    dc = DonorCollection()

    dc.add_donor(Donor('Bob'))
    dc.find_donor()

    dc.list_donors()

    dc.thank_donors()

    dc.create_report()

