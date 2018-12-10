from mailroom import Donor
from mailroom import Donors
import statistics


def test_make_donor():
    donor = Donor("Fred Flinstone")
    assert donor.name == "Fred Flinstone"


def test_make_donor_with_donation():
    donor = Donor("Fred Flinstone", [100, 200, 300, 400])
    assert donor.name == "Fred Flinstone"
    assert donor.donation == [100, 200, 300, 400]


def test_add_donation():
    donor = Donor("Fred Flinstone")
    donor.add_donation(500)
    assert donor.donation == [
        500,
    ]


def test_append_donation():
    donor = Donor("Fred Flinstone")
    donor.add_donation(500, 365.00)
    assert donor.donation == [500, 365.00]
    donor.add_donation(1007)
    assert donor.donation == [500, 365.00, 1007]


def test_average():
    donor = Donor("Fred Flinstone")
    average = donor.make_average([500, 600, 800])
    assert average == statistics.mean([500, 600, 800])


def test_total():
    donor = Donor("Fred Flinstone")
    total = donor.make_total([100, 200, 300])
    assert total == sum([100, 200, 300])


def test_number_donations():
    donor = Donor("Fred Flinstone")
    number_of_donations = donor.num_donations([1, 2, 3, 4, 5])
    assert number_of_donations == 5


def test_thank_you():
    donor = Donor("Fred Flinstone")
    donations = [100, 200, 300]
    thanks = donor.make_thank_you(donations)
    assert thanks == 'Dear Fred Flinstone, Thank you for your donation of $600.00. These funds help save the migratory butterflies of New South East.Thank you'


def test_filename():
    donor = Donor("Fred Flinstone")
    filename = donor.make_filename()
    assert filename == 'Fred_Flinstone.txt'


def test_make_report_string():
    donor = Donor("Fred Flinstone")
    donation = [100, 200, 300, 400, 500]
    report_line = donor.make_report_string(donation)
    assert report_line == "Fred Flinstone       $1500.00         5               $300.00         "


def test_make_Donors():
    d1 = Donor("Fred Flinstone")
    d2 = Donor("James Dean")
    d3 = Donor("Jack the Ripper")
    donor_list = [d1, d2, d3]
    d_list = Donors(donor_list)
    assert d_list.donor_list[0].name == "Fred Flinstone"


def test_add_new_donor():
    d1 = Donor("Fred Flinstone")
    d2 = Donor("James Dean")
    d3 = Donor("Jack the Ripper")
    d_list = Donors([d1, d2, d3])
    d4 = Donor("Mickey Mouse")
    d_list.append(d4)
    assert d_list.donor_list[3].name == "Mickey Mouse"
    d_list.donor_list[3].add_donation(100)
    assert d_list.donor_list[3].donation == [
        100,
    ]


def test_make_check_Donors_attributes():
    d1 = Donor("Fred Flinstone", [100, 200, 300, 400])
    d2 = Donor("James Dean", [500, 600, 700, 800])
    d3 = Donor("Jack the Ripper", [1, 2, 3, 4])
    d_list = Donors([d1, d2, d3])
    assert d_list.donor_list[1].donation == [500, 600, 700, 800]


def test_list_donors():
    d1 = Donor("Fred Flinstone")
    d2 = Donor("James Dean")
    d3 = Donor("Jack the Ripper")
    d_list = Donors([d1, d2, d3])
    list_of_donors = d_list.list_donors()
    assert list_of_donors == [
        "Fred Flinstone", "James Dean", "Jack the Ripper"
    ]


def test_sort_donors():
    d1 = Donor("Fred Flinstone", [100, 200, 300, 400])
    d2 = Donor("James Dean", [500, 600, 700, 800])
    d3 = Donor("Jack the Ripper", [1, 2, 3, 4])
    d4 = Donor("Mickey Mouse")
    d_list = Donors([d1, d2, d3])
    d_list.sort_donors()
    list_of_donors = d_list.list_donors()
    assert list_of_donors == [
        "James Dean", "Fred Flinstone", "Jack the Ripper"
    ]
    d_list.append(d4)
    d_list.sort_donors()
    list_of_donors = d_list.list_donors()
    assert list_of_donors == [
        "James Dean", "Fred Flinstone", "Jack the Ripper","Mickey Mouse"]

def test_make_report():
    d1 = Donor("Fred Flinstone", [100, 200, 300, 400])
    d2 = Donor("James Dean", [500, 600, 700, 800])
    d3 = Donor("Jack the Ripper", [1, 2, 3, 4])
    d_list = Donors([d1, d2, d3])
    report = d_list.make_report()
    assert d_list.make_headers_string(
    ) == 'Donor Names          Total Given     Num Gifts       Average Gifts  '
    assert report.startswith('Donor')
    assert 'Fred Flinstone       $1000.00         4               $250.00' in report
    assert 'James Dean           $2600.00         4               $650.00' in report
    assert 'Jack the Ripper      $10.00           4               $2.50' in report
    assert report.endswith('\n')


def test_make_thank_strings():
    d1 = Donor("Fred Flinstone", [100, 200, 300, 400])
    d2 = Donor("James Dean", [500, 600, 700, 800])
    d3 = Donor("Jack the Ripper", [1, 2, 3, 4])
    d_list = Donors([d1, d2, d3])
    thank_notes = d_list.make_thank_notes()
    assert thank_notes == [
        'Dear Fred Flinstone, Thank you for your donation of $1000.00. These funds help save the migratory butterflies of New South East.Thank you',
        'Dear James Dean, Thank you for your donation of $2600.00. These funds help save the migratory butterflies of New South East.Thank you',
        'Dear Jack the Ripper, Thank you for your donation of $10.00. These funds help save the migratory butterflies of New South East.Thank you'
    ]

def test_find_donor():
    d1 = Donor("Fred Flinstone", [100, 200, 300, 400])
    d2 = Donor("James Dean", [500, 600, 700, 800])
    d3 = Donor("Jack the Ripper", [1, 2, 3, 4])
    d4 = Donor("Mickey Mouse", [100,200,300,5,15,7])
    d_list = Donors([d1, d2, d3, d4])
    donor_class=d_list.find_donor("Mickey Mouse")
    assert donor_class.donation==[100,200,300,5,15,7]
    donor_class=d_list.find_donor("")
    assert donor_class==[]
    
 def test_make_filenames():
    pass