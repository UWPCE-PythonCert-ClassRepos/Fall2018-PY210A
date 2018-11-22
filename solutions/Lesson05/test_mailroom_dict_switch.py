import mailroom_dict_switch as mr

<<<<<<< Updated upstream

def test_remove_inputquotes():
    result = mr.remove_inputquotes('"this"')
    assert result == 'this'

=======
def test_remove_inputquotes():
    result = mr.remove_inputquotes('"this"')

    assert result == 'this'
>>>>>>> Stashed changes

def test_remove_inputquotes_single():
    result = mr.remove_inputquotes("'this'")

    assert result == 'this'

<<<<<<< Updated upstream

def test_make_donor_list():
    result = mr.make_donor_list()

    print(result)
    num_donors = len(mr.DONORS)
    assert result.startswith("Donor Names:")
    assert len(result.split("\n")) == num_donors + 1
    # assert False


=======
#pytest parameterized testing

def test_make_donor_list():
    result = mr.make_donor_list()
    print(result)

    num_donors = len(mr.DONORS)

    assert len(result.split("\n")) == num_donors + 1
    assert result.startswith("Donor Names:")
    #assert False
>>>>>>> Stashed changes
