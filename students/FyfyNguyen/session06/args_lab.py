#!/usr/bin/env python3


def color(fore_color="ivory",
          back_color="charcoal",
          link_color="mulberry",
          visited_color="azure"):
    return fore_color, back_color, link_color, visited_color


def colors_two(*args, **kwargs):
    return (args, kwargs)
