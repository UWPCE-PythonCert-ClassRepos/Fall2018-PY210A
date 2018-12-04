# Lesson 06 Exercise: Args and Kwargs Lab

# Keyword arguments
# Write a function that has four optional parameters (with defaults):


def colors(fore_color="red", back_color="yellow", link_color="green", visited_color="blue"):
    return fore_color, back_color, link_color, visited_color


# Generic parameters


def colors2(*args, **kwargs):
    return args, kwargs
