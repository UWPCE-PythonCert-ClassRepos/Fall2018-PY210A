#!usr/bin/env python3

"""test script for squirrel_play"""


from squirrel_play import squirrel_play

def test_1():
    assert squirrel_play(70, False) == True

def test_2():
    assert squirrel_play(95, False) == False

def test_3():
    assert squirrel_play(95, True) == True
