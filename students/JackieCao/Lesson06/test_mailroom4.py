#!/usr/bin/env python3
"""
test mailroom
"""
from mailroom4 import update_donors
from mailroom4 import print_thank_you_letter
from mailroom4 import return_donors_list
from mailroom4 import get_report
from mailroom4 import donors
from mailroom4 import get_letter_context
from mailroom4 import get_letter_name

def test_update_donors():
    donors = update_donors("Fred Jones", 600)
    assert donors["Fred Jones"] == [100, 200, 100, 600]
    donors = update_donors("Jane Toy", 100)
    assert donors["Jane Toy"] == [100]

def test_print_thank_you_letter():
    letter_text = print_thank_you_letter("Jane Toy", 800)
    assert letter_text == "Dear Jane Toy,\n\n    Thank you for your donation of $800.\n\nBest,\nDonation Group"

def test_return_donors_list():
    assert return_donors_list() == ["Fred Jones", "Bean Shing",
                                   "Ann Shaw", "King May", "Jane Toy"]
def test_get_letter_context():
    assert get_letter_context("King May") == "Dear King May,\n\n    Thank you for your donation of $600.\n\nBest,\nDonation Group"

def test_get_letter_name():
    assert get_letter_name("King May") == "King May.txt"

def test_get_report():
    data = [('Ann Shaw', 500, 2, 250.0), ('Bean Shing', 420, 2, 210.0), ('Fred Jones', 1000, 4, 250.0), ('Jane Toy', 100, 1, 100.0), ('King May', 600, 2, 300.0)]
    rows = "{:15s} | {:11s} | {:9s} | {:12s}".format(
            "Donor's Name", "Total Donated", "Number of Donations", "Average$")
    for row in data:
        a_row = "{:15s}   {:11.2f}   {:9d}   {:18.2f}".format(*row)
        rows = (rows + "\n" +  a_row)
    assert get_report() == rows

