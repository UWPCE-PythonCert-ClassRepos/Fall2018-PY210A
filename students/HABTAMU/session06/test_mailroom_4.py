#!/usr/bin/env python3

"""
unit tests for the mailroom program
"""
import os
import sys

import mailroom_4 as mailroom
    """
    Tests each functionwhether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
donors_info = mailroom.donors_info

def test_generates_letter(capsys):
    """ Test donors name and contribution in the template letter 
       and from readouterr() call snapshots the output and capture
       """
    mailroom.generates_letter("Bill Gates", 890093.93)
    captured = capsys.readouterr()
    assert "Bill Gates" in captured.out
    assert "$890,093.93" in captured.out


def test_create_report(capsys):
    # Test the content from the report as a table using readouterr
    mailroom.create_report()
    captured = capsys.readouterr()
    assert captured.out.startswith("Donor Name          | Total Given |  Num Gifts | Average Gift")
    assert "Warren Buffett        $16217.34        4          $4054.34" in captured.out


def test_save_letter_todisk():
    # Test each donors and contrubution from saved letter. 
    mailroom.save_letter_todisk()
    for donor, contribution in {"Bill Gates": "$16,500.00", "Paul Alen": "$10,600.00", "Mark Zuckerberg":"$42,082.11"}.items():
        with open(f"{donor.replace(' ', '_')}.txt", "r") as txt:
            content = txt.read()
            assert donor in content
            assert contribution in content

if __name__ == '__main__':
    test_generates_letter(capsys)
    test_create_report(capsys)
    test_save_letter_todisk()
