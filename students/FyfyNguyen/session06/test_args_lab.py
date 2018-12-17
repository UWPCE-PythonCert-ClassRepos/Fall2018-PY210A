#!/usr/bin/env python3

"""
Tests for args_lab
"""

import pytest
from args_lab import colors, call_colors


def test_pos():
    result = colors('ivory', 'charcoal', 'mulberry', 'azure')
    print(result)
    assert 'ivory' in result
    assert 'charcoal' in result
    assert 'mulberry' in result
    assert 'azure' in result


def test_key():
    result = colors(link_color='mulberry', back_color='charcoal')
    print(result)
    assert 'mulberry' in result
    assert 'charcoal' in result


def test_combo():
    with pytest.raises(TypeError):
        result = colors('azure', link_color='mulberry', fore_color='ivory')
        print(result)
        assert 'azure' in result
        assert 'mulberry' in result
        assert 'ivory' in result


def test_default():
    result = colors('ivory', 'charcoal', 'mulberry', 'azure')
    print(result)
    assert 'ivory' in result
    assert 'charcoal' in result
    assert 'mulberry' in result
    assert 'azure' in result


def test_dict():
    d = dict(fore_color="ivory",
             back_color="charcoal",
             link_color="mulberry",
             visited_color="azure"
             )
    result = colors(**d)
    assert 'ivory' in result
    assert 'charcoal' in result
    assert 'mulberry' in result
    assert 'azure' in result


def test_tuple():
    d = ('ivory', 'charcoal', 'mulberry', 'azure')
    result = colors(*d)
    assert 'ivory' in result
    assert 'charcoal' in result
    assert 'mulberry' in result
    assert 'azure' in result


def test_tuple_dict():
    regular = ('ivory', 'charcoal')
    links = dict(link_color='mulberry', visited_color='azure')
    result = colors(*regular, **links)
    print(result)
    assert 'ivory' in result
    assert 'charcoal' in result
    assert 'mulberry' in result
    assert 'azure' in result


def test_tuple_dict2():
    args, kwargs = call_colors('blue', 'purple')
    assert args == ('blue', 'purple')
    assert kwargs == {}
