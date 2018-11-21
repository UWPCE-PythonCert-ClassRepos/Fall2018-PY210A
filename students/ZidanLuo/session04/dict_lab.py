#!/usr/bin/env python3

def count_t(value):
    result = 0
    for c in value:
        if c == 't':
            result += 1
    return result
my_dict = {'name':'Chris','city':'Seattle','cake':'Chocolate'}
print(my_dict)
my_dict.pop('cake')
print(my_dict)
my_dict['fruit'] = 'Mango'
print(my_dict)
print ('cake' in my_dict)
print ('Mango' in my_dict.values())

new_dict = {}
for key, value in my_dict.items():
    new_dict[key] = count_t(value)

print(new_dict) 

s2 = set()
s3 = set()
s4 = set()
for n in range(0,20):
    if n % 2 == 0:
        s2.add(n)

for n in range(0,20):
    if n % 3 == 0:
        s3.add(n)

for n in range(0,20):
    if n % 4 == 0:
        s4.add(n)

print(s2)
print(s3)
print(s4)
print(s3 < s2)
print(s4 < s2)


word = 'P y t h o n'
s1 = set(word.split())
s1.add('i')
print(s1)
word2 = 'm a r a t h o n'
s5 = frozenset(word2.split())
print(s5)
print("union: " + str(s1.union(s5)))
print("intersection: " + str(s1.intersection(s5)))
