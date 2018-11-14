#Task 1
tup = (2, 123.4567, 10000, 12345.67)

print('file_{:>03}: {}, {:.2e}, {:.2e}'.format(tup[0], str(round(tup[1], 2)), tup[2], tup[3]))

#Task 2
first = f'file_{tup[0]:03}:'
second = str(round(tup[1], 2))
third = "{:.2e}".format(tup[2])
fourth = "{:.2e}".format(tup[3])

print(f'{first} {second}, {third}, {fourth}')

#Task 3
def formatter(seq):

    l = len(seq)
    return ("The {} numbers are: " + ", ".join(["{}"]*l)).format(l, *seq)

#Task 4
tup2 = (4, 30, 2017, 2, 27)
print('{:02} {} {} {:02} {}'.format(tup2[3], tup2[4], tup2[2], tup2[0], tup2[1]))

#Task 5
lst = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {lst[0][:-1]} is {lst[1]} and the weight of a {lst[2][:-1]} is {lst[3]}')
print(f'The weight of an {lst[0][:-1].upper()} is {lst[1]*1.2} and the weight of a {lst[2][:-1].upper()} is {lst[3]*1.2}')


#Task 6
lster = [['Dan Watts', 'Tina Tallman', 'Fanny Mcbride'], [124124, 5352 ,235232],
         ['$12439', '$129.99', '$19048.44']]

dashes = '-' * 40

print(dashes)
for i in range(0,len(lster)):
    print('{:<20s}{:<12d}{:<12s}'.format(lster[0][i], lster[1][i], lster[2][i]))
print(dashes)






