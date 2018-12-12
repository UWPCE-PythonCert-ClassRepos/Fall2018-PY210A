#!/usr/bin/env python3
import os
import mailroom_4 as m4

# Test Data Structure list
def test_data_structure():
    for name, donation in m4.DATA_STRUCTURE:
        print(name, donation)
        assert isinstance(name, str)
        assert isinstance(donation, list)
# Test Data Structure Dictionary
def test_data_structure_dicts():
    for entry in m4.DATA_STRUCTURE_DICTS:
        print(entry['name'], entry['donation'])
        assert isinstance(entry['name'], str)
        assert isinstance(entry['donation'], list)
# Test Sending a Thank You
def test_new_thank_you():
    new_thank_you = m4.thank_you(full_name='Kristian Francisco', donation_amount=100)
    assert 'Kristian Francisco' in new_thank_you
    assert '100' in new_thank_you

def test_exist_thank_you():
    new_thank_you = m4.thank_you(full_name='Jeff Bezos', donation_amount=51512)
    assert 'Jeff Bezos' in new_thank_you
    assert '51512' in new_thank_you
# Test Listing Donors
def test_list_donors():
    test_donors = m4.list_donors()
    ('Jeff_Bezos' and 'Bill Gates' and 'Steve Jobs') in test_donors
# Test Creating A Report
def test_create_a_report():
    report = m4.create_a_report()
    for name, donation in m4.DATA_STRUCTURE:
        assert name in report
        assert str(sum(donation)) in report
        assert str(len(donation)) in report
        #assert str(sum(donation) / len(donation)) in report
# Test Sending Letters to Everyone
def test_send_letters():
    files = m4.send_letters()
    dsk_files = os.listdir()
    #for file in files:
    for file in files:
        assert file in dsk_files