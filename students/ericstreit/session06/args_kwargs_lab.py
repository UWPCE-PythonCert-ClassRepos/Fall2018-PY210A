#Lesson##
#XXXXX Exercise ##
#
#!/usr/bin/env python3

#define function
def myfunc(n):
    """
Write a function that has four optional parameters (with defaults):

    fore_color
    back_color
    link_color
    visited_color

Have it return the colors (use strings for the colors, e.g. “blue”, “red”, etc.)
Call it with a couple different parameters set.
    """
def colors(fore='red', back='white', link='blue', visited='green'):
    return(fore, back, link, visited)

def colors2(*args):
    return(args)

def colors3(**kwargs):
    return(kwargs)

#for testing
if __name__=="__main__":
    print(colors('red', 'green', 'blue', 'yellow'))

def test_1():
    assert colors('red', 'green', 'blue', 'yellow') == ('red', 'green', 'blue', 'yellow')

def test_2():
    assert colors(back='yellow') == ('red', 'yellow', 'blue', 'green')

def test_3():
    assert colors(back='yellow', link='puce') == ('red', 'yellow', 'puce', 'green')

def test_4():
    my_tup = ('purple', 'pink')
    assert colors(*my_tup) == ('purple', 'pink', 'blue', 'green')

def test_5():
    my_dict = {'link':'yellow', 'fore':'purple'}
    assert colors(**my_dict) == ('purple', 'white', 'yellow', 'green')

def test_6():
    my_tup = ('green', 'rainbow')
    my_dict = {'link':'yellow'}
    assert colors(*my_tup, **my_dict) == ('green', 'rainbow', 'yellow', 'green')

def test_7():
    assert colors2('green', 'brown') == ('green', 'brown')

def test_8():
    my_dict = {'link':'yellow', 'fore':'purple'}
    assert colors3(my_dict) == ('yellow', 'purple')

#def test_7():
    #my_tup = {'green', 'brown'}
    #assert colors2(my_tup) == ('green', 'brown')
