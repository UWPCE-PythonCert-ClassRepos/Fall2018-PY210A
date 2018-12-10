#Lesson09
#Objected Oriented Mailroom Exercise 09 - Test Code
#
#!/usr/bin/env python3
from donor_models import *
#define function
def test_name():
    bob = Donors("Bob Smith")
    assert bob.name == "Bob Smith"

def test_add_donations():
    bob = Donors("Bob Smith")
    assert bob.add_donations(400) == [400]
    assert bob.add_donations(600) ==[400, 600]
    assert bob.add_donations(844) ==[400, 600, 844]

def test_sum_donations():
    bob = Donors("Bob Smith")
    assert bob.add_donations(400) == [400]
    assert bob.add_donations(600) ==[400, 600]
    assert bob.add_donations(500) ==[400, 600, 500]
    assert bob.sum_donations() == 1500

def test_str():
    bob = Donors("Bob Smith")
    assert bob.add_donations(400) == [400]
    assert bob.add_donations(600) ==[400, 600]
    assert bob.add_donations(500) ==[400, 600, 500]
    assert "Donor, Bob Smith, with a total donation amount of: $1500"

def test_avg_donations():
        bob = Donors("Bob Smith")
        assert bob.add_donations(400) == [400]
        assert bob.add_donations(600) ==[400, 600]
        assert bob.add_donations(500) ==[400, 600, 500]
        assert bob.avg_donations() == 500

def test_main_menu():
    mainmenu = Menu("Main Menu")
    assert mainmenu.menu_name == "Main Menu"

#for testing
if __name__=="__main__":
    pass
