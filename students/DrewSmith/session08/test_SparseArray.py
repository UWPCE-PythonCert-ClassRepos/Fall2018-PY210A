#!/usr/bin/env python
"""
Test SparseArray
"""
from SparseArray import SparseArray

def test_init():
    s = SparseArray([0,3,5,0,4])
    assert len(s) == 5
    assert len(s._values) == 3

def test_get_item():
    s = SparseArray([0,3,5,0,4])
    assert s[0] == 0
    assert s[1] == 3
    assert s[4] == 4
    assert s[-3] == 5

def test_set_item():
    s = SparseArray([0,3,5,0,4])
    s[0] = 3
    assert s[0] == 3
    s[1] = 0
    assert s[1] == 0
    
def test_del_item():
    s = SparseArray([1,2,0,0,0,0,3,0,0,4])
    del s[1]
    assert s[1] == 0
    del s[4]
    assert s[4] == 3

def test_append():
    s = SparseArray([1,2,0,0,0,0,3,0,0,4])
    s.append(10)
    assert len(s) == 11
    assert s[10] == 10

def test_contains():
    s = SparseArray([1,2,0,0,0,0,3,0,0,4])
    s.append(10)
    assert 3 in s
    assert 0 in s
    assert 50 not in s

def test_slice():
    s = SparseArray([1,2,0,0,0,0,3,0,0,4])
    result = s[1:4]
    assert str(result) == "[2, 0, 0]"
    result = s[::2]
    assert str(result) == "[1, 0, 0, 3, 0]"
    result = s[-4:]
    assert str(result) == "[3, 0, 0, 4]"

def test_str():
    s = SparseArray([1,2,3,4])
    result = str(s)
    assert result == "[1, 2, 3, 4]"
