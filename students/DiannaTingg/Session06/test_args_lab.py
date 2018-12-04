# Tests for Args Lab

import pytest
from args_lab import colors, colors2

# Keyword arguments


def test_default():
    result = colors()
    print(result)
    assert result == ("red", "yellow", "green", "blue")


def test_pos():
    result = colors("pink", "orange", "yellow", "purple")
    print(result)
    assert result == ("pink", "orange", "yellow", "purple")


def test_key():
    result = colors(link_color="red", back_color="blue")
    print(result)
    assert result == ("red", "blue", "red", "blue")


def test_pos_key():
    result = colors("purple", link_color="red", back_color="blue")
    print(result)
    assert result == ("purple", "blue", "red", "blue")


def test_tuple():
    cols = ("brown", "black", "white", "gray")
    result = colors(*cols)
    print(result)
    assert result == ("brown", "black", "white", "gray")


def test_dict():
    cols = {"visited_color": "lime", "link_color": "olive", "back_color": "forest", "fore_color": "teal"}
    result = colors(**cols)
    print(result)
    assert result == ("teal", "forest", "olive", "lime")


def test_tuple_dict():
    regular = ("red", "blue")
    links = {"link_color": "gold"}
    result = colors(*regular, **links)
    print(result)
    assert result == ("red", "blue", "gold", "blue")


def test_pos_key_error():
    with pytest.raises(TypeError):
        result = colors("magenta", link_color="pink", fore_color="red")
        print(result)


# Generic parameters


def test_colors2_pos():
    args, kwargs = colors2("green", "lavender", flower="pink")
    print(args, kwargs)
    assert args == ("green", "lavender")
    assert kwargs == {"flower": "pink"}


def test_colors2_no_args():
    args, kwargs = colors2(bee="yellow")
    print(args, kwargs)
    assert args == ()
    assert kwargs == {"bee": "yellow"}


def test_colors2_no_kwargs():
    args, kwargs = colors2("hot pink", "electric blue", "neon green")
    print(args, kwargs)
    assert args == ("hot pink", "electric blue", "neon green")
    assert kwargs == {}
