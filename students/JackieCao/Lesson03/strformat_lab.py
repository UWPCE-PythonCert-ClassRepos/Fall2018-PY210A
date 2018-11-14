# task one

a_tuple = (2, 123.4567, 10000, 12345.67)

a = 'file_' + '{:03}'.format(a_tuple[0]) + ' : '

b = '{:.2f}'.format(a_tuple[1]) + ", "

c = '{:.2e}'.format(a_tuple[2]) + ", "

d = '{:.3}'.format(a_tuple[3])

print(a + b + c + d)

# or add them together
'file_' + '{:03}'.format(a_tuple[0]) + ' : ' + '{:.2f}'.format(a_tuple[1]) + ", " + '{:.2e}'.format(a_tuple[2]) + ", " + '{:.3}'.format(a_tuple[3])

# task two

a_tuple = (2, 123.4567, 10000, 12345.67)

f'file_{a_tuple[0]:03} : {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.3}'

print(f'file_{a_tuple[0]:03} : {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.3}')
# task three


def formatter(a_tuple):
    l = len(a_tuple) 
    return 'the '+ str(l) + ' numbers are: {:}'.format(str(a_tuple)) 

print(formatter((2,3,5)))
print(formatter((2,3,5,7,9)))


# task four

a_tuple = (4, 30, 2017, 2, 27)

print(f'{a_tuple[3]:02} {a_tuple[4]:02} {a_tuple[2]:04} {a_tuple[0]:02} {a_tuple[1]:02}')

# task four

alist = ['oranges', 1.3, 'lemons', 1.1]

# Write an f-string that will display:The weight of an orange is 1.3 and the weight of a lemon is 1.1
f'The weight of an {alist[0][:-1]} is {alist[1]} and the weight of a {alist[2][:-1]} is {alist[3]}'

print(f'The weight of an {alist[0][:-1]} is {alist[1]} and the weight of a {alist[2][:-1]} is {alist[3]}')
# change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher
f'The weight of an {alist[0][:-1].upper()} is {alist[1]*1.2} and the weight of a {alist[2][:-1].upper()} is {alist[3]*1.2}'

print(f'The weight of an {alist[0][:-1].upper()} is {alist[1]*1.2} and the weight of a {alist[2][:-1].upper()} is {alist[3]*1.2}')

# task six
import pandas as pd

data = [['Alex',10,'$10000.00'],['Bob',12,'$123.55'],['Clarke',13,'$23333.11']]
df = pd.DataFrame(data,columns=['Name','Age','Cost'])

print(df)










