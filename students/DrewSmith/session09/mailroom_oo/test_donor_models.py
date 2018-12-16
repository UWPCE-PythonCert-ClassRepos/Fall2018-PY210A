#!/usr/bin python3
from donor_models import Donor
from donor_models import DonorCollection
import pytest
import pathlib
import os


def setup_DonorCollection():
    donors = DonorCollection()
    donors.add_donor(Donor("Fred Jones", [100, 200, 300]))
    donors.add_donor(Donor("Amy Shumer", [1000, 2000, 3000]))
    donors.add_donor(Donor("Bill Gates", [200, 400, 750, 400]))
    donors.add_donor(Donor("John Smith Jr.", [200, 400, 9050.20, 30]))
    donors.add_donor(Donor("Jeff Bezos", [200, 225.50, 10000, 30]))
    return donors


def test_donor_create_donor_name():
    name = "Fred Flintstone"
    donor = Donor(name)
    assert donor.name == name


def test_donor_create_donor_name_and_donation():
    name, donations = "Fred Flintstone", (100, 3.50)

    donor = Donor(name, donations)
    assert donor.name == name
    assert donor.donations == donations


def test_donor_add_donation():
    name, donation = "Fred Flintstone", 500
    donor = Donor(name)
    donor.add_donation(donation)
    assert donor.num_donations == 1


def test_donor_add_donation_negative():
    name, donation = "Fred Flintstone", -500.00
    donor = Donor(name)
    with pytest.raises(TypeError):
        donor.add_donation(donation)


def test_donor_get_donor_name_key():
    name, key = "Bob Johnson Jr.", "bob_johnson_jr"
    assert Donor.getDonorNameKey(name) == key


def test_donor_get_name_key_from_instsance():
    name, key = "Bob Johnson Jr.", "bob_johnson_jr"
    donor = Donor(name)
    assert donor.key == key


def test_donor_last_donation():
    donor = Donor("Fred Flintstone")
    assert donor.last_donation is None
    donor.add_donation(500)
    assert donor.last_donation == 500
    donor.add_donation(55.30)
    assert donor.last_donation == 55.30


def test_donor_thank_you_text():
    donor = Donor("John Bon Jovi", [23.431])
    result = donor.get_thank_you_text()
    assert "Dear John Bon Jovi," in result
    assert "$23.43" in result
    assert "$23.431" not in result


def test_donor_donation_sum():
    donor = Donor("Steve Johnson", [100.00, 15, 30])
    assert donor.donation_sum() == float(145)


def test_donor_donation_average():
    donor = Donor("Steve Johnson", [100.00, 200, 400, 300])
    assert donor.donation_average() == float(250)


def test_donor_append_donations():
    donor = Donor("Steve Johnson", [100.00])
    donor += Donor("Steve Johnson", [123.21, 15.21])
    result = donor.donations
    assert len(result) == 3
    assert 123.21 in result
    assert 15.21 in result


def test_donor_equals():
    donor = Donor("Sean Carrol")
    assert donor == Donor("sean CarrOL")


def test_donor_not_equals():
    donor = Donor("Sean Carrol Jr.")
    assert donor != Donor("Sean Carrol")


# DonorCollection Tests
def test_donor_collection_add_donor():
    dc = DonorCollection()
    dc.add_donor(Donor("Bob"))
    assert dc["Bob"] == Donor("Bob")


def test_donor_collection_multiple():
    dc = DonorCollection()
    dc.add_donor(Donor("Bob"))
    dc.add_donor(Donor("Sean Carrol"))
    dc.add_donor(Donor("Peter Newhouse Jr."))
    assert dc["Bob"] == Donor("Bob")
    assert dc["Sean Carrol"] == Donor("sean CarrOL")
    assert dc["Peter Newhouse Jr."] == Donor("Peter NEWhouse Jr.")


def test_donor_collection_duplicates():
    dc = DonorCollection()
    dc.add_donor(Donor("Bob", (123.00,)))
    dc.add_donor(Donor("Bob", (456.00,)))
    dc.add_donor(Donor("Peter Newhouse Jr.", (7890,)))
    assert len(dc) == 2
    assert set(dc) == set([Donor("Bob"), Donor("Peter Newhouse Jr.")])
    assert dc["Bob"].donations == (123.00, 456.00)


def test_donor_collection_list_donors():
    dc = DonorCollection()
    dc.add_donor(Donor("Steve Johnson", [100.00, 200, 400, 300]))
    dc.add_donor(Donor("Cindy Johnson", [100.00, 200, 400, 300]))
    dc.add_donor(Donor("Beth Smith", [100.00, 200, 400, 300]))
    result = list(dc.list_donors())
    assert len(result) == 3
    assert "Cindy Johnson" in result


def test_donor_collection_contains():
    dc = setup_DonorCollection()
    name, fake_name = "Bill Gates", "Not A Name"
    donor = Donor(name)
    assert name in dc
    assert donor in dc
    assert fake_name not in dc
    assert Donor(fake_name) not in dc


def test_generate_report():
    dc = setup_DonorCollection()
    result = dc.generate_report()
    assert len(result) == len(dc) + 1
    assert len(result[0]) == 4


def test_all_thank_yous_to_files():
    dc = setup_DonorCollection()
    dir_path = pathlib.Path.cwd()
    dc.generate_donor_files(dir_path)
    for donor in dc:
        path = dir_path / donor.file_name
        assert os.path.exists(path)
        result = open(path, 'r').read()
        assert result == donor.get_thank_you_text()
