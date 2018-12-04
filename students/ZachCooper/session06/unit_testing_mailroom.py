

"""Test for mailroom4"""
import os
import pytest
import mailroom4 as mr


def disney_donor_db():
    donor_name = ["Yosemite Sam", "Yogi Bear", "Daffey Duck",
                  "Wile E. Coyote", "Bugs Bunny", "Mickey Mouse"]
    donation = [[100.56, 200.23, 300], [2000.33, 4000, 1000],
                [5000.24, 10000.34, 30000], [300.40, 1000, 750.17],
                [100000.87, 50000, 100], [1345.67, 345.78, 1.23]]
    return dict(zip(donor_name, donation))


mr.donors = disney_donor_db()


def test_list_donors():
    listing = mr.list_donors()

    print(listing)
    assert listing.startswith("Donor List:\n")
    assert "Yosemite Sam" in listing
    assert "Wile E. Coyote" in listing
    assert len(listing.split('\n')) == 7


# Test to see if function properly return donors and donations
def test_donor_donations():
    result = mr.donor_donations()

    assert "Yosemite Sam", [100.56, 200.23, 300] in result


# Run the program and enter new donor data in test script
def test_adds_new_donor():
    mr.add_new_donor("Zach Cooper")

    assert "Zach Cooper" in mr.donors
    assert [] == mr.donors.get("Zach Cooper")


# Again enter test data from test script
def test_add_donation_to_donor():
    mr.add_donation_to_donor("Zach Cooper", 40)

    assert 40 in mr.donors.get("Zach Cooper")


# Test to see if content in letter passes
def test_send_letters():
    result = mr.send_letter("Yosemite Sam", 5000.00)

    assert result.startswith("Dear Yosemite Sam")


# Test to make sure donation is value is correct
def test_check_donation():
    with pytest.raises(ValueError):
        mr.check_donation(0)


# Check to see if negative value results in error
def test_check_negative_donation():
    with pytest.raises(ValueError):
        mr.check_donation(-123)


# Test to make sure donation value return float with 2 dec places
def test_check_donation_number_return():
    result = mr.check_donation("200.33")

    assert result == 200.33


# Test letter contents
def test_send_letter_contains_donation():
    result = mr.send_letter("Mickey Mouse", 500)

    assert "Thank you for your very kind donation of $500.00." in result

# Test donor report output
    """def test_donor_report():
    mr.donors = disney_donor_db()
    report = mr.donor_report()


    assert report.startswith("Donor Name                | Total Given | Num Gifts | Average Gift")
    assert "Yosemite Sam                  $    877.33           1   $     877.33" in report

    lines = report.split("\n")
    assert len(lines) == 7"""


def test_send_letters_to_disk():
    mr.send_letters_to_disk()

    for donor in disney_donor_db():
        donor = donor.replace(" ", "_") + ".txt"
        print(os.path.join(mr.OUT_PATH, donor))
        assert os.path.isfile(os.path.join(mr.OUT_PATH, donor))

# convert functino into file name
    # check that it's not empty:
    with open(os.path.join(mr.OUT_PATH, 'Daffey_Duck.txt')) as f:
        size = len(f.read())
    assert size > 0














