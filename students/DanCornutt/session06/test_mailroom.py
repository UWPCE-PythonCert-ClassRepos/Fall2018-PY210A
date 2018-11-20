#!/usr/bin/env python

import os
import pytest
from mailroom import *


def test_check_donor_1():
    """Finds donor in list"""
    assert check_donor("Billy Bills") is True

def test_check_donor_2():
    """Does not find donor in list"""
    assert check_donor("Billy Billz") is False

def test_gen_letter_1():
    """Generates valid letter for donor in list"""
    assert gen_letter("Billy Bills") == """Dearest Billy Bills,

    We greatly thank you for your recent contribution of $300.00.

    It will go straight to the person who needs it the most, our CEO.

    Please give more next time.

    	Love,

    		The Team"""

def test_gen_letter_1():
    """Does not generate valid letter for donor not in list"""
    with pytest.raises(KeyError):
        gen_letter("Billy Billz") != """Dearest Billy Billz,

    We greatly thank you for your recent contribution of $300.00.

    It will go straight to the person who needs it the most, our CEO.

    Please give more next time.

    	Love,

    		The Team"""

def test_write_donor(): #Tests if file has been created in directory
    write_donor("Billy Bills")
    assert os.path.exists("BillyBills_thank_you.txt") is True
    #remove files
    os.remove("BillyBills_thank_you.txt")

def test_thank_you_1():
    #all_users=True is validated by test_write_donor
    #not sure how to test else case for user input in pytest or
    #printing to screen. Function could be refactored and return something if
    #2nd else is called
    pass


def test_donor_db(): #not sure how to test for user input in pytest.
    pass

def test_edit_donor():
    #TODO Should be refactored to test for non-valid donor name i.e. " "
    #Could return value to test
    pass

def test_add_donation():
    #TODO Should be refactored to return string vs print to screen.
    pass

def test_add_money():
    #not sure how to test for user input in pytest.
    pass

def test_thank_you_all():
    #assert thank_you_all() == all letters were created in directory
    write_donor("Billy Bills")
    assert os.path.exists("BillyBills_thank_you.txt") is True
    write_donor("Fred Jones")
    assert os.path.exists("FredJones_thank_you.txt") is True
    write_donor("Amy Shumer")
    assert os.path.exists("AmyShumer_thank_you.txt") is True
    write_donor("Bob Sherlock")
    assert os.path.exists("BobSherlock_thank_you.txt") is True
    write_donor("Tom Johnson")
    assert os.path.exists("TomJohnson_thank_you.txt") is True
    #remove files
    os.remove("BillyBills_thank_you.txt")
    os.remove("FredJones_thank_you.txt")
    os.remove("AmyShumer_thank_you.txt")
    os.remove("BobSherlock_thank_you.txt")
    os.remove("TomJohnson_thank_you.txt")


def test_report():
    assert report() == ("Donor Name   | Total Given | Num Gifts |Average Gift      \n" +
"--------------------------------------------------\n" +
"Billy Bills  |$  21,760.55 |         3 |$ 7,253.52          \n" +
"Amy Shumer   |$   7,000.00 |         3 |$ 2,333.33          \n" +
"Tom Johnson  |$   1,200.00 |         3 |$ 400.00            \n" +
"Fred Jones   |$     600.01 |         3 |$ 200.00            \n" +
"Bob Sherlock |$      60.00 |         3 |$ 20.00             ")

def test_make_report():
    #Simple call report() and prints to screen, unit test not needed.
    pass

def test_return_total():
    """Returns second element in list"""
    lst = ["one", "two"]
    assert return_total(lst) == "two"

def test_donor_list():
    #Simple print donor list to screen. Unit test not needed.
    pass

def test_unknown():
    #Simple print to screen. Unit test not needed.
    pass

def test_quit_menu():
    """Tests quit menu command operational"""
    assert quit_menu() == "exit menu"

def test_menu_selection():
    #Unit testing with user input, unknown how to test
    pass
