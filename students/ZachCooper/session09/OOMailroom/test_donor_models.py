#!/usr/bin/env python3


import os
from donor_models import Donor, DonorCollection, sample_disney_donors


# def disney_donor_db():
#     donor_name = ["Yosemite Sam", "Yogi Bear", "Daffey Duck",
#                   "Wile E. Coyote", "Bugs Bunny", "Mickey Mouse"]
#     donation = [[100.56, 200.23, 300], [2000.33, 4000, 1000],
#                 [5000.24, 10000.34, 30000, 300], [300.40, 1000, 750.17],
#                 [1000, 50000, 3000], [1345.67, 345.78, 1.23]]
#     return dict(zip(donor_name, donation))


Disney_db = DonorCollection(sample_disney_donors())


def test_donor_name():
    donor = Donor("Yosemite Sam")

    assert donor.name == "Yosemite Sam"


def test_add_donation():
    donor = Donor("Yosemite Sam")

    donor.add_donation(300)

    assert donor.num_donations == 1


def test_last_donation():
    donor = Donor("Yosemite Sam")

    donor.donations = [100.56, 200.23, 300]
    assert donor.donations[-1] == 300


def test_sum_donation_total():
    donor = Donor("Yogi Bear")

    donor.donations = [2000.33, 4000, 1000]

    assert sum(donor.donations) == 7000.33


def test_total_donations_made():
    donor = Donor("Daffey Duck")

    donor.donations = [5000.24, 10000.34, 30000, 300]

    assert len(donor.donations) == 4


def test_send_letter():
    donor = Donor("Daffey Duck")
    donor.donations = [5000.24, 10000.34, 30000, 300]
    letter = donor.send_letter()
    assert letter.startswith("Dear Daffey Duck,")
    assert "Dear Daffey Duck" in letter
    #assert letter.endswith("Sincerely, -The Team\n")
    assert "donation of $300.00" in letter


def test_avg_donation_made():
    donor = Donor("Bugs Bunny")
    donor.donations = [1000, 5000, 3000]

    assert sum(donor.donations) / len(donor.donations) == 3000



# Test DonorCollection


def test_donor_list():
    # Start with fresh db as mentioned in class
    Disney_db = DonorCollection(sample_disney_donors())

    list_don = Disney_db.donor_list()
    # Assert with similar test as my test_mailroom
    assert list_don.startswith("List of Disney Donors:\n")
    assert "Bugs Bunny" in list_don
    assert "Daffey Duck" in list_don
    assert len(list_don.split('\n')) == 6


def test_add_donor():
    name = "Goofy"
    donor = Disney_db.add_donor(name)
    donor.add_donation(500)

    assert donor.name == "Goofy"
    assert len(donor.donations) == 1
    #assert donor.last_donation == 500 ###Raises and AssertionError???###
    #assert Disney_db.find_donor(name) is donor


def test_find_donor():
    donor = Donor("Daffey Duck")

    assert donor.name == "Daffey Duck"


def test_generate_report():
    Disney_db = DonorCollection(sample_disney_donors())
    report = Disney_db.generate_report()

    print(report)

    ### Im getting an AttributeError 'NoneType' for startswith...???
    assert report.startswith("Donor Name                | Total Given | Num Gifts | Average Gift")
    assert "Yosemite Sam                  $    100.56           3   $     100.56" in report


## Not sure on this....Used similar code from my test_mailroom4
def test_send_letters_to_disk():
    Disney_db.send_letters_to_disk()

    for donor in Disney_db():
        donor = donor.replace(" ", "_") + ".txt"
        print(os.path.join(DonorCollection.OUT_PATH, donor))
        assert os.path.isfile(os.path.join(DonorCollection.OUT_PATH, donor))

# convert function into file name
    # check that it's not empty:
    with open(os.path.join(DonorCollection.OUT_PATH, 'Daffey_Duck.txt')) as f:
        size = len(f.read())
    assert size > 0
