#!/usr/bin/env python

"""
Tim Pauley
Python 201a Assignment 06
Date: Nov 20 2018
"""

#MailRoom Part 4

import os

import MailRoomPart4 as mailroom

# so that it's there for the tests
mailroom.donor_db = mailroom.get_donor_db()



def test_list_donors():
    listing = mailroom.list_donors()
    assert listing.startswith("Donor list:\n")
    assert "Mark Zuckerberg" in listing
    assert "Paul Allen" in listing
    assert len(listing.split('\n')) == 5


def test_find_donor():
    """ checks a donor that is there, but with odd case and spaces"""
    donor = mailroom.find_donor("jefF beZos ")

    assert donor[0] == "Jeff Bezos"


def test_find_donor_not():
    "test to see if person is in db"
    donor = mailroom.find_donor("Paul Allan")

    assert donor is None


def test_gen_letter():
    donor = ("Jack White", [400.00, 50.05, 22.0])
    letter = mailroom.gen_letter(donor)
    assert letter.startswith("Hey Jack White")
    assert letter.endswith("-The Dream Team\n")
    assert "donation of $22.00" in letter


def test_add_donor():
    name = "Jack White  "
    donor = mailroom.add_donor(name)
    donor[1].append(300)
    assert donor[0] == "Jack White"
    assert donor[1] == [300]
    assert mailroom.find_donor(name) == donor


def test_generate_donor_report():

    report = mailroom.generate_donor_report()

    print(report)  

    assert report.startswith("Donor Name                | Total Given | Num Gifts | Average Gift")

    assert "Jeff Bezos                  $    877.33           1   $     877.33" in report


def test_save_letters_to_disk():


    mailroom.save_letters_to_disk()
    assert os.path.isfile('Paul_Allen.txt')
    assert os.path.isfile('Mark_Zuckerberg.txt')
    with open('Mark_Zuckerberg.txt') as f:
        size = len(f.read())
    assert size > 0


if __name__ == "__main__":
    test_list_donors()
    test_find_donor()
    test_find_donor_not()
    test_gen_letter()
    test_add_donor()
    test_generate_donor_report()
    test_save_letters_to_disk()
    print("Your tests all passed! Great Job!")