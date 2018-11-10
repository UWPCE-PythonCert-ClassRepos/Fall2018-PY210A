#!/usr/bin/env python3
"""dict and set lab with comprehension


"""
def c_dict():
    """dict of chris's favorites.

    """
    food_prefs = {"name": "Chris",
                  "city": "Seattle",
                  "cake": "chocolate",
                  "fruit": "mango",
                  "salad": "greek",
                  "pasta": "lasagna"}
    return food_prefs

def chris_text(food_prefs):
    """prints text about chris.

    """
    body = """Chris is from {}, and he likes {} cake, {} fruit, {} salad,
    and {} pasta""".format(
        food_prefs['city'], food_prefs['cake'],
        food_prefs['fruit'], food_prefs['salad'],
        food_prefs['pasta'])
    return body


def hex_dict():
    """creates dictionary of integers and equivalent hexidecimal numbers

    """
    h_dict = dict(list(enumerate([hex(i) for i in range(15)])))
    return h_dict.items()


if __name__ == "__main__":
    print(chris_text(c_dict())) #1

    print(hex_dict()) #2/#3
