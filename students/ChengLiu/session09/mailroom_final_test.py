#!/usr/bin/env python3

"""
Cheng Liu
Mail-room Final
"""

# import os
# import pytest
from .mailroom_final import Donor


def test_donor_with_donation():
    donor_test = Donor("test name", [1, 2, 3])
    # assert donor_test.name == "Test Name"
    # assert donor_test.donations == [1, 2, 3]
    assert donor_test.donor_name == "Test Name"
    assert donor_test.list_donations == [1, 2, 3]
    assert donor_test.last_donation == 3


def test_donor_without_donation():
    donor_test = Donor("test name")
    # assert donor_test.name == "Test Name"
    # assert donor_test.donations == [1, 2, 3]
    assert donor_test.donor_name == "Test Name"
    assert donor_test.list_donations == []
    assert donor_test.last_donation is None


def test_total_donations():
    donor_test_1 = Donor("test name", [1, 2, 3])
    assert donor_test_1.total_donations == 6

    donor_test_2 = Donor("test name")
    assert donor_test_2.total_donations == 0


def test_num_of_donations():
    donor_test_1 = Donor("test name", [1, 2, 3])
    donor_test_2 = Donor("test name")

    assert donor_test_1.num_of_donations == 3
    assert donor_test_2.num_of_donations == 0


def test_avg_donations():
    donor_test_1 = Donor("test name", [1, 2, 3])
    donor_test_2 = Donor("test name")

    assert donor_test_1.avg_donations == 2
    assert donor_test_2.avg_donations is None


# def test_find_donor():
#     donors_test = Donor("test One", [1, 2, 3])

#     donor_target = donors_test.find_donor("test one")
#     assert donor_target.name == "Test Name"
#     assert donor_target.donations == [1, 2, 3]

#     donor_none = donors_test.find_donor("test five")
#     assert donor_none.name is None
#     assert donor_none.donations is None








# def test_add_donor():
#     donor = Donor("Kobe Br")
#     assert donor.name == "Kobe Br"
#     assert donor.last_donation is None


# def test_add_donation():
#     donor.add_donation(100)


#     assert donor.last_donation == 100


# def test_list_donors():
#     assert "Default Test1" in Donor.list_donors()


# def test_find_donors():
#     test_donor = Donor.find_donors('default test3')
#     assert test_donor is None


# def test_letter():
#     donor = Donor("Jeff Bzo", [100.10, 50.50])
#     donor_letter = donor.letter(donor)
#     assert "Jeff Bzo" in donor_letter
#     assert "$50.50" in donor_letter


# def test_report():
#     assert "Jeff Bzo" in report
