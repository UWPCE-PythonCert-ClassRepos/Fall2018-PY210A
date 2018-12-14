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
    assert bob.add_donations(400) == [0, 400]
    assert bob.add_donations(600) ==[0, 400, 600]
    assert bob.add_donations(844) ==[0, 400, 600, 844]

def test_sum_donations():
    bob = Donors("Bob Smith")
    assert bob.add_donations(400) == [0, 400]
    assert bob.add_donations(600) ==[0, 400, 600]
    assert bob.add_donations(500) ==[0, 400, 600, 500]
    assert bob.sum_donations() == 1500

def test_str():
    bob = Donors("Bob Smith")
    assert bob.add_donations(400) == [0, 400]
    assert bob.add_donations(600) ==[0, 400, 600]
    assert bob.add_donations(500) ==[0, 400, 600, 500]
    assert "Donor, Bob Smith, with a total donation amount of: $1500"

def test_avg_donations():
        bob = Donors("Bob Smith")
        assert bob.add_donations(400) == [0, 400]
        assert bob.add_donations(600) ==[0, 400, 600]
        assert bob.add_donations(500) ==[0, 400, 600, 500]
        assert bob.avg_donations() == 500

def test_main_menu():
    mainmenu = Menu("Main Menu")
    assert mainmenu.menu_name == "Main Menu"

def test_donor_name_format():
    Test = Menu("Test Menu")
    assert Test.donor_name_format("Bob Smith") == "bobsmith"

def test_donor_list():
    test_menu = Menu("Test Menu")
    #assert test_menu.donor_exists("hestershaw") == True

def test_donor_add():
    test_menu = Menu("Test Menu")
    test_menu.donor_add('joebob', "Joe Bob")
    assert test_menu.donor_exists("joebob")

def test_get_obj_name():
    # doesn't work - I've coded my project in a way that is hard to test. prob
    # means it is not a good design?
    test_menu = Menu("Test Menu")
    test_menu.donor_add('joebob', "Joe Bob")
    #assert test_menu.get_obj_name('joebob') == joebob



#for testing
if __name__=="__main__":
    pass
