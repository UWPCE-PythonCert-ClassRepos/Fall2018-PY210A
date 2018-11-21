# Unit tests for Mailroom, Part 4

# Import modules
import datetime
import os
import mailroom_four as mr


# Initial donor database
def reset_donor_database():
    donors = {"Jimmy Fallon": [500.00, 700.00], "Taylor Swift": [1000.00], "Dan White": [200.00, 300.00, 400.00],
              "Trevor Noah": [750.00, 850.00], "Elon Musk": [3000.00], "Selena Gomez": [100.00, 150.00, 200.00]}
    return donors


# List existing donors
def test_existing_donors():
    mr.donors = reset_donor_database()
    existing = mr.existing_donors()
    assert existing == ["Jimmy Fallon", "Taylor Swift", "Dan White", "Trevor Noah", "Elon Musk", "Selena Gomez"]


# Validate donor name
def test_check_name_empty():
    name1 = mr.check_name("")
    assert name1 is False


def test_check_name_num():
    name2 = mr.check_name("4")
    assert name2 is False


def test_check_name_exit():
    name3 = mr.check_name("E")
    assert name3 is None


def test_check_name_list():
    name4 = mr.check_name("L")
    assert name4 is False


def test_check_name_correct():
    name5 = mr.check_name("Dianna Tingg")
    assert name5 is True


# Verify donation amount
def test_check_donation_long():
    donation1 = mr.check_donation("etc")
    assert donation1 is None


def test_check_donation_correct():
    donation2 = mr.check_donation("500")
    assert donation2 is True


def test_check_donation_small():
    donation3 = mr.check_donation(".001")
    assert donation3 is False


def test_check_donation_wrong():
    donation4 = mr.check_donation("x")
    assert donation4 is False


# Add donor/donation to dictionary
def test_add_donation_new():
    mr.donors = reset_donor_database()
    mr.add_donation("Dianna Tingg", 500.00)
    assert mr.donors["Dianna Tingg"] == [500.00]


def test_add_donation_existing():
    mr.donors = reset_donor_database()
    mr.add_donation("Elon Musk", 1000.00)
    assert mr.donors["Elon Musk"] == [3000.00, 1000.00]


# Generate thank you letter
def test_thank_you_letter():
    letter1 = mr.thank_you_letter("Ariana Grande", 200.00)
    assert letter1 == "{}\n\nDear Ariana Grande:\n\nThank you so much for the generous donation of $200.00.\n" \
                      "We will use the money to provide tiny cars to clowns in need.\n\nBest regards,\nDianna Tingg\n" \
                      "Tiny Clown Car Foundation".format(datetime.datetime.now().strftime("%B %d, %Y"))


# Check directory
def test_check_directory_default():
    directory = mr.check_directory("")
    assert directory is True


# Create/save thank you letters for all donors
def test_save_letters():
    mr.save_letters("")
    date = datetime.datetime.now().strftime("%m-%d-%Y")
    assert os.path.isfile("Jimmy Fallon {}.txt".format(date))
    assert os.path.isfile("Taylor Swift {}.txt".format(date))
    assert os.path.isfile("Dan White {}.txt".format(date))
    assert os.path.isfile("Trevor Noah {}.txt".format(date))
    assert os.path.isfile("Elon Musk {}.txt".format(date))
    assert os.path.isfile("Selena Gomez {}.txt".format(date))


# Create a report
def test_create_report():
    mr.donors = reset_donor_database()
    data = mr.create_report()

    assert data == [["Elon Musk", 3000.00, 1, 3000.00],
                    ["Trevor Noah", 1600.00, 2, 800.00],
                    ["Jimmy Fallon", 1200.00, 2, 600.00],
                    ["Taylor Swift", 1000.00, 1, 1000.00],
                    ["Dan White", 900.00, 3, 300.00],
                    ["Selena Gomez", 450.00, 3, 150.00]]
