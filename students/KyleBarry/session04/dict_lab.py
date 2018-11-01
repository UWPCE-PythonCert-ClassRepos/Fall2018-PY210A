#!/usr/local/bin/python3

dict_ = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

for i in dict_.items():
    print(i)

del dict_['cake']

for i in dict_.items():
    print(i)

dict_['fruit'] = 'Mango'

for i in dict_.keys():
    print(i)

for i in dict_.values():
    print(i)

if 'cake' in dict_.keys():
    print('True')
else:
    print('False')

if 'Mango' in dict_.values():
    print('True')
else:
    print('False')


dict2 = {}
for i in dict_.keys():
    dict2[i] = dict_[i].count('t')

print(dict2)

s2 = set([i for i in list(range(20)) if i % 2 == 0])

s3 = set([i for i in list(range(20)) if i % 3 == 0])

s4 = set([i for i in list(range(20)) if i % 4 == 0])

pset = set('Python')
pset.add('i')
print(pset)
print(s2, s3, s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

frozen = frozenset('marathon')
inter = pset.intersection(frozen)
union = pset.union(frozen)
print(inter, union)


