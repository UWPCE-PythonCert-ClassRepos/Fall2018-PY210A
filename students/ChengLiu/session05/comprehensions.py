feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]
print(comprehension[0])

print(comprehension[1])

comp = [delicacy for delicacy in feast if len(delicacy) > 6]
print(len(feast))

print(len(comp))

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension2 = [skit * number for number, skit in list_of_tuples]
print(comprehension2[0])
print(len(comprehension2[2]))

eggs = ['poached egg', 'fried egg']
meats = ['lite spam', 'ham spam', 'fried spam']
comprehension3 = ['{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]
print(comprehension3)


comprehension4 = {c for c in 'aabbbcccc'}


dict_of_weapons = {'first': 'fear',
                   'second': 'surprise',
                   'third': 'ruthless efficiency',
                   'fourth': 'fanatical devotion',
                   'fifth': None}
dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}
