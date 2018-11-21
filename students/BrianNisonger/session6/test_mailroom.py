import mailroom


def test_average_donations():
    test_amount = (100, 200, 300, 400)
    test_amount = mailroom.average_donations(test_amount)
    assert test_amount == 250


def test_total_donations():
    test_amount = (100, 200, 300, 400)
    test_amount = mailroom.total_donations(test_amount)
    assert test_amount == 1000


def test_count_donations():
    test_amount = (100, 200, 300, 400)
    test_amount = mailroom.count_donations(test_amount)
    assert test_amount == 4


def test_make_report_strings():
    sum_donors = [['Bill Gates', [200.0, 600.0, 3]],
                  ['Jack Frost', [69.0, 207.0, 3]],
                  ['Maya Angelou', [7084.8533333333335, 21254.56, 3]]]
    report_string = mailroom.make_report_strings(sum_donors)
    test_report_string = [
        'Bill Gates           $600.00          3               $200.00         ',
        'Jack Frost           $207.00          3               $69.00          ',
        'Maya Angelou         $21254.56        3               $7084.85        '
    ]
    assert report_string == test_report_string


def test_make_sum_donors():
    donors = {
        "Bill Gates": [100.00, 200.00, 300.00],
        "Jack Frost": [2.00, 5.00, 200.00],
        "Maya Angelou": [20000.00, 20.00, 1234.56]
    }
    sum_donors = mailroom.make_sum_donors(donors)
    test_sum_donors = [['Bill Gates', [200.0, 600.0, 3]],
                       ['Jack Frost', [69.0, 207.0, 3]],
                       ['Maya Angelou', [7084.8533333333335, 21254.56, 3]]]
    assert sum_donors == test_sum_donors


def test_make_header_string():
    header_string = mailroom.make_headers_string()
    test_header_string = "Donor Names          Total Given     Num Gifts       Average Gifts  "
    assert header_string == test_header_string


def test_sort_key():
    sum_donors = ['Bill Gates', [200.0, 600.0, 3]]
    test_sort_key = mailroom.sort_key(sum_donors)
    assert test_sort_key == 600.0


def test_make_total_donors():
    donors = {
        "Bill Gates": [100.00, 200.00, 300.00],
        "Jack Frost": [2.00, 5.00, 200.00],
        "Maya Angelou": [20000.00, 20.00, 1234.56]
    }
    total_donors = mailroom.make_total_donors(donors)
    test_total_donors = [['Bill Gates', 600.0, 'Bill_Gates.txt'],
                         ['Jack Frost', 207.0, 'Jack_Frost.txt'],
                         ['Maya Angelou', 21254.56, 'Maya_Angelou.txt']]
    assert total_donors == test_total_donors


def test_make_filename():
    name = "Brian Nisonger"
    test_filename = mailroom.make_filename(name)
    assert test_filename == "Brian_Nisonger.txt"


def test_make_thank_you_list():
    test_total_donors = [['Bill Gates', 600.0, 'Bill_Gates.txt'],
                         ['Jack Frost', 207.0, 'Jack_Frost.txt'],
                         ['Maya Angelou', 21254.56, 'Maya_Angelou.txt']]
    thank_you_list = mailroom.make_thank_you_list(test_total_donors)
    test_thank_you_list = [
        [
            'Dear Bill Gates, Thank you for your donation of $600.00.'
            'These funds help save the migratory butterflies of New South East.Thank you',
            'Bill_Gates.txt'
        ],
        [
            'Dear Jack Frost, Thank you for your donation of $207.00.'
            'These funds help save the migratory butterflies of New South East.Thank you',
            'Jack_Frost.txt'
        ],
        [
            'Dear Maya Angelou, Thank you for your donation of $21254.56.'
            'These funds help save the migratory butterflies of New South East.Thank you',
            'Maya_Angelou.txt'
        ]
    ]
    assert thank_you_list == test_thank_you_list


def test_thank_donor_msg():
    thank_donor_msg_string = mailroom.thank_donor_msg('Brian Nisonger', 600.0)
    test_thank_donor_msg_string = (
        'Dear Brian Nisonger, Thank you for your donation of $600.00.'
        'These funds help save the migratory butterflies of New South East.Thank you'
    )
    assert test_thank_donor_msg_string == thank_donor_msg_string


def test_list_donors():
    donors = {
        "Bill Gates": [100.00, 200.00, 300.00],
        "Jack Frost": [2.00, 5.00, 200.00],
        "Maya Angelou": [20000.00, 20.00, 1234.56]
    }
    list_donor_list = mailroom.list_donors(donors)
    assert list_donor_list == ["Bill Gates", "Jack Frost", "Maya Angelou"]
