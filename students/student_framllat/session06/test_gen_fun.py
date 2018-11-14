#!/usr/bin/env python3

from gen_fun import gen_fun

def test1():
	assert gen_fun("red","blue","yellow","chartreuse") == (('red', 'blue', 'yellow', 'chartreuse'), {})

def test2():
	assert gen_fun() == ((), {})

def test3():
	assert gen_fun("purple", link_color='red', back_color='blue') == (('purple',), {'link_color': 'red', 'back_color': 'blue'})

def test4():
	reg_tup = ('red', 'blue')
	assert gen_fun(reg_tup) == ((('red', 'blue'),), {})

def test5():
	reg_dict = {"link_color":"chartreuse"}
	assert gen_fun(reg_dict) == (({'link_color': 'chartreuse'},), {})

def test6():
	reg_tup = ('red', 'blue')
	reg_dict = {"link_color":"chartreuse"}
	assert gen_fun(reg_tup, reg_dict) == ((('red', 'blue'), {'link_color': 'chartreuse'}), {})

def test7():
	reg_tup = ('red', 'blue')
	reg_dict = {"link_color":"chartreuse"}
	# This assert adds the *, ** for args/kwargs
	assert gen_fun(*reg_tup, **reg_dict) == (('red', 'blue'), {'link_color': 'chartreuse'})



# def gen_fun(*args, **kwarg):
#     print("The positionals aka *args:", args)
#     print("The keywords aka **kwargs:", kwargs)
	            
    
