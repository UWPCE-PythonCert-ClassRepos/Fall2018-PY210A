"""
test for args and kwargs lab
"""
import pytest
from args_and_kwargs import colors, colors2


def test_pos():
    result = colors('red', 'blue', 'yellow', 'chartreuse')
    assert result == ('red', 'blue', 'yellow', 'chartreuse')

def test_key():
    result = colors(link_color='red', back_color='blue')
    assert result == ('red', 'blue', 'red', 'lavender')

def test_combination():
    with pytest.raises(TypeError):
        result = colors('purple', link_color='red', fore_color='blue')
    #print(result)
    #assert result == ('purple', 'blue', 'red', 'lavender')

def test_default():
    result = colors()
    assert result == ('red', 'blue', 'green', 'lavender')


def test_dict():
    cols = dict(fore_color='orange',
                back_color='black',
                link_color='ground color',
                visited_color='lavender'
                )
    result = colors(**cols)
    print(result)
    assert result == ('orange', 'black', 'ground color', 'lavender')


def test_tuple():
    color_tup = ('blue', 'red')
    result = colors(*color_tup)
    assert result == ('blue', 'red', 'green', 'lavender')


def test_tuple_dict():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    result = colors(*regular, **links)
    print(result)
    assert result == ('red', 'blue', 'chartreuse', 'lavender')

def test_colors2_pos():
    result = colors2('green', 'lavender')
    print(type(result))
    print(type(('green', 'lavender', 'green', 'lavender')))
    assert result == ('green', 'lavender', 'green', 'lavender')


def test_pos2():
    result = colors2('red', 'blue', 'yellow', 'chartreuse')
    assert result == ('red', 'blue', 'yellow', 'chartreuse')

def test_key2():
    result = colors2(link_color='red', back_color='blue')
    assert result == ('red', 'blue', 'red', 'lavender')

def test_combination2():
    with pytest.raises(TypeError):
        result = colors2('purple', link_color='red', fore_color='blue')
    #print(result)
    #assert result == ('purple', 'blue', 'red', 'lavender')

def test_default2():
    result = colors2()
    assert result == ('red', 'blue', 'green', 'lavender')


def test_dict2():
    cols = dict(fore_color='orange',
                back_color='black',
                link_color='ground color',
                visited_color='lavender'
                )
    result = colors2(**cols)
    print(result)
    assert result == ('orange', 'black', 'ground color', 'lavender')


def test_tuple2():
    color_tup = ('blue', 'red')
    result = colors2(*color_tup)
    assert result == ('blue', 'red', 'green', 'lavender')


def test_tuple_dict2():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    result = colors2(*regular, **links)
    print(result)
    assert result == ('red', 'blue', 'chartreuse', 'lavender')
