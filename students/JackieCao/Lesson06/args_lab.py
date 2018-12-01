#!/usr/bin/env python3
"""
args and kwargs LAB
"""

def colors(fore_color = "red",
           back_color = "blue",
           link_color = "green",
           visited_color = "lavender"
          ):
    return fore_color, back_color, link_color, visited_color

def colors2(*args, # one star * always a tuple
            **kwargs # two star ** always a dict
           ):
    return(args, kwargs)

