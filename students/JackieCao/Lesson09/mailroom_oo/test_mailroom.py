#!/usr/bin/env python

"""
test
"""

import os
import pytest
from donor_models import Donor, DonorDB, get_sample_data

import cli_main

sample_db = DonorDB(get_sample_data())

def test_db():
    db = DonorDB()
    assert len(db.donors) == 0


def test_add_donation():
    donor = sample_db.donor_data.popitem()[1]

    donor.add_donation(3000)

    assert donor.last_donation == 3000


def test_list_donors():
    sample_db = DonorDB(get_sample_data())
    listing = sample_db.list_donors()
    assert listing.startswith("Donor list:\n")
    assert "J Bob" in listing
    assert len(listing.split('\n')) == 5


def test_gen_letter():
    donor = Donor("F Bob", [400, 400])
    letter = sample_db.gen_letter(donor)
    print(letter)
    assert letter.startswith("Dear F Bob")
    assert "donation of $400" in letter


def test_add_donor():
    name = "F Bob"

    donor = sample_db.add_donor(name)
    donor.add_donation(300)
    assert donor.name == "F Bob"
    assert donor.last_donation == 300


def test_generate_donor_report():
    sample_db = DonorDB(get_sample_data())
    report = sample_db.generate_donor_report()

    print(report)


def test_save_letters_to_disk():

    sample_db.save_letters_to_disk()
    assert os.path.isfile('J_Bob.txt')


