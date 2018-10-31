#Task One
tp = (2, 123.4567, 10000, 12345.67)
print("file_{:0>3d}: {:.2f}, {:.2e}, {:2e}".format(*tp))
#Task Two
print("file_" + '%03d' % (tp[0]) + ": " + '%.2f' % (tp[1]) + 
	", " + '%.2e' % (tp[2]) + ', ' + '%.2e' % (tp[3]))
#Task Three
def formatter(tpl):
	form_string = "the " + str(len(tpl)) + " numbers are: " + "{:d}, "*len(tpl)
	return form_string.format(*tpl)

#Task Four
new_tpl = (4, 30, 2017, 2, 27)
print('{:02} {:d} {:d} {:02} {:d}'.format(new_tpl[-2], 
	new_tpl[-1], new_tpl[2], new_tpl[0], new_tpl[1]))

#Task Five
ls = ['Orange', 1.3, 'lemon', 1.1]
result = f"The weight of an {ls[0]} is {ls[1]} and the weight of a {ls[2]} is {ls[3]}"
r = f"The weight of an {ls[0]} is " + str(ls[1] * 1.2) + f" and the weight of a {ls[2]} is " + str(ls[3]*1.2)
print (result)
print (r)

#Task Six
donors = [('jin', 22, 520), ('Yu', 22, 1000), ('Levy', 30, 10000)]
ls = []


for donor in donors:
	i = len(str(donor[2]))
	ls.append(i)
	length = max(ls) + 5


print('{:10}{:>5}{:>{length}}'.format('Name', 'Age', 'Cost', length = length))

for donor in donors:
	print('{:10}{:>5}{:>{length}}'.format(donor[0], donor[1], donor[2], length  = length))
	print()