import mailroom_04 as mr


def test_make_list():
    result = mr.make_list()

    assert len(result) == len(mr.donors)


def test_add_donation():
    result = mr.add_donation("Tara Towers", 9999)

    assert result[-1] == 9999


def test_add_donation_new():
    result = mr.add_donation_new("Jane Janeson", 1000)

    assert result in mr.donors.values()


def test_make_thank_you_file():
    result = mr.make_thank_you_file("Kevin Smith", 10000)

    # Just open(result) works, but this makes it clearer I think
    assert bool(open(result)) is True


def test_make_report():
    result = mr.make_report()

    # Just open(result) works, but this makes it clearer I think
    assert bool(open(result)) is True


def test_exiting():
    result = mr.exiting()

    assert result == "exiting"
