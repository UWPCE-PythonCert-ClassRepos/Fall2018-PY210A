#!/usr/bin/env python3

# 1st function that has four optional parameters (with defaults) and its test driven function
def fun(fore_color,
        back_color,
        link_color,
        visited_color='chartreuse'):
    return True


def test_fun1():
    fun('red', 'blue', 'yellow', 'chartreuse')


def test_fun2():
    assert fun(fore_color='red',
               link_color='blue',
               back_color='blue')


def test_fun3():
    fun('purple', link_color='red', back_color='blue')


def test_fun4():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    fun(*regular, **links)



# 2nd new function with parameter as *args and **kwargs and its test driven function
def func(fore_color='red',*args,
         **kwargs):
    return True


def test_func1():
    assert func("blue", "red")


def test_func2():
    assert func(fore_color='red', link_color='blue', back_color='yellow', visited_color='chartreuse')


def test_func3():
    func('red', 'blue', 'yellow', 'chartreuse')


def test_func4():
    func(link_color='red', back_color='blue')


def test_func5():
    func('purple', link_color='red', back_color='blue')


def test_func6():
    func()


def test_func7():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    func(*regular, **links)


