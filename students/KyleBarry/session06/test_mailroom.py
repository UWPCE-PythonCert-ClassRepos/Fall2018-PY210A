import os
from mailroom_04 import Donor, DonorManager


def test_create_donor():
    donor = Donor("Tom")

    assert donor.name == "Tom"


def test_add_donation():
    donor = Donor("George")

    donor.add_donation(100)

    assert donor.num_donations == 1


def test_average_donation():
    donor = Donor("Jane")

    donor.add_donation(500)
    donor.add_donation(1000)
    donor.add_donation(9999)

    assert donor.average_donation == round(((500+1000+9999)/3), 2)


def test_total_donations():
    donor = Donor("Billie Joe")

    donor.add_donation(90200)
    donor.add_donation(78000)
    donor.add_donation(80)

    assert donor.total_donations == 90200 + 78000 + 80


def test_make_thank_you_file():
    donor = Donor("Sally")

    result = donor.make_thank_you_file()

    assert bool(open(result)) is True


def test_get_last_donation():
    donor = Donor("Mildred")

    donor.add_donation(9800)
    donor.add_donation(1000)

    assert donor.get_last_donation == 1000


def test_change_name():
    donor = Donor("Susie")

    donor.change_name("Terry")

    assert donor.name == "Terry"


def test_create_donor_manager():
    manager = DonorManager()

    assert bool(manager.donors) is True


def test_make_report():
    manager = DonorManager()

    result = manager.make_report()

    assert bool(open(result)) is True


def test_donor_manager_list():
    manager = DonorManager()

    assert len(manager.donors) > 0


def test_display_donor():
    manager = DonorManager()

    donor = Donor("Margie")

    result = manager.display_donor("Margie")

    assert result == manager.donors["Margie"]
