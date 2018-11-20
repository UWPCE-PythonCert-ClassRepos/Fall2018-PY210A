#!/usr/bin/env Python3

import pytest
from textwrap import dedent

import Mailroom_4

from Mailroom_4 import exitout, makereport, add_Donor_Donation, assemble_thank_you, getDonation


def test_exitout():
    with pytest.raises(SystemExit):
        exitout()

def test_makereport():
    assert makereport(True) == [[653784.49, 'William Gates III', 2, 326892.24],
                                [16396.1, 'Mark Zuckerberg', 3, 5465.37],
                                [9063.02, 'John Galt', 3, 3021.01],
                                [877.33, 'Jeff Bezos', 1, 877.33],
                                [708.42, 'Paul Allen', 3, 236.14]]


def test_add_Donor_Donation():
    assert add_Donor_Donation('Susie Q', 33.00, True) == {"William Gates III": [653772.32, 12.17],
                                                          "Jeff Bezos": [877.33],
                                                          "Paul Allen": [663.23, 43.87, 1.32],
                                                          "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
                                                          "John Galt": [25.00, 9038.01, 0.01],
                                                          "Susie Q": [33.00]
                                                          }

def test_assemble_thank_you():
    result = assemble_thank_you("John Doe", 0.05)
    assert assemble_thank_you("John Doe", 0.05) == dedent(
        '''\tDear John Doe,
        Thank you for your generous donation of $0.05 to our cause.
        
        Sincerely,
        The Team''')

def test_getDonation():
    assert getDonation(2) == 2
