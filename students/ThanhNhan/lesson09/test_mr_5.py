import os
import pytest
from .mail5 import Donor, DonorCollection

donor_db = {"Tom Cruise": [233.23, 12.17],
            "Alyssa Nhan": [23., 23],
            "Jessy Apple, IIS": [33.0],
            "Jin Unknown": [12.0, 12.0]
            }

# Test object of the name
def test_donor_name():
    donor = Donor("Test ASdf")
    assert donor.name == "Test ASdf"

# Count how many time donation
def test_add_donation():
    donor = Donor("Fred Test")
    donor.add_donations(500)
    assert donor.num_donations == 1
    donor.add_donations(320)
    assert donor.num_donations == 2

#Test dollar amount input
def test_ck_char_input():
    donor = Donor("Fred Test")
  
    with pytest.raises(ValueError):
        donor.add_donations(0.001)

    with pytest.raises(ValueError):
        donor.add_donations("asd")

    with pytest.raises(ValueError):
        donor.add_donations(-50)

    with pytest.raises(ValueError):
        donor.add_donations(0.0)


# Validate Name Input
def test_validate_name():
    name1 = Donor(" ")
    assert name1.validate_name() is False

    name2 = Donor("23")
    assert name2.validate_name() is False

    name3 = Donor("asd2a adf3")
    assert name3.validate_name() is False

    name4 = Donor("3ass3 12sdf")
    assert name4.validate_name() is False

    name5 = Donor("Tom Asd")
    assert name5.validate_name() is True

    name6 = Donor("Tom")
    assert name6.validate_name() is False

    name7 = Donor("Tom ")
    assert name7.validate_name() is False

    name8 = Donor("Tom Asd III")
    assert name8.validate_name() is True

    name9 = Donor("Tom Asdasfasf, III")
    assert name9.validate_name() is True

    name10 = Donor("Tom Asdasfasf ")
    assert name10.validate_name() is True


def test_donor_thank_you_Letter():
    donor = Donor("Tom Tom")
    donor.add_donations(2432)
    assert donor.generate_letter(donor.donations) == """
            Dear {},
            Thank you  for your very kind donation of ${:.2f}
            It will be put to very good use.

                            Sincerely,
                            - The Team   
	        """.format("Tom Tom", 2432.00)



def test_DonorCollection():
    donor = DonorCollection(donor_db)
    assert donor.data_collection == {"Tom Cruise": [233.23, 12.17],
                                    "Alyssa Nhan": [23., 23],
                                    "Jessy Apple, IIS": [33.0],
                                    "Jin Unknown": [12.0, 12.0]
                                    }
    
def test_exist_list():
    donor = DonorCollection(donor_db)
    assert donor.exist_list() == ["Tom Cruise", "Alyssa Nhan", "Jessy Apple, IIS", "Jin Unknown"]

def test_lookup_name():
    donor = DonorCollection(donor_db, "Test As")
    assert donor.find_donor() is False
    donor = DonorCollection(donor_db, "Tom Cruise")
    assert donor.find_donor() is True


def test_display_report():
    donor = DonorCollection(donor_db)
    assert donor.create_report() == [["Jessy Apple, IIS", 33.00, 1, 33.00],
                                        ["Tom Cruise", 245.40, 2, 122.70],
                                        ["Alyssa Nhan", 46.00, 2, 23.00],
                                        ["Jin Unknown", 24.00, 2, 12.00],]

def test_sort():
    row = ["Jessy Apple", 33.00, 1, 33.00]
    assert DonorCollection._sort(row) == "Apple"

def test_sort2():
    row = ["Jessy H Apple", 33.00, 1, 33.00]
    assert DonorCollection._sort(row) == "Apple"
  
def test_sort3():
    row = ["Jessy Apple, IIS", 33.00, 1, 33.00]
    assert DonorCollection._sort(row) == "Apple,"

def test_check_directory_default():
    direct = DonorCollection(donor_db)
    print("Please make sure directory (D_letter) is create to pass this condition")
    assert direct.ck_dir() is True

def test_save_letters():
    save_letter = DonorCollection(donor_db)
    save_letter.ss_letterall()
    assert os.path.isfile("D_letter/Jessy Apple, IIS.txt")
    assert os.path.isfile("D_letter/Tom Cruise.txt")
    assert os.path.isfile("D_letter/Alyssa Nhan.txt")
    assert os.path.isfile("D_letter/Jin Unknown.txt")

def test_add_donor_db():
    
    dn = Donor("Tom Nhan")
    dn.add_donations(200)
    dn_db = DonorCollection(donor_db, dn.name)
    dn_db.add_donor(dn)
    assert dn_db.data_collection["Tom Nhan"] == [200]

    dn = Donor("Jin Unknown")
    dn.add_donations(423)
    dn_db = DonorCollection(donor_db, dn.name)
    dn_db.add_donor(dn)
    assert dn_db.data_collection["Jin Unknown"] == [12.0, 12.0, 423.0]

    
    

    # donor.add_donation(300)
    # assert donor.name == "Fred Flintstone"
    # assert donor.last_donation == 300
    # assert sample_db.find_donor(name) is donor

    # dc = DonorCollection(donor_db, "Tom Nhan")

    # assert dc.add_donor("Tom Nhan").append()

    # if donor.find_donor is True:
    #     donor.add_donations(2.32)
    # else:
    #     donor.add_donations
    # donor.add_donor(donor.name)





#     dc.thank_donors()

#     dc.create_report()
