#!/usr/bin python3
"""
Test Mailroom version 4
"""
import pytest, os, pathlib
import mailroom as mr

def test_translate_donor_name_period():
    result = mr.translate_donor_name("Fake Name Jr.")
    assert result == "fake_name_jr"

def test_translate_donor_name_no_change():
    result = mr.translate_donor_name("bob")
    assert result == "bob"


def test_add_donation_single():
    key = "bob_smith_jr"
    mr.add_donation("Bob Smith Jr.", 200.15)
    assert key in mr.donors
    assert mr.donors[key].name == "Bob Smith Jr."
    assert mr.donors[key].amounts[0] == 200.15

def test_add_donation_double():
    key = "robert_smith_jr"
    mr.add_donation("Robert Smith Jr.", 200.15)
    mr.add_donation("Robert Smith Jr.", 15)
    assert key in mr.donors
    assert mr.donors[key].name == "Robert Smith Jr."
    assert mr.donors[key].amounts[0] == 200.15
    assert mr.donors[key].amounts[1] == 15

def test_add_donation_double_name_difference():
    key = "albert_smith_jr"
    mr.add_donation("Albert Smith Jr.", 200.15)
    mr.add_donation("albert smith Jr", 15)
    assert key in mr.donors
    assert mr.donors[key].name == "Albert Smith Jr."
    assert mr.donors[key].amounts[0] == 200.15
    assert mr.donors[key].amounts[1] == 15


def test_get_thank_you_text():
    result = mr.get_thank_you_text("John Bon Jovi", 23.431)
    assert "Dear John Bon Jovi," in result
    assert "$23.43" in result
    assert "$23.431" not in result


def test_get_report():
    result = mr.get_report()
    assert len(result) == len(mr.donors) + 2
    assert result[0].count('|') == 3


def test_get_thank_you_file_path():
    result = mr.get_thank_you_file_path("my_donor_name")
    assert result.name == "my_donor_name.txt"


def test_all_thank_yous_to_files():
    mr.all_thank_yous_to_files()
    for donor in mr.donors.items():
        path = mr.get_thank_you_file_path(donor[0])
        assert os.path.exists(path)
        result = open(path, 'r').read()
        assert result == mr.get_thank_you_text(donor[1].name, donor[1].amounts[-1])