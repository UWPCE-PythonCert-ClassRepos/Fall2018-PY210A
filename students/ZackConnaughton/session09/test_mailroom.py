"""
inputs and prints not in this code for testing
"""

import os
from mailroom import Donor

def test_create_donor_name():
    d = Donor("Fred Flintstone")
    assert d.name == "Fred Flintstone"

def test_add_donation():
    d = Donor("Fred Flintstone")
    d.add_donation(100)
    assert d.donation_count == 1
    assert d.latest_donation == 100

def test_total_donations():
    pass


def test_average_donation():
    pass


def test_donor_thank_you():
    d.thank_you_note()


def test_donor_list():

    dl = donor_list():

    dl.add_donor(Donor("Bobby Johnny"))

    dl.find_donor():

    dl.list_donors():

    dl.donor_report():
