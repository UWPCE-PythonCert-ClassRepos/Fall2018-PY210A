"""
tests for mailroom part 5
"""


import pytest
from mailroom_oo import donor_modules as mrd


mrd.donors = mrd.get_sample_donors()


def test_create_donor():
    mrd.donor = mrd.Donor("Fred Flintstone")

    assert mrd.donor.name == "Fred Flintstone"
    assert mrd.donor.last_donation is None


def test_add_donation():
    mrd.donor = mrd.Donor("Fred Flintstone")
    print(mrd.donor)
    assert False

    #mrd.donor.add_donation(500)

    #assert 500 in mrd.donors.values()


# def test_number_of_donations():
#     mrd.donor = mrd.Donor("Fred Flintstone")
#     mrd.donor.add_donation(1000)
#     mrd.donor.add_donation(600)
#     print(mrd.donor.num_donations)

    #assert mrd.donor.num_donations == 2

# def test_donor_thank_you_letter():
#     pass
#
#
# def test_donor_collection():
#     mr.dc = mr.DonorCollection()
#
#     mr.dc.add_donor(Donor("Bob"))
#
#         assert "Bob" in mr.dc.donors
#         assert [] == mr.dc.donors.get("Bob")

    # mr.dc.find_donor()
    #
    #
    # mr.dc.list_donors()
    #
    #
    # mr.dc.thank_donors()

# def get_sample_donors():
#     donors = {"Rick Sanchez": [3.00, 1.00],
#               "Liz Lemon": [4000.00, 3000.00, 6000.00],
#               "Andy Dwyer": [10.00],
#               "Brendan Small": [3.00, 10.00],
#               "Coach McGuirk": [2.00, 1.00]}
#     return donors
#
#
# mr.donors = get_sample_donors()
#
#
# def test_adds_new_donor():
#     mr.add_new_donor("Jake Ham")
#
#     assert "Jake Ham" in mr.donors
#     assert [] == mr.donors.get("Jake Ham")
#
#
#
# def test_add_new_donation():
#     mr.add_donation_to_donor("Jake Ham", 500)
#
#     assert 500 in mr.donors.get("Jake Ham")
#
#
#
# def test_add_new_donation_key_does_not_exist():
#     with pytest.raises(KeyError):
#         mr.add_donation_to_donor("Jessica", 1000)
#
#
#
# def test_add_donor_already_exists():
#     mr.add_new_donor("Rick Sanchez")
#
#     assert [3.00, 1.00] == mr.donors.get("Rick Sanchez")
#
#
#
# def test_report_creation():
#     mr.donors = get_sample_donors()
#     report = mr.create_report()
#
#     assert report.startswith("Donor Name")
#     report = report.split("\n")
#     assert report[1].startswith("---")
#     assert len(report) == 7
#
#
#
# def test_check_donation():
#     with pytest.raises(ValueError):
#         mr.check_donation(0)
#
#
#
# def test_check_negative_donation():
#     with pytest.raises(ValueError):
#         mr.check_donation(-123)
#
#
#
# def test_check_donation_return_number():
#     result = mr.check_donation("5000")
#
#     assert result == 5000.0
#
#
#
# def test_gen_letters():
#     result = mr.generate_letter("Rick Sanchez", 500.00)
#
#     assert result.startswith("Dear Rick Sanchez")
#
#
#
# def test_letter_contains_donation():
#     result = mr.generate_letter("Rick Sanchez", 5000)
#
#     assert "Thank you for your crappy donation of $5000.00" in result
#

