#!/usr/bin/env python3
"""
for testing
"""
import glob
import pytest
from donor_models import *
from cli_main import donors

def test_create_donor():
    donor = Donor("Fred Flintstone")

    assert donor.name == "Fred Flintstone"

def test_add_donation():
    donor = Donor("Fred Flintstone")

    donor.add_donation(500)

    assert donor.num_donations == 1
    assert donor.new_donation == 500

def test_donor_thank_you_data():
    donor = Donor("Bob")
    donor.add_donation(500)
    assert donor.thank_you_data == {'d_name': 'Bob', 'd_dollar': 500}


def test_donor_collection():
    dc = DonorCollection()
    d = Donor("Bob")
    d.add_donation(500)

    dc.add_old_donors(donors)
    dc.add_donor(d.name, d.donations)

    assert dc.list_donors == ['Fred Jones', 'Amy Shumer', 'Bean Shing', 'Ann Shaw', 'King May', 'Bob']

    assert dc.report_data == [('Fred Jones', 600, 3, 200.0),
                              ('Amy Shumer', 30, 2, 15.0),
                              ('Bean Shing', 420, 2, 210.0),
                              ('Ann Shaw', 500, 2, 250.0),
                              ('King May', 800, 4, 200.0),
                              ('Bob', 500, 1, 500.0)]

    dc.send_thank_to_all()
    files = sorted(glob.glob("*.txt"))
    assert files == [k + '.txt' for k in sorted(dc.list_donors)]


