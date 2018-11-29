#!/usr/bin/env python

"""
unit tests for the mailroom program
"""
import os

import pytest

import mailroom2 as mailroom

# so that it's there for the tests
# you may want to re-run this in a test that requires a
# "clean" database
mailroom.donor_db = mailroom.get_donor_db()


def test_list_donors():
    listing = mailroom.list_donors()

    # hard to test this throughly -- better not to hard code the entire
    # thing. But check for a few aspects -- this will catch the likely
    # errors
    assert listing.startswith("Donor list:\n")
    assert "Jeff Bezos" in listing
    assert "William Gates III" in listing
    assert len(listing.split('\n')) == 5


def test_find_donor():
    """ checks a donor that is there, but with odd case and spaces"""
    donor = mailroom.find_donor("jefF beZos ")

    assert donor[0] == "Jeff Bezos"


def test_find_donor_not():
    "test one that's not there"
    donor = mailroom.find_donor("Jeff Bzos")

    assert donor is None


def test_gen_letter():
    """ test the donor letter """

    # create a sample donor
    donor = ("Fred Flintstone", [432.45, 65.45, 230.0])
    letter = mailroom.gen_letter(donor)
    # what to test? tricky!
    assert letter.startswith("Dear Fred Flintstone")
    assert letter.endswith("-The Team\n")
    assert "donation of $230.00" in letter


def test_add_donor():
    name = "Fred Flintstone  "

    donor = mailroom.add_donor(name)
    donor[1].append(300)
    assert donor[0] == "Fred Flintstone"
    assert donor[1] == [300]
    assert mailroom.find_donor(name) == donor


def test_generate_donor_report():

    # make sure the the database is "clean"
    mailroom.donor_db = mailroom.get_donor_db()
    report = mailroom.generate_donor_report()

    print(report)  # printing so you can see it if it fails
    # this is pretty tough to test
    # these are not great, because they will fail if unimportant parts of the
    # report are changed.
    # but at least you know that code is working now.
    assert report.startswith("Donor Name                | Total Given | Num Gifts | Average Gift")

    assert "Jeff Bezos                  $    877.33           1   $     877.33" in report

    lines = report.split("\n")
    assert len(lines) == 6


def test_save_letters_to_disk():
    """
    This only tests that the files get created, but that's a start

    Note that the contents of the letter was already
    tested with test_gen_letter
    """

    mailroom.save_letters_to_disk()

    assert os.path.isfile('Jeff_Bezos.txt')
    assert os.path.isfile('William_Gates_III.txt')
    # check that it's not empty:
    with open('William_Gates_III.txt') as f:
        size = len(f.read())
    assert size > 0


def test_validate_donation_good():
    result = mailroom.validate_donation("500")

    assert result == 500.0


def test_validate_donation_notnum():
    with pytest.raises(ValueError):
        mailroom.validate_donation("some junk")


def test_validate_donation_negative():
    with pytest.raises(ValueError):
        mailroom.validate_donation("-100")


def test_validate_donation_nan():
    with pytest.raises(ValueError):
        mailroom.validate_donation("NaN")


def test_validate_donation_tiny():
    with pytest.raises(ValueError):
        mailroom.validate_donation("0.00000001")


if __name__ == "__main__":
    # this is best run with a test runner, like pytest
    # But if not, at least this will run them all.
    test_list_donors()
    test_find_donor()
    test_find_donor_not()
    test_gen_letter()
    test_add_donor()
    test_generate_donor_report()
    test_save_letters_to_disk()
    print("All tests Passed")
