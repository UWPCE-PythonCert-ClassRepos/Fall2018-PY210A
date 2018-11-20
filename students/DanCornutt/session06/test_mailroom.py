#!/usr/bin/env python

from mailroom import *
import pytest

def test_check_donor_1():
    """Finds donor in list"""
    assert check_donor("Billy Bills") == True

def test_check_donor_2():
    """Does not find donor in list"""
    assert check_donor("Billy Billz") == False

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
    pass

def test_thank_you_1(): #Function should be refactored to be tested easier
    pass

def test_donor_db(): #testing user input
    pass

def test_edit_donor():
    #Should be refactored to test for non-valid donor name i.e. " "
    #Should return value to test
    pass

def test_add_donation():
    #Should be refactored to return string vs print to screen.
    #
    pass

def test_add_money():
    #not sure how to test for user input for pytest...
    pass

def test_thank_you_all():
    #assert thank_you_all() == all letters were created in directory
    pass

def test_report():
    assert report() == ("Donor Name   | Total Given | Num Gifts |Average Gift      \n" +
"--------------------------------------------------\n" +
"Billy Bills  |$  21,760.55 |         3 |$ 7,253.52          \n" +
"Amy Shumer   |$   7,000.00 |         3 |$ 2,333.33          \n" +
"Tom Johnson  |$   1,200.00 |         3 |$ 400.00            \n" +
"Fred Jones   |$     600.01 |         3 |$ 200.00            \n" +
"Bob Sherlock |$      60.00 |         3 |$ 20.00             ")

def test_make_report():
    #calls report() and prints to screen, unit test not needed.
    pass

def test_return_total():
    """Returns second element in list"""
    lst = ["one", "two"]
    assert return_total(lst) == "two"

def test_donor_list():
    #prints donor list to screen. Unit test not needed.
    pass

def test_unknown():
    pass

def test_quit_menu():
    pass

def test_menu_selection():
    pass
