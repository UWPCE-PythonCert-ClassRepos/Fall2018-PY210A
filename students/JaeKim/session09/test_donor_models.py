import os
from donor_models import Donor, DonorCollection, get_donordb


def test_donor_name():
    donor = Donor("Fred Flinstone")

    assert donor.name == "Fred Flinstone"


def test_add_donation():
    donor = Donor("Fred Flinstone")
    donor.add_donation(500)

    assert donor.num_donations == 1


def test_last_donation():
    donor = Donor("Fred Flinstone")
    donor.add_donation(1)
    donor.add_donation(2)
    donor.add_donation(3)

    assert donor.last_donation == 3


def test_average_donation():
    donor = Donor("Fred Flinstone")
    donor.add_donation(5)
    donor.add_donation(10)

    assert donor.average_donation == 7.5


def test_total_donation():
    donor = Donor("Fred Flinstone")
    donor.add_donation(5)
    donor.add_donation(10)

    assert donor.total_donation == 15


def test_dbdonor_find_donor():
    dbdonor = DonorCollection(get_donordb())
    results = dbdonor.find_donor("Dwyane Wade")

    assert results is True


def test_dbdonor_find_donor_invalid():
    dbdonor = DonorCollection(get_donordb())
    results = dbdonor.find_donor("Invalid Donor")

    assert results is False


def test_dbdonor_list_donors():
    dbdonor = DonorCollection(get_donordb())
    results = dbdonor.list_donors()

    assert "LeBron James" in results
    assert "Dwyane Wade" in results
    assert "Carmelo Anthony" in results


def test_dbdonor_make_report():
    dbdonor = DonorCollection(get_donordb())
    results = dbdonor.make_report()

    assert results.count("\n") == 4
    assert results.startswith("Donor Name") is True
    assert "LeBron James" in results
    assert "Dwyane Wade" in results
    assert "Carmelo Anthony" in results


def test_dbdonor_send_all_donors():
    dbdonor = DonorCollection(get_donordb())
    results = dbdonor.send_all_donors()

    assert results.count("Have a great day!") == 3
    assert "Hi LeBron James" in results
    assert "Hi Dwyane Wade" in results
    assert "Hi Carmelo Anthony" in results

def test_dbdonor_find_donor_false():
    dbdonor = DonorCollection(get_donordb())
    find_donor = dbdonor.find_donor("Jae Kim")

    assert find_donor is False

def test_dbdonor_add_donor():
    dbdonor = DonorCollection(get_donordb())
    dbdonor.add_donor(Donor("Jae Kim"))
    find_donor = dbdonor.find_donor("Jae Kim")

    assert find_donor is True
