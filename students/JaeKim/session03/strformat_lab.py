# Task One
values = ( 2, 123.4567, 10000, 12345.67)
print('file_{:03} : {:.4f}, {:.2e}, {:.2e}'.format(values[0], values[1], values[2], values[3]))

# Task Two
print(f"file_{values[0]:03} : {values[1]:.4f}, {values[2]:.2e}, {values[3]:.2e}")

# Task Three
def formatter(in_tuple):
    numbers = len(in_tuple)
    form_string = "the {} numbers are: ".format(numbers) + ("{} " * numbers)

    return form_string.format(*in_tuple)

print(formatter((1,2,3,4,5)))

# Task Four
tuple_task_4 = (4, 30, 2017, 2, 27)
print('{:02} {} {} {:02} {}'.format(tuple_task_4[3], tuple_task_4[4], tuple_task_4[2], tuple_task_4[0], tuple_task_4[1]))

# Task Five
# ['oranges', 1.3, 'lemons', 1.1]
# The weight of an orange is 1.3 and the weight of a lemon is 1.1
items = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {items[0]} is {items[1]} and the weight of a {items[2]} is {items[3]}')

# Task Six
database = ['Bob', 30, 300], ['Mary', 70, 10000], ['Jose', 19, 100], ['Scott', 55, 900]
print('\n{:>12}  {:>12}  {:>12}'.format('Name', 'Age', 'Cost'))

for person in database:
    print('{:>12}  {:>12}  {:>12}'.format(person[0], person[1], person[2]))