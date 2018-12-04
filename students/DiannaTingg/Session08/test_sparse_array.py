# Tests for Sparse Array Class

from sparse_array import SparseArray
import pytest


def test_new_array():
    SparseArray([0, 1, 0, 2, 0, 3])


def test_no_array():
    with pytest.raises(TypeError):
        SparseArray()


def test_length():
    sa = SparseArray([0, 1, 0, 2, 0, 3])

    assert len(sa) == 6


def test_string():
    sa = SparseArray([0, 1, 0, 2, 0, 3])

    assert str(sa) == "[0, 1, 0, 2, 0, 3]"


def test_equals():
    sa1 = SparseArray([0, 0, 7, 0, 0, 7])

    assert sa1 == SparseArray([0, 0, 7, 0, 0, 7])
    assert sa1 != SparseArray([7, 7])
    assert sa1 == [0, 0, 7, 0, 0, 7]


def test_add():
    sa = SparseArray([0, 1, 0])
    answer = sa.size
    answer += 1

    assert answer == 4


def test_sub():
    sa = SparseArray([0, 1, 0])
    answer = sa.size
    answer -= 1

    assert answer == 2


def test_convert_neg_index():
    sa = SparseArray([0, 1, 0, 2, 0, 3])
    new_index = sa.convert_neg_index(-2)

    assert new_index == 4


# Valid index numbers
def test_get_index():
    sa = SparseArray([0, 1, 2, 3, 4, 0])

    assert sa[0] == 0
    assert sa[2] == 2
    assert sa[5] == 0
    assert sa[-1] == 0
    assert sa[-2] == 4


# Index number too high
def test_get_index2():
    sa = SparseArray([0, 1, 2, 3, 4, 0])

    with pytest.raises(IndexError):
        print(sa[8])


# Index number too low (supports negative indexing)
def test_get_index3():
    sa = SparseArray([0, 1, 2, 3, 4, 0])

    with pytest.raises(IndexError):
        print(sa[-7])


# Valid index numbers
def test_set_index():
    sa = SparseArray([0, 1, 0, 2, 0, 3])
    sa[1] = 5

    assert sa == [0, 5, 0, 2, 0, 3]


# Index number too high
def test_set_index2():
    sa = SparseArray([0, 1, 0, 2, 0, 3])

    with pytest.raises(IndexError):
        sa[10] = 8


# Index number too low (supports negative indexing)
def test_set_index3():
    sa = SparseArray([0, 1, 0, 2, 0, 3])
    sa[-1] = 0

    assert sa == [0, 1, 0, 2, 0, 0]

    with pytest.raises(IndexError):
        sa[-8] = 8


def test_delete_index():
    sa = SparseArray([0, 0, 2, 3, 4, 5])
    del sa[2]

    assert len(sa) == 5
    assert sa == [0, 0, 3, 4, 5]


def test_delete_index2():
    sa = SparseArray([0, 0, 2, 3, 4, 5])
    with pytest.raises(IndexError):
        del sa[6]


def test_append():
    sa = SparseArray([0, 1, 0, 3, 4, 0])
    assert len(sa) == 6

    sa.append(8)
    assert len(sa) == 7
    assert sa == [0, 1, 0, 3, 4, 0, 8]
    assert sa != [0, 1, 0, 3, 4, 0]


def test_slicing():
    sa = SparseArray([0, 1, 2, 0, 3, 0, 4, 5])
    test_slice = sa[1:4]

    assert test_slice == [1, 2, 0]


def test_slicing2():
    sa = SparseArray([0, 1, 2, 0, 3, 0, 4, 5])
    test_slice = sa[8:9]

    assert test_slice == []


def test_slicing3():
    sa = SparseArray([0, 1, 2, 0, 3, 0, 4, 5])
    test_slice = sa[::2]

    assert test_slice == [0, 2, 3, 4]
    assert test_slice != [0, 1, 2, 0, 3, 0, 4, 5]
