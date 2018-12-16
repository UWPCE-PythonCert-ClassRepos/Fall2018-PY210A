from .donor_models import 



def test_find_or_create_donor():
    """test one that's not there"""
    donor = sample_db.test_find_or_create_donor("Bob Jones")

    assert donor.name == "Bob Jones"
    assert donor.last_donation is None
