#!/usr/bin/env python

"""
Author: Jim Jenkins (dvlupr)
Date: 10/30/2018

"""
#TASK 1


#create string
str_num = (2, 123.4567, 10000, 12345.67)
#clean up 'file_002 :   123.46, 1.00e+04, 1.23e+04'
print ('Task 1: file_00{} :  {:.2f}, {:.2e}, {:.2e} '.format(str_num[0], str_num[1], str_num[2], str_num[3]))


#TASK 2


#alternate way to format
print('Task 2: file_00%d :  %.2f, %.2e, %.2e' % (str_num[0], str_num[1], str_num[2], str_num[3]))


#TASK 3


#reformat the string using a variable
def formatter(seq):
    return ('file_00{} :  {:.2f}, {:.2e}, {:.2e} '.format(*seq))

#form_string
num = (str_num[0], str_num[1], str_num[2], str_num[3])
# return form_string.format(*seq)
print('Task 3:', formatter(num))



#TASK 4


# tuple  for formatting
tup_nums = (4, 30, 2017, 2, 27)

t1 = tup_nums[3]
t2 = tup_nums[4]
t3 = tup_nums[2]
t4 = tup_nums[0]
t5 = tup_nums[1]

print('Task 4: {:02d} {} {} {:02d} {}'.format(t1, t2, t3, t4, t5))


#TASK 5


# list of variables
fruit_list = ['oranges', 1.3, 'lemons', 1.1]
#  The weight of an orange is 1.3 and the weight of a lemon is 1.1
print(f'TASK 5: The weight of an {fruit_list[0]} is {fruit_list[1]} and the weight of a {fruit_list[2]} is {fruit_list[3]}')
print(f'TASK 5: The weight of an {fruit_list[0].upper()} is {fruit_list[1]*1.2} and the weight of a {fruit_list[2].upper()} is {fruit_list[3]*1.2}')


#TASK 6


key_list = ['name','age', 'amount']

name_list = ['John Doe', 'Tom Tinker', 'David Goliath', 'Billy Joel', 'Mona Liza', 'Dire Straits', 'Alice Cooper', 'Steve Perry', 'Sting', 'Jim Jenkins']
age_list = [21, 25, 30, 33, 64, 55, 28, 24, 53, 51]
amount_list = [1000, 2000, 3000, 400, 500, 60, 7000, 8000, 900, 9000]

people = [{key_list[0]:a, key_list[1]:b, key_list[2]:c}
              for a, b, c in zip(name_list, age_list, amount_list)]

print('TASK 6:')
print ("{:<15} | {:^12} | {:^12} ".format('Name:', 'Age:', 'Cost:'))
for person in people:
    print('{:<15}   {:^12}   ${:>9,.2f}'.format(person['name'], person['age'], person['amount']))