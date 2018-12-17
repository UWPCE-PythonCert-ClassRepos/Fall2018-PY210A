# Tests for Mailroom - Object Oriented

from donor_models import Donor, DonorCollection
import cli_main as cm


import pytest
import datetime
import os


# Tests for Donor Class
def test_donor_init():
    donor = Donor("George Jetson")

    assert donor.name == "George Jetson"
    assert donor.donations == []


def test_donor_init2():
    with pytest.raises(TypeError):
        Donor("George Jetson", 100)


def test_add_donation():
    donor = Donor("George Jetson")

    donor.add_donation(200)
    assert donor.donations == [200]

    donor.add_donation(300)
    assert donor.donations == [200, 300]


def test_num_donations():
    donor = Donor("Jane Jetson")

    donor.add_donation(100)
    assert donor.num_donations == 1

    donor.add_donation(100)
    assert donor.num_donations == 2


def test_total_donations():
    donor = Donor("Jane Jetson")

    donor.add_donation(100)
    assert donor.total_donations == 100

    donor.add_donation(200)
    assert donor.total_donations == 300


def test_avg_donation():
    donor = Donor("Jane Jetson")
    assert donor.avg_donation == 0

    donor.add_donation(100)
    assert donor.avg_donation == 100

    donor.add_donation(200)
    assert donor.avg_donation == 150


logo = r"""
  _   _   _   _     _   _   _   _   _   _   _   _   _   _  
 / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
( M | a | r | s ) ( F | o | u | n | d | a | t | i | o | n )
 \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
"""


def test_thank_you_letter():

    date = datetime.datetime.now().strftime("%B %d, %Y")
    donor = Donor("Judy Jetson")
    donor.add_donation(150)
    letter = donor.thank_you_letter()

    assert letter == f"{logo}\n\n{date}\n\n" \
        f"Dear Judy Jetson:\n\n" \
        f"Thank you so much for the generous donation of $150.00.\n" \
        f"We will use the money to help Earthlings move to Mars!\n\n" \
        f"Best regards,\nDianna Tingg\nMars Foundation"


# Tests for DonorCollection Class
def test_coll_init():
    charity = DonorCollection()
    assert charity.donors_dict == {}


def test_coll_create_donor():
    charity = DonorCollection()
    charity.create_donor("Judy Jetson")

    assert "Judy Jetson" in charity.donors_dict
    assert charity.donors_dict["Judy Jetson"].donations == []


def test_coll_find_donor():
    charity = DonorCollection()
    charity.create_donor("Judy Jetson")

    assert charity.find_donor("Judy Jetson") == charity.donors_dict["Judy Jetson"]


def test_coll_find_donor2():
    charity = DonorCollection()

    assert charity.find_donor("Rosie") == charity.donors_dict["Rosie"]


def test_list_donors():
    charity = DonorCollection()
    charity.create_donor("Elroy Jetson")
    charity.create_donor("Astro")
    donor_list = charity.list_donors()

    assert donor_list == ["Astro", "Elroy Jetson"]


def test_sort_key():
    charity = DonorCollection()
    test = ["Elroy Jetson", 400, 2, 200]

    assert charity.sort_key(test) == 400


def test_create_report():
    charity = DonorCollection()
    charity.create_donor("Elroy Jetson")
    charity.donors_dict["Elroy Jetson"].add_donation(100)
    charity.donors_dict["Elroy Jetson"].add_donation(100)

    charity.create_donor("Astro")
    charity.donors_dict["Astro"].add_donation(300)

    assert charity.create_report() == [["Astro", 300, 1, 300], ["Elroy Jetson", 200, 2, 100]]


# Tests for main program
def test_check_name_invalid():
    name1 = cm.check_name("")
    assert name1 is False

    name2 = cm.check_name("5")
    assert name2 is False


def test_check_name_exit():
    name3 = cm.check_name("E")
    assert name3 is None


def test_check_name_list():
    name4 = cm.check_name("L")
    assert name4 is False


def test_check_donation_exit():
    amount1 = cm.check_donation("etc")
    assert amount1 is None


def test_check_donation_small():
    amount2 = cm.check_donation(".001")
    assert amount2 is False


def test_check_donation_valid():
    amount3 = cm.check_donation("1")
    assert amount3 is True


def test_check_donation_invalid():
    amount4 = cm.check_donation("")
    assert amount4 is False

    amount5 = cm.check_donation("z")
    assert amount5 is False


def test_check_directory():
    dir1 = cm.check_directory("")
    assert dir1 is True
