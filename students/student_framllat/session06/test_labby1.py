from labby1 import colour_test

def test1():
	assert colour_test("red","blue","yellow","chartreuse") == ('red', 'blue', 'yellow', 'chartreuse')
	    
def test2():
	assert colour_test(link_color='red', back_color='blue') == ('red', 'blue', 'red', 'chartreuse')

def test3():
	assert colour_test("purple", link_color='red', back_color='blue') == ('purple', 'blue', 'red', 'chartreuse')

def test4():
	tup1 = ('red', 'blue')
	assert colour_test(*tup1) == ('red', 'blue', 'yellow', 'chartreuse')

def test5():
	dict1 = {"link_color":"chartreuse"}
	assert colour_test(**dict1) == ('red', 'blue', 'chartreuse', 'chartreuse')

def test6():
	tup1 = ('red', 'blue')
	dict1 = {"link_color":"chartreuse"}
	assert colour_test(*tup1, **dict1) == ('red', 'blue', 'chartreuse', 'chartreuse')

