#!/usr/bin/env Python3


######
#Created by: Carol Farris
#Name: test_OO_Mailroom.Python.py
#Purpose: Create an object oriented Mailroom
#Progress:
#Mostly done with Donor class. Now fill out and test Donor Collection
#####

from OO_Mailroom import *
# .donor_Models for the donors in test_donor_models

#for CLI
#from donor_models import Donor, DonorCollection, any other...


donor_mock2 = [Donor("William Gates III", [653772.32, 12.17]),
              Donor("Jeff Bezos", [877.33]),
              Donor("Paul Allen", [663.23, 43.87, 1.32]),
              Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
              Donor("John Galt", [25.00, 9038.01, 0.01])]                        


#######################Test Donor Class################


def test_donor_name():
    donor = Donor("A Person")

    assert donor.name == "A Person"


def test_add_donation():
    """Tests you can add a donation from multiple donors"""
    donor = Donor("Yo Mama")
    donor.add_donation(500)
    donor.add_donation(200)
    print('donor.donations[0]', donor.donations[0])
    assert donor.donations[0] == 500
    assert donor.num_donations == 2


def test_add_donation_checks():
    """tests that add_donation cheks donation values are numeric and greater than a penny"""
    donor = Donor("Yo Mama")
    donor.add_donation(200)
    donor.add_donation(500)
    
    assert donor.add_donation("apple") == "Donation value must be entirely numeric!"
    assert donor.add_donation(0.0003) == "Donation cannot be smaller than a penny!"
    assert donor.donations[1] == 500
    assert donor.num_donations == 2


def test_get_sum_of_donations():
    donor = Donor("Pippy Longstocking")
    donor.add_donation(25)
    donor.add_donation(300)
    donor.add_donation(500)

    assert donor.sum_donations() == 825


def test_get_last_donation():
    donor = Donor("Pippy Longstocking", 10)
    donor.add_donation(25)
    donor.add_donation(300)
    donor.add_donation(500)

    assert donor.get_last_donation() == 500

def test_sum_thank_your_letter():
    """Returns a thank you letter that defaults to last value unless you indicate sum for the thank you to reference sum"""
    donor = Donor("Pippy Longstocking")
    donor.add_donation(25)
    donor.add_donation(300)
    donor.add_donation(500)

    print(donor.thank_your_letter())
    assert donor.thank_your_letter() == dedent(
        '''\tDear Pippy Longstocking,
        Thank you for your generous donation of $500 to our cause.
        
        Sincerely,
        The Team''')

    print(donor.thank_your_letter('sum'))
    assert donor.thank_your_letter('sum') == dedent(
        '''\tDear Pippy Longstocking,
        Thank you for your generous donation of $825 to our cause.
        
        Sincerely,
        The Team''')

def test_repr_():
    donor = Donor("Pippy Longstocking")
    donor.add_donation(25)
    donor.add_donation(300)
    print(donor)
    assert repr(donor) == 'Donor(Pippy Longstocking) : [25, 300]'



#######################Test Donor Collection Class################

def test_donor_collection():
    """tests to see I can instantiate a donor collection and that I am able to add a list of donors"""
    dc = DonorCollection()
    dp = DonorCollection(donor_mock2)

    assert "John Galt" in dp.donor_dict.keys()


def test_add_donor():
    """Tests that you can add a donor to the DonorCollection object. 
       Then add a donation, then confirm the name is they key in the
       dictionary."""
    donor = Donor("Pippy Longstocking")
    dc = DonorCollection()
    donor.add_donation(25)
    dc.addDonor(donor.name, donor)
    donor2 = Donor("Manu Chow")
    donor2.add_donation(500)
    dc.addDonor(donor2.name, donor2)

    assert "Manu Chow" in dc.donor_dict.keys()
    assert "Pippy Longstocking" in dc.donor_dict.keys()


def test_search_donor():
    pass

