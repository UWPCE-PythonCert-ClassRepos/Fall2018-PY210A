#!/usr/bin/env python

import mailroom as mr

def test_get_donors():
    result = mr.get_donors()
    print(result)
    assert result == ['Jimmy John', 'Amy Shumer', 'Parker Pony', 'Cher', 'Legolass Mario']

def test_print_donors():
    result = mr.print_donors()
    print(result)
    result_lines = result.splitlines()
    assert result_lines[0] == 'List of current donors:'
    assert len(result_lines) > 1

def test_enter_donation():
    pass

def test_save_thank_you_letter():
    pass

def test_thank_you_letter():
    result = mr.thank_you_letter('Jimmy John')
    output = "Dear Jimmy John\n\n"
    output += "          Thank you for your kind donation of $300.00.\n\n"
    output += "          It will be put to very good use.\n\n"
    output += "               Sincerely,\n"
    output += "                  -Everyone here at Company Spot"
    assert result == output

def test_thank_you():
    pass

def test_stats():
    result = mr.stats('Jimmy John')
    print(result)
    assert result == ['Jimmy John', 600, 3, '200.00']

def test_widths():
    result = mr.widths([['Test Name that is long', 15000, 100, '12000000000.00'],
                        ['Second Sample Name', 1100, 1, '4000']]
                      )
    print(result)
    assert result == [22, 12, 12, 14]

def test_data_header():
    result = mr.data_header([10, 15, 12, 17])
    output = '\nDonor Name|Total Given    | Num Gifts  |  Average Gift   '
    output += '\n' + '-' * (54 + 3)
    assert result == output

def test_data_print():
    pass

def test_report():
    pass

def test_all_letters():
    pass

def test_unknown():
    pass
