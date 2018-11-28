#!/usr/bin/env python3

"""
tests for args_lab
"""
import pytest
from args_lab import colors
from args_lab import colors2

def test_pos():
    result = colors('red', 'blue', 'lavender', 'purple')
    assert result == ('red', 'blue', 'lavender', 'purple')

def test_key():
    result = colors(link_color='lavender', back_color='purple')
    assert result == ('red', 'purple', 'lavender', 'lavender')

def test_pos_key():
    with pytest.raises(TypeError):
        result = colors('purple', link_color='red', fore_color='blue')
    #assert result == ('blue', 'blue', 'red', 'lavender')

def test_default():
    result = colors()
    assert result == ('red', 'blue', 'green', 'lavender')

def test_empty():
    result = colors('')
    assert result == ('', 'blue', 'green', 'lavender')

def test_dict():
    cols = dict(fore_color="purple", 
            back_color="blue", 
            link_color="green", 
            visited_color="pink")
    result = colors(**cols)
    assert result == ('purple', 'blue', 'green', 'pink')


def test_dict2():
    cols = dict(fore_color="purple", 
            back_color="blue",)
    result = colors(**cols)
    assert result == ('purple', 'blue', 'green', 'lavender')


def test_tuple():
    cols_t = ("purple", "blue","green","pink")
    result = colors(*cols_t)
    assert result == ('purple', 'blue', 'green', 'pink')

def test_tuple_dict():
    cols_t = ("purple", "blue",)
    cols = dict(link_color="green", 
            visited_color="pink")
    result = colors(*cols_t, **cols)
    assert result == ('purple', 'blue', 'green', 'pink')

def test_tuple_dict2():
    args, kwargs = colors2('green', 'lavender')
    assert args == ('green', 'lavender')
    assert kwargs == {}