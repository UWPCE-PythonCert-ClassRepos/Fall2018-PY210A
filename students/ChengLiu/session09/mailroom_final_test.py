#!/usr/bin/env python3

"""
Cheng Liu
Mail-room Final
"""

# import os
# import pytest
from .mailroom_final import Donor, DonorDB


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


def test_donor_data():
    donors = [Donor("Test Name_1", [1, 2, 3]),
              Donor("Test Name_2", [10, 20, 30]),
              Donor("Test Name_3")]

    db = DonorDB(donors)

    assert db.donor_data == {"Test Name_1": [1, 2, 3],
                             "Test Name_2": [10, 20, 30],
                             "Test Name_3": []}


def test_find_donor():
    donors = [Donor("Test Name_1", [1, 2, 3])]
    db = DonorDB(donors)

    assert db.find_donor("Test Name_1") == [1, 2, 3]


def test_find_no_donor():
    donors = [Donor("Test Name_1", [1, 2, 3])]
    db = DonorDB(donors)

    assert db.find_donor("Test Name_5") is None


def test_add_donor():
    donors = [Donor("Test Name_1", [1, 2, 3])]
    db = DonorDB(donors)
    db.add_donor("Test Name_added", 100)
    assert db["Test Name_add"] == [100]




# def test_list_donors():
#     assert "Default Test1" in Donor.list_donors()


# def test_letter():
#     donor = Donor("Jeff Bzo", [100.10, 50.50])
#     donor_letter = donor.letter(donor)
#     assert "Jeff Bzo" in donor_letter
#     assert "$50.50" in donor_letter


# def test_report():
#     assert "Jeff Bzo" in report
