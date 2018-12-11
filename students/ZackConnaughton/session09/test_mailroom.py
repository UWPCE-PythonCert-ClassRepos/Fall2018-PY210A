"""
inputs and prints not in this code for testing
"""

import os
from mailroom import Donor, Donor_Collection


def test_load_donor_dict():
    d_info = {'name': 'Test Donor', "donation_list": [100, 200, 150]}
    d = Donor(d_info)
    assert d.name == "Test Donor"
    assert d.donation_list == [100, 200, 150]

def test_create_donor_by_name():
    d = Donor.from_name("Fred Flintstone")
    assert d.name == "Fred Flintstone"

def test_add_donation():
    d = Donor.from_name("Fred Flintstone")
    d.add_donation(100)
    assert d.donation_count == 1
    assert d.latest_donation == 100

def test_latest_donation():
    d = Donor.from_name("Fred Flintstone")
    assert d.latest_donation is None
    d.add_donation(100)
    assert d.latest_donation == 100
    d.add_donation(200)
    assert d.latest_donation == 200

def test_total_donations():
    d = Donor.from_name("Fred Flintstone")
    assert d.donation_total == 0
    d.add_donation(100)
    d.add_donation(200)
    assert d.donation_total == 300

def test_average_donation():
    d = Donor.from_name("Fred Flintstone")
    assert d.donation_average == 0
    d.add_donation(100)
    d.add_donation(200)
    assert d.donation_average == 150


def test_donor_thank_you():
    d = Donor.from_name("Fred Flintstone")
    d.add_donation(100)
    ty_letter = d.thank_you_letter()
    print(ty_letter)
    assert ty_letter.startswith('Dear Fred Flintstone')
    assert ty_letter.find('donation of $100.00.') != -1
    assert ty_letter.count("\n") == 7


def test_create_donor_list():
    donor_dict = {'TestDonor1': {'name': 'Test Donor1', "donation_list": [100, 200, 150]},
                  'TestDonor2': {'name': 'Test Donor2', "donation_list": [60, 90, 200]}}
    dc = Donor_Collection(donor_dict)
    assert len(dc.donors) == 2

def test_add_donor_to_collection():
    donor_dict = {'TestDonor1': {'name': 'Test Donor1', "donation_list": [100, 200, 150]},
                  'TestDonor2': {'name': 'Test Donor2', "donation_list": [60, 90, 200]}}
    dc = Donor_Collection(donor_dict)
    dc.add_donor('Added_Donor')
    assert len(dc.donors) == 3

def test_find_donor():
    donor_dict = {'TestDonor1': {'name': 'Test Donor1', "donation_list": [100, 200, 150]},
                  'TestDonor2': {'name': 'Test Donor2', "donation_list": [60, 90, 200]}}
    dc = Donor_Collection(donor_dict)
    assert dc.find_donor('Test Donor2').name == 'Test Donor2'
    assert not dc.find_donor('Not_Found_Donor')


def test_list_donors():
    donor_dict = {'TestDonor1': {'name': 'Test Donor1', "donation_list": [100, 200, 150]},
                  'TestDonor2': {'name': 'Test Donor2', "donation_list": [60, 90, 200]}}
    dc = Donor_Collection(donor_dict)
    assert dc.list_donors() == ['Test Donor1', 'Test Donor2']


def test_donor_report():
    donor_dict = {'TestDonor1': {'name': 'Test Donor1', "donation_list": [100, 200, 150]},
                  'TestDonor2': {'name': 'Test Donor2', "donation_list": [60, 90, 200]}}
    dc = Donor_Collection(donor_dict)
    dc_report = dc.report()
    assert len(dc_report) == 2
    assert 'Test Donor1' in dc_report[0]
    assert 150 in dc_report[0]
    assert 350 in dc_report[1]
    for donor in dc_report:
        assert not 'Cher' in donor
