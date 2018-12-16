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

# need more works here
# def test_add_donor():
#     donors_orig = [Donor("Test Name_orig", [100, 200])]
#     db = DonorDB(donors_orig)

#     donors_add = [Donor("Test Name_add", [10, 20])]
#     db = db.add_donor(donors_add)
#     assert db["Test Name_add"] == [100, 200]


def test_list_donors():
    donor_test1 = Donor("test name1", [1, 2, 3])
    donor_test2 = Donor("test name2", [10, 20, 30])
    donor_test3 = Donor("test name3", [100, 200, 300])

    donors = [donor_test1, donor_test2, donor_test3]
    donors_db = DonorDB(donors)
    # print(donors_db.donor_data)
    # print(type(donors_db.list_donors()))
    assert donors_db.list_donors() == "Test Name1\n""Test Name2\n""Test Name3"


def test_letter():
    donor = Donor("test name3", [100, 200, 300])
    print(donor)
    print(donor.name)
    print(donor.donations)
    print(donor.last_donation)

    donor_db = DonorDB([donor])
    letter_data = donor_db.donor_data
    print(donor_db)
    print(letter_data)

    donor_letter = donor_db.letter()
    assert "Test Name3" in donor_letter
    assert "$300.00" in donor_letter


# def test_report():
#     assert "Jeff Bzo" in report
