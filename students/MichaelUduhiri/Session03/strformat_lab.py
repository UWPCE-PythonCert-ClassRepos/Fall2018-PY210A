'''
    Task One - Write a format string that will take the below tuple
    and produce: file_002 : 123.46, 1.00e+04, 12e+04
'''
numbers = (2, 123.4567, 10000, 12345.67)
print("My string of numbers is {}, {:.2f}, {:.2e}, {:.2e}".format("file_002", 123.467, 10000, 12345.67))


'''
    Task Two - Repeat the above task but use an alternate type of format string
'''
numbers = (2, 123.4567, 10000, 12345.67)
F"My string has the following numbers {numbers}"


'''
    Task Three - Rewrite to take an arbitrary number of values
'''
new_numbers = (2,4,6,8,10)
"The 3 numbers are: {:d}, {:d}, {:d}, {:d}, {:d}".format(*new_numbers)

'''
    Task Four
'''
more_numbers = (4, 30, 2017, 2, 27)



'''Task Five'''
my_tuple = ['orange', 1.3, 'lemons', 1.1]
f"The weight of an {} is {} and the weight of a {} is {}".format(my_tuple)
