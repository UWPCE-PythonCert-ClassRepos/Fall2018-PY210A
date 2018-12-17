# test mailroom

import os
import sys
import pytest
from mailroom_oo.cli_main import CLI as cli
from mailroom_oo.donor_models import Donor as d
from mailroom_oo.donor_models import DonorCollection as dc
# import mailroom_oo.donor_models as dm
# import doctest

# from mailroom_oo.donor_models import DonorCollection


def test_donate():
    donor = d("Cho", 3000)
    donor.donate(700)
    assert donor.get_total_donation() == 3700


def test_get_total_donation():
    donor = d("Paul Alen", 3000)
    donor.donate(250)
    donor.donate(50)
    assert donor.get_total_donation() == 3300


def test_get_num_donations():
    donor = d("Jeff Benzo", 2300)
    assert donor.get_num_donations() == 1


def test_get_avarage_donation():
    donor = d("Mark Zuckerberg", 100)
    donor.donate(200)
    donor.donate(600)
    assert donor.get_avarage_donation() == 300


def test_add_donation():
    # dc().add_donation()

    dc().add_donation("Bill", 34)
    
    assert """
    Dear {Bill},

        Thank you for your generous donation $34.00

    Best regards,
    Your Youth and Seniors Foundation"""


def test_create_report():
    dc().create_report()
    
    assert """
    Donor Name          | Total Given |  Num Gifts | Average Gift
    ------------------------------------------------------------
    Bill Gates            $16500.00        3          $5500.00

    """

def test_save_letter_todisk():
    dc().save_letter_todisk()

    assert os.path.isfile('Bill_Gates.txt')
    assert os.path.isfile('Jeff_Benzo.txt')

    with open('Jeff_Benzo.txt') as f:
        size = len(f.read())
    assert size > 156


def test_list_donors():
    list_d = dc().list_donors()
    assert "Bill Gates\n- Paul Alen\n- Jeff Benzo\n- Mark Zuckerberg\n- Warren Buffett\n" in list_d


if __name__ == '__main__':
    test_donate()
    test_get_total_donation()
    test_get_num_donations()
    test_get_avarage_donation()
