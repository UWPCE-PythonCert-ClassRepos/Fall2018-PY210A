import mailroom as mail


def test_add_donor():
    mail.add_donor("Jae", 500)

    assert "Jae" in mail.players


def test_send_thank_you():
    letter = mail.send_thank_you("LeBron James")

    assert letter.startswith("Hi LeBron James,")


def test_reset_donors():
    mail.add_donor("Jae", 500)
    mail.players = mail.reset_donors()

    assert "Jae" not in mail.players


def test_make_report():
    report = mail.make_report()

    assert report.startswith("Donor Name")
    assert "LeBron James" in report
    assert "Dwyane Wade" in report
    assert "Carmelo Anthony" in report
    assert "Kevin Durant" in report
    assert "Michael Jordan" in report


def test_make_report_with_new_donor():
    mail.add_donor("Jae", 500)
    report = mail.make_report()

    assert "Jae" in report
