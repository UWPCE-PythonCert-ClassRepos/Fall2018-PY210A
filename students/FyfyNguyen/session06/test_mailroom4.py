#!/usr/bin/env python3

"""
Mailroom 4 tests
"""

import pytest
import os
import pathlib
import mailroom4 as mr


def test_print_donors():
    listing = mr.print_donors()
    assert "Robyn Rihanna" in listing
    assert "Aubrey Drake Graham" in listing


def test_find_donor():
    donor = mr.find_donor("beyonce caRter Knowles ")
    assert donor[0] == "Beyonce Carter Knowles"


def test_if_not_find_donor():
    donor = mr.find_donor("Beyonce Carter Knowles")
    assert donor is None


def test_add_new_donor():
    name = " Jennifer Lopez"
    donor = mr.add_new_donor(name)
    donor[1].append(750)
    assert donor[0] == "Jennifer Lopez"
    assert donor[1] == [750]
    assert mailroom.find_donor(name) == donor


def test_create_report():
    result = mr.create_report()
    assert result.startswith("Donor Name                     | Total Given | Num Gifts | Average Gift")
    assert "------------------------------------------------------------------------" in result
    assert "Ariana Grande                  |           3 |         3 | $    2,416.67" in result


def test_thank_you():
    result = mr.thank_you("Chrissy Teigen", 4500)
    assert "Dear Chrissy Teigen," in result
    assert "$4,500.00" in result
    assert "4500" not in result


def test_thank_you_all():
    result = mr.thank_you_all("Fyfy Nguyen")
    assert result.name == "Fyfy_Nguyen.txt"


def test_thank_you_all_files():
    mr.thank_you_all()
    for donor in mr.donor_db.items():
        file_path = mr.thank_you_all
