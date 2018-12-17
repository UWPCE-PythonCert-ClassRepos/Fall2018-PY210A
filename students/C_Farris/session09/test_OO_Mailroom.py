#!/usr/bin/env Python3


######
#Created by: Carol Farris
#Name: test_OO_Mailroom.Python.py
#Purpose: Test Donor and Donor Collection classes for OO Mailroom
#####

from OO_Mailroom import *

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
    """tests that add_donation cheks donation values 
    are numeric and greater than a penny"""
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
    """Returns a thank you letter that defaults to last value
     unless you indicate sum for the thank you to reference sum"""
    donor = Donor("Pippy Longstocking")
    donor.add_donation(25)
    donor.add_donation(300)
    donor.add_donation(500)

    assert donor.thank_your_letter() == dedent(
        '''\tDear Pippy Longstocking,
        Thank you for your generous donation of $500.00 to our cause.
        
        Sincerely,
        The Team''')

    print(donor.thank_your_letter('sum'))
    assert donor.thank_your_letter('sum') == dedent(
        '''\tDear Pippy Longstocking,
        Thank you for your generous donation of $825.00 to our cause.
        
        Sincerely,
        The Team''')

def test_repr_():
    donor = Donor("Pippy Longstocking")
    donor.add_donation(25)
    donor.add_donation(300)

    assert repr(donor) == 'Donor(Pippy Longstocking) : [25, 300]'


#######################Test Donor Collection Class################

def test_donor_collection():
    """tests to see I can instantiate a donor 
    collection and that I am able to add a list of donors"""
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
    dc.addDonor("Py Thon", Donor("Py Thon"))
    
    assert "Py Thon" in dc.donor_dict.keys()
    assert "Manu Chow" in dc.donor_dict.keys()
    assert "Pippy Longstocking" in dc.donor_dict.keys()

def test_add_donor_cleaned_name():
    """Confirm cleaned donor name is capitalized 
    with all other letters lowercase """
    donor = Donor("Pippy Longstocking", [0.1, 0.01, 100000])
    donor2 = Donor("MANU ChoW", [10, 20, 30])
    donor3 = Donor("barak obama", [400, 500, 600])
    dc = DonorCollection()
    dc.addDonor(donor.name, donor)
    dc.addDonor(donor2.name, donor2)
    dc.addDonor(donor3.name, donor3)

    assert dc.list_donors() == 'Pippy Longstocking\nManu Chow\nBarak Obama\n'


def test_list_donors():
    dc = DonorCollection()
    donor = Donor("Pippy Longstocking", 0.1)
    donor2 = Donor("Manu Chow", 10)
    donor3 = Donor("Barak Obama", [400, 500, 600])
    dc.addDonor(donor.name, donor)
    dc.addDonor(donor2.name, donor2)
    dc.addDonor(donor3.name, donor3)

    assert dc.list_donors() =='Pippy Longstocking\nManu Chow\nBarak Obama\n'


def test_donor_Found():
    """tests that a valid donor object can be tested/added to dictionary"""
    dc = DonorCollection()
    donor = Donor("Pippy Longstocking", 100000)
    donor2 = Donor("Manu Chow", [10, 20, 30, 40])
    donor3 = Donor("Barak Obama", 400)
    dc.addDonor(donor.name, donor)
    dc.addDonor(donor2.name, donor2)
    dc.addDonor(donor3.name, donor3)

    assert dc.donor_Found(donor2.name) == True
    assert dc.donor_Found('Betsy DeVos') == False


def test_add_donor_donation():
    dc = DonorCollection()
    donor3 = Donor("Barak Obama", 400)
    dc.addDonor(donor3.name, donor3)
    dc.add_donor_donation("Barak Obama", 3000)

    assert repr(donor3) == 'Donor(Barak Obama) : [400, 3000]'


def test_create_report():
    """test create_report and confirms it starts with a 
    header list, then header f string and lastly donor 
    list for reporting"""
    dc = DonorCollection()
    donor = Donor("Pippy Longstocking", 100000)
    donor2 = Donor("Manu Chow", [10, 20])
    donor3 = Donor("Barak Obama", [400, 1, 2, 3])
    dc.addDonor(donor.name, donor)
    dc.addDonor(donor2.name, donor2)
    dc.addDonor(donor3.name, donor3)
 
    assert dc.create_report() == (['Donor Name', 'Total Donation', 'Number Donations', 'Average Donation'], 
                                   '\nDonor Name           Total Donation  Number Donations Average Donation         ',
                                   [[100000.0, 'Pippy Longstocking', 1, 100000.0], [406.0, 'Barak Obama', 4, 101.5],
                                    [30.0, 'Manu Chow', 2, 15.0]])

def test_send_file_to_disk():
    """test send_file_to_disk to ensure you 
    can add a donor and donor letter """
    donor = Donor("Leo Tolstoy", 25)
    dc = DonorCollection()
    dc.addDonor(donor.name, donor)
    letter = "Dear Leo,\n Thanks for writing War and Peace.\nI did think it interesting you tried to relate war to mathematical theory of war.\n"
    OUT_PATH = "thank_you_letters"
    
    assert os.path.exists('./thank_you_letters/Leo_Tolstoy.txt') == True
    assert os.path.getsize('./thank_you_letters/Leo_Tolstoy.txt') > 0


def test_prepare_to_write_to_disk():
    """tests the method prepare_to_write_to_disk to 
    ensure  given a path it will write the form letter to each donor."""
    dc = DonorCollection(donor_mock2)
    OUT_PATH = "thank_you_letters"
    dc.prepare_to_write_to_disk(OUT_PATH)

    assert os.path.exists('./thank_you_letters/') == True


def test_save_all_thank_yous(): 
    """Tests save_all_thank_yous writes a thank you l
    etter in a donor_name.txt in a thank_you directory
    Also tests that at files are not of zero size"""
    dc = DonorCollection(donor_mock2)
    dc.save_all_thank_yous()

    assert os.path.exists('./thank_you_letters/Jeff_Bezos.txt') == True
    assert os.path.exists('./thank_you_letters/John_Galt.txt') == True
    assert os.path.exists('./thank_you_letters/Mark_Zuckerberg.txt') == True
    assert os.path.exists('./thank_you_letters/Paul_Allen.txt') == True
    assert os.path.exists('./thank_you_letters/William_Gates_III.txt') == True
    assert os.path.exists('./thank_you_letters/Betsy_DeVos.txt') == False

    assert os.path.getsize('./thank_you_letters/Jeff_Bezos.txt') > 0
    assert os.path.getsize('./thank_you_letters/John_Galt.txt') > 0


def test_thank_donor():
    donor = Donor("Leo Tolstoy", [3000, 25])
    dc = DonorCollection()
    dc.addDonor(donor.name, donor)
    print(dc.thank_donor(donor.name))
    print(dc.thank_donor("Isaac Newton"))

    assert dc.thank_donor(donor.name) == dedent(
        '''\tDear Leo Tolstoy,
        Thank you for your generous donation of $25.00 to our cause.
        
        Sincerely,
        The Team''')

    assert dc.thank_donor(donor.name, 'sum') == dedent(
        '''\tDear Leo Tolstoy,
        Thank you for your generous donation of $3025.00 to our cause.
        
        Sincerely,
        The Team''')

    assert dc.thank_donor("Isaac Newton") == 'Donor Not Found! No \'thank you letter\' made'



