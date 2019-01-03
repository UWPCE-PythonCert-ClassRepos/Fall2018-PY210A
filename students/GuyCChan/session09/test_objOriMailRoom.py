from objOriMailRoom import Donor, test_data, DonorCollection # make_report, letters_to_donors, test_data
import pytest

sample_db = DonorCollection(test_data())

""" Tests for Donor class."""
def test_empty_db():
    test_db = DonorCollection()
    assert len(test_db.donors) == 0

def test_create_donor_in_empty_db():
    donor = Donor("Mike May")
    assert donor.name == "Mike May"
    assert donor.last_donation is None

def test_add_donation():
    donor = Donor("Mike May")
    donor.add_donation("100.00")
    assert donor.last_donation == 100.00

def test_for_very_small_donation():
    donor = Donor("Teri Thomas")
    with pytest.raises(ValueError):
        donor.add_donation("0.05")

def test_for_negative_doantion():
    donor = Donor("Teri thomas")
    with pytest.raises(ValueError):
        donor.add_donation("-50.00")

def test_num_donations():
    donor = Donor("Teri Thomas", [60.00, 49.50, 100.50])
    assert donor.num_donations == 3

def test_tot_donations():
    donor = Donor("Teri Thomas", [60.00, 49.50, 100.50])
    assert donor.tot_donations == 210.00

def test_avg_donation():
    donor = Donor("Teri Thomas", [60.00, 49.50, 100.50])
    assert donor.avg_donation == 70.00

def test_last_donation():
    donor = ("Mike May", [100.00, 150.00, 25.00, 200.00])
    assert donor[1][-1] == 200.00


""" Tests for DonorCollection class."""
def test_donors_in_db():
    assert "John Goodfellow" in sample_db
    assert sample_db("Mike May") is None
    assert len(sample_db) == 6

def test_add_donor():
    new_donor = donor("Alison Ailey")
    assert "Alison Ailey" in sample_db
    assert new_donor.value() is None

def test_find_donor():
    donor = donor("Dave Day")
    assert test_data(donor) is None

def test_make_donor_report():


def test_thank_all_donors():


def test_thank_you_letter():




