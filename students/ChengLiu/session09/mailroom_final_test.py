#!/usr/bin/env python3

"""
Cheng Liu
Mail-room Final
"""

import os
import pytest
import mailroom_final


def test_default_donor():
    assert donors['Test Default'] == ("Test Default", [1, 2, 3])


def test_add_donor():
    donor = Donor("Kobe Br")
    assert donor.name == "Kobe Br"
    assert donor.last_donation is None


def test_add_donation():
    donor.add_donation(100)


    assert donor.last_donation == 100


def test_list_donors():
    assert "Default Test1" in Donor.list_donors()


def test_find_donors():
    test_donor = Donor.find_donors('default test3')
    assert test_donor is None


def test_letter():
    donor = Donor("Jeff Bzo", [100.10, 50.50])
    donor_letter = donor.letter(donor)
    assert "Jeff Bzo" in donor_letter
    assert "$50.50" in donor_letter


def test_report():
    assert "Jeff Bzo" in report
