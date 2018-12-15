#testing

import glob
import pytest
from donor_models import *
from cli_main import donors

def test_create_donor():
    donor = Donor("Bill Clinton")

    assert donor.name == "Bill Clinton"

def test_add_donation():
    donor = Donor("Bill Clinton")

    donor.add_donation(500)

    assert donor.num_donations == 2
    assert donor.new_donation == 500

def test_donor_thank_you_data():
    donor = Donor("Ed")
    donor.add_donation(500)
    assert donor.thank_you_data == {'d_name': 'Ed', 'd_dollar': 500}


def test_donor_collection():
    dc = DonorCollection()
    d = Donor("Ed")
    d.add_donation(500)

    dc.add_old_donors(donors)
    dc.add_donor(d.name, d.donations)

    assert dc.list_donors == ['Javier Bardem', 'Pino Aprile', 'Oprah Winfrey', 'Peter Voss', 
                              'Luciano Pavarotti', 'Ed']

    """
    note, need to set computational digits to no more than 2 - otherwise assertion errors
    occur since division carries out digits to the 10th or 11th place - the difference in 
    digits throws the error

    """
    assert dc.report_data == [('Javier Bardem', 5800.00, 3, 1933.33),
                              ('Pino Aprile', 5750.00, 3, 1916.67),
                              ('Oprah Winfrey', 30000.00, 2, 15000.00),
                              ('Peter Voss', 4700.00, 3, 1566.67),
                              ('Luciano Pavarotti', 1600.00, 3, 533.33),
                              ('Ed', 500.00, 2, 250.00)]

    dc.send_thank_to_all()
    files = sorted(glob.glob("*.txt"))
    assert files == [k + '.txt' for k in sorted(dc.list_donors)]


