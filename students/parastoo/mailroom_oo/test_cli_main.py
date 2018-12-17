from donor_models import Donor
from donor_models import DB

donors_names = ['Margare Atwood', 'Fred Armisen', 'Heinz the Baron Krauss von Espy']
donations = [[300, 555], [240, 422, 1000], [1500, 2300]]
DONORS = dict(zip(donors_names, donations))

def test_donor_name():
    d = Donor('Fred Armisen')
    assert d.name == 'Fred Armisen'

def test_donation_list():
    d1 = Donor('Fred Armisen', [240, 422, 1000])
    d2 = Donor('Fred Armisen', 240)

    assert d1.donations == [240, 422, 1000]
    assert d2.donations == [240]

def test_total_donation():
    d = Donor('Fred Armisen', [240, 422, 1000])

    assert d.total_donations == 1662

def test_average():
    d = Donor('Fred Armisen', [240, 422, 1000])

    assert d.average_donations == 554

def test_add_donation():
    d = Donor('Fred Armisen', [240, 422, 1000])
    d.add_donation(600)

    assert d.donations == [240, 422, 1000, 600]

def test_letter():
    d = Donor('Fred Armisen', [240, 422, 1000])
    letter = d.gen_letter

    assert letter.startswith('Dear Fred Armisen')
    assert 'donation of $1000' in letter

def test_donors():
    db = DB(DONORS)
    assert db.donors == DONORS

def test_empty_donors():
    db = DB()
    assert db.donors == {}

def test_update_donor():

    db = DB(DONORS)
    db.update_donor('Margare Atwood', 400)

    assert db.donors == {'Margare Atwood': [300, 555, 400],
                  'Fred Armisen': [240, 422, 1000],
                  'Heinz the Baron Krauss von Espy': [1500, 2300]}


def test_find_donor():
    db = DB(DONORS)

    assert db.find_donor('Margare Atwood') == 'Margare Atwood'
    assert db.find_donor('Paul Allen') == None

def test_add_donor():
    d = DB(DONORS)
    donor = d.add_donor('Paul Allen', 5000)

    assert 'Paul Allen' in DONORS
    assert DONORS['Paul Allen'] == 5000

def test_list_donors():
    db = DB(DONORS)
    list = db.list_donors

    assert list == 'Margare Atwood\nFred Armisen\nHeinz the Baron Krauss von Espy\nPaul Allen'


