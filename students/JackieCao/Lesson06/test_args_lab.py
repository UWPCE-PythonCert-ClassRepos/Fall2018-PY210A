"""
tests for args_lab
"""

from args_lab import colors
from args_lab import colors2
def test_pos():
    result = colors("red", "blue", "yellow", "chartreuse")
    print(result)
    assert result == ("red", "blue", "yellow", "chartreuse")


def test_key():
    result = colors(link_color = "red", back_color = "blue")
    print(result)
    assert result == ("red", "blue", "red", "lavender")

def test_pos_key():
    result = colors('purple',link_color = "red", back_color = "blue")
    print(result)
    assert result == ("purple", "blue", "red", "lavender")

def test_dict():
    cols = dict(fore_color = "red",
                back_color = "blue",
                link_color = "green",
                visited_color = "lavender"
               )
    print(cols)
    result = colors(**cols) # pass dictionary use **, pass tuple use *
    assert result == ("red", "blue", "green", "lavender")

def test_cols2_pos():
    args, kwargs = colors2("green", "lavender")
    assert args == ("green", "lavender")
    assert kwargs == {}

def test_cols2_key():
    args, kwargs = colors2(back_color = "red", link_color = "blue")
    assert args == ()
    print(kwargs)
    assert kwargs == {"back_color": "red", "link_color": "blue"}

def test_cols2_pos_key():
    args, kwargs = colors2("purple", back_color = "red", link_color = "blue")
    print(args)
    print(kwargs)
    assert args == ("purple",)
    assert kwargs == {"back_color": "red", "link_color": "blue"}

def test_cols2_dict():
    cols = dict(fore_color = "red",
                back_color = "blue",
                link_color = "green",
                visited_color = "lavender"
               )
    print(cols)
    args, kwargs = colors2(**cols) # pass dictionary use **, pass tuple use *
    print(args)
    print(kwargs)
    assert args == ()
    assert kwargs == {"fore_color": "red",
                      "back_color": "blue",
                      "link_color": "green",
                      "visited_color": "lavender"
                     }



