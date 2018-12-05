"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
Mailroom Assignment - part 4 / session 06 - tests
"""


import os

import pytest

import mailroom_wk4dict as mailroom


"""
Best practice is to place donor data base in this test program instead 
of calling it from the main user program - this way test integrity is 
maintained, say in the event if the main user program is changed.

"""
mailroom.donor_db = mailroom.record_donor_db()


def test_donor_list():
    list_of_donors = mailroom.donor_list()
    
    assert list_of_donors.startswith("-- Donors --")
    assert "Javier Bardem" in list_of_donors
    assert "Luciano Pavarotti" in list_of_donors
    assert len(list_of_donors.split('\n'))  == 6


def test_find_donor():
    # tests for odd case and spaces in a donor's name
    donor = mailroom.find_donor("pIno aPrIle ")
    assert donor[0] == "Pino Aprile"



