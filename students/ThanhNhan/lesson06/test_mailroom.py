#!/usr/bin/env python
import mailroom4 as mr4
import os

"""
Send a thank you (adds a new donor or updates existing donor info)
Create a report
Send letters (creates files)
Your unit tests should test the data manipulation logic code: generating thank you text, adding or updating donors, and listing donors.
Send a thank you (adds a new donor or updates existing donor info)
"""
def test_existing_donor():

    new_donor = {"Tom Cruise": [233.23, 12.17],
             "Alyssa Nhan": [23., 23],
             "Jessy Test": [33.0],
             "Jin Unknown": [12.0, 12.0]
             }
    mr4.donor_dict = new_donor
    new_donor_db = mr4.chk_exist_donor()
    assert new_donor_db == ["Tom Cruise", "Alyssa Nhan", "Jessy Test", "Jin Unknown"]


# Validate Name Input
def test_validate_name():
    name1 = mr4.validate_name(" ")
    assert name1 is False

    name2 = mr4.validate_name("23")
    assert name2 is False

    name3 = mr4.validate_name("asd2a adf3")
    assert name3 is False

    name4 = mr4.validate_name("3ass3 12sdf")
    assert name4 is False

    name5 = mr4.validate_name("Tom Asd")
    assert name5 is True

    name6 = mr4.validate_name("Tom")
    assert name6 is False

    name7 = mr4.validate_name("Tom ")
    assert name7 is False

    name8 = mr4.validate_name("Tom Asd III")
    assert name8 is True

    name9 = mr4.validate_name("Tom Asdasfasf, III")
    assert name9 is True

# Test for lookup Name
def test_lookup_name():
    name1 = mr4.lookup_name("Alyssa Nhan")
    assert name1 == "Alyssa Nhan"

    name2 = mr4.lookup_name("Thanh Inte")
    assert name2 is None

#Test dollar amount input
def test_ck_char_input():
    donate1 = mr4.ck_dollar("xasdf")
    assert donate1 is False
def test_ck_integer():
    donate2 = mr4.ck_dollar("500")
    assert donate2 is True
def test_ck_longfloat():
    donate3 = mr4.ck_dollar("0.001")
    assert donate3 is False
def test_ck_string():
    donate4 = mr4.ck_dollar("asd")
    assert donate4 is False
def test_ck_pt2float():
    donate4 = mr4.ck_dollar("0.23")
    assert donate4 is True

#Test for donation add
def test_existing_donation():
    mr4.add_donation("Alyssa Nhan", "Alyssa Nhan", 2.32)
    assert mr4.donor_dict["Alyssa Nhan"] == [23., 23, 2.32]

def test_new_donation():
    mr4.add_donation(None,  "Tom Asdf", 1324.23)
    assert mr4.donor_dict["Tom Asdf"] == [1324.23]

#Test Thank you Letter
def test_single_letter():
    letter1 = mr4.create_letter("Tom Tom", 3240.00)
    assert letter1 == """
            Dear {},
            Thank you  for your very kind donation of ${:.2f}
            It will be put to very good use.

                            Sincerely,
                            - The Team   
	        """.format("Tom Tom", 3240.00)

#Check Directorys
def test_check_directory_default():
    direct = mr4.ck_dir()
    print("Please make sure directory (D_letter) is create to pass this condition")
    assert direct is True

#Test Create Report
# def test_create_report():
    data = mr4.create_report()
    print(data)
    assert data == [["Tom Cruise", 245.40, 2, 122.70],
                    ["Alyssa Nhan", 48.32, 3, 16.11],
                    ["Jessy Test", 33.00, 1, 33.00],
                    ["Jin Unknown", 24.00, 2, 12.00],
                    ["Tom Asdf", 1324.23, 1, 1324.23],]
 

#  # Create/save thank you letters for all donors
def test_save_letters():
    mr4.ss_letterall()
    assert os.path.isfile("D_letter/Tom Asdf.txt")
    assert os.path.isfile("D_letter/Tom Cruise.txt")
    assert os.path.isfile("D_letter/Alyssa Nhan.txt")
    assert os.path.isfile("D_letter/Jessy Test.txt")
    assert os.path.isfile("D_letter/Jin Unknown.txt")
  
