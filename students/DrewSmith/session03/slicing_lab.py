
def exchange_first_last(seq):
    if len(seq) <= 1:
        return seq[:]
    return seq[-1:] + seq[1:-1] + seq[:1]

def every_other_removed(seq):
    return seq[::2]

def four_ends_removed(seq):
    return seq[4:-4:2]

def reverse(seq):
    return seq[::-1]

def thirds_switch_a_roo(seq):
    if len(seq) < 3:
        return seq[:]
    third = len(seq) // 3
    neg_third = third * -1
    return seq[neg_third:] + seq[:third] + seq[third:neg_third]

if __name__ == "__main__":
    assert exchange_first_last("this is a string") == "ghis is a strint"
    assert exchange_first_last((2, 54, 13, 12, 5, 32)) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last('a') == "a"
    assert exchange_first_last([]) == []

    assert every_other_removed("this is a string") == "ti sasrn"
    assert every_other_removed((2, 54, 13, 12, 5, 32)) == (2, 13, 5)
    assert every_other_removed([2, 54, 13, 12, 5, 32, 400]) == [2, 13, 5, 400]
    assert every_other_removed('a') == "a"
    assert every_other_removed([]) == []

    assert four_ends_removed("this is a string") == " sas"
    assert four_ends_removed((2, 54, 13, 12, 5, 32)) == ()
    assert four_ends_removed([2, 54, 13, 12, 5, 32, 400, 60]) == []
    assert four_ends_removed([2, 54, 13, 12, 5, 32, 400, 60, 70]) == [5]

    assert reverse("this is a string") == "gnirts a si siht"
    assert reverse((2, 54, 13, 12, 5, 32)) == (32, 5, 12, 13, 54, 2)
    assert reverse('a') == "a"
    assert reverse([]) == []

    assert thirds_switch_a_roo("123456789") == "789123456"
    assert thirds_switch_a_roo("1234567890") == "8901234567"
    assert thirds_switch_a_roo("12345678900") == "90012345678"
    assert thirds_switch_a_roo("12") == "12"
    assert thirds_switch_a_roo([]) == []