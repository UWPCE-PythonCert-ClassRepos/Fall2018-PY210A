
#Task One - write format string
fnum = (2, 123.4567, 10000, 12345.67) #output 'file_002 :   123.46, 1.00e+04, 1.23e+04'
sorted(fnum)
print ("file_00{} :  {:.2f}, {:.2e}, {:.2e} ".format(fnum[0], fnum[1], fnum[2], fnum[3]))

#Task Two - using fstring - need some research
print(f"file_00{fnum[0]}:  {fnum[1]:.2f}, {fnum[2]:.2e}, {fnum[3]:.2e} ")

#Task Three - write function call for the formatter
t = (1, 2, 3) #example
"the 3 numbers are: {:d}, {:d}, {:d}".format(*t)

def formatter(in_tuple):

	form_string = "the {} numbers are: ".format(len(in_tuple))

	for x in range (len(in_tuple)):
		if x == len(in_tuple)-1:
			form_string += "{:d}"
		else:
			form_string += " {:d}, "

	return form_string.format(*in_tuple)

#Task Four - Use index numbers to specify position
#output  '02 27 2017 04 30'
fmt = (4, 30, 2017, 2, 27)
print ("0{} {} {} 0{} {}".format(fmt[3], fmt[4], fmt[2], fmt[0], fmt[1]))

if __name__ == "__main__":
	first_tuple = (2, 3, 5)
	print(formatter(first_tuple))
	second_tuple = (2,3, 5, 7, 9)
	print(formatter(second_tuple))

#Task Five - f-strings are new to Python (version 3.6), but are very powerful and efficient.
el = ['oranges', 1.3, 'lemons', 1.1] #el - element list
print(f"The weight of an {el[0]} is {el[1]} and the weight of the {el[2]} is {el[3]}")
print(f"The weight of an {el[0].upper()} is {el[1] * .2 + el[1]} and the weight of the {el[2].upper()} is {el[3] * .2 + el[3]:.2f}")


#6 task 6
listTuple = [('Name', 'Age', 'Cost', 'Total'),
            ('Paul', 6, 10.03, 200.00),
            ('Mark', 6, 20.30, 400.0),
            ]

print('{:10}\t{:10}{:10}{:14}'.format(listTuple[0][0], listTuple[0][1], listTuple[0][2], listTuple[0][3],))
print('{:10}{:10}{:10}{:14}'.format(listTuple[1][0], listTuple[1][1], listTuple[1][2], listTuple[1][3],))
print('{:10}{:10}{:10}{:14}'.format(listTuple[2][0], listTuple[2][1], listTuple[2][2], listTuple[2][3],))

#extra task
print("---Extra Task")
a = (1,2,3,4,5,6,7,8,9,10)
print("".join([" - {}   "] * 10).format(* a))

 	

