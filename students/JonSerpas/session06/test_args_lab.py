from args_lab import colors
import pytest


def test_pos():
    result = colors('red', 'blue', 'yellow', 'chartreuse')

    print(result)
    assert result == ('red', 'blue', 'yellow', 'chartreuse')


def test_pos2():
    result = colors(link_color='red', back_color='blue')

    print(result)
    assert result == ('red', 'blue', 'red', 'lavender')


def test_pos_key():
    result = colors('purple', link_color='red', fore_color='blue')

    print(result)
    assert result == ('blue', 'blue', 'red', 'lavender')


def test_pos_key_error():
    with pytest.raises(TypeError):
        result = colors('purple', link_color='red', fore_color='blue')
        return result


def test_defaults_empty():
    result = colors()
    assert result == ('red', 'blue', 'green', 'lavender')

