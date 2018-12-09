# Tests for Mailroom - Object Oriented

from mailroom_oo.donor_models import Donor, DonorCollection
import pytest


# Tests for Donor Class
def test_donor_init():
    donor = Donor("George Jetson", 100)

    assert donor.name == "George Jetson"
    assert donor.donations == [100]


def test_donor_init2():
    with pytest.raises(TypeError):
        Donor("Jane Jetson")


def test_add_donation():
    donor = Donor("George Jetson", 100)
    donor.add_donation(200)

    assert donor.donations == [100, 200]


def test_num_donations():
    donor = Donor("Jane Jetson", 200)
    assert donor.num_donations == 1

    donor.add_donation(200)
    assert donor.num_donations == 2


def test_total_donations():
    donor = Donor("Judy Jetson", 100)
    assert donor.total_donations == 100

    donor.add_donation(200)
    assert donor.total_donations == 300


def test_avg_donation():
    donor = Donor("Elroy Jetson", 200)
    assert donor.avg_donation == 200

    donor.add_donation(100)
    assert donor.avg_donation == 150


# Tests for DonorCollection Class
def test_coll_init():
    charity = DonorCollection()
    assert charity.donors_dict == {}


def test_coll_add_donation_new():
    charity = DonorCollection()
    charity.add_donation("Judy Jetson", 100)

    assert "Judy Jetson" in charity.donors_dict
    assert charity.donors_dict["Judy Jetson"].donations == [100]


def test_coll_add_donation_existing():
    charity = DonorCollection()
    charity.add_donation("Elroy Jetson", 100)
    charity.add_donation("Elroy Jetson", 200)

    assert "Elroy Jetson" in charity.donors_dict
    assert charity.donors_dict["Elroy Jetson"].donations == [100, 200]


def test_list_donors():
    charity = DonorCollection()
    charity.add_donation("George Jetson", 400)
    charity.add_donation("Jane Jetson", 300)
    charity.add_donation("Judy Jetson", 200)
    charity.add_donation("Elroy Jetson", 100)
    donor_list = charity.list_donors()

    assert donor_list == ["Elroy Jetson", "George Jetson", "Jane Jetson", "Judy Jetson"]

def test_sort_key():
    charity = DonorCollection()
    test = ["Rosie Robot", 400, 2, 200]

    assert charity.sort_key(test) == 400

def test_create_report():
    charity = DonorCollection()
    charity.add_donation("Judy Jetson", 400)
    charity.add_donation("Elroy Jetson", 500)

    assert charity.create_report() == [["Elroy Jetson", 500, 1, 500], ["Judy Jetson", 400, 1, 400]]

# Tests for main program




print("All tests passed!")

# def test_donor_thank_you_letter():
# def test_donor_collection():
#     dc.find_donor()
#     dc.thank_donors()
