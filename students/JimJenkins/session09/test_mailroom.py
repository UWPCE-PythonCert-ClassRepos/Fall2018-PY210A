#!/usr/bin/env python3

"""
Author: Jim Jenkins
Date: 12/10/2018

Description: Object oriented version of mail room.
"""

from .mailroom import Donor, Donor_collection


def test_create_donor():
    donor = Donor('Tom Tinker')

    assert donor.name == 'Tom Tinker'
    print(donor)


def test_add_donation():
    donor = Donor('Tom Tinker')
    donor.add_donation(500)

    assert donor.num_donations == 1


def test_lookup_donor():
    donor = Donor('Tom Tinker')
    assert Donor.find_donor(donor) == 1


def test_donor_thank_you_letter():
    pass
