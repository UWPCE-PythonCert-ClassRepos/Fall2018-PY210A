#!/usr/bin/env python


def dict_1():
    people={'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print(people)
    people.pop('cake')
    print(people)
    people['fruit'] = 'Mango'
    print(people)
    print(people.keys())
    print(people.values())
    print('cake' in people.keys())
    print('Mango' in people.values())

    #dictonaries 2 exercise
    people_t = {}
    for k, v in people.items():
        people_t[k] = (v.lower().count('t'))
    print(people_t)


def sets_1():
    s2 = set()
    s3 = set()
    s4 = set()
    for i in range(20):
        if i % 2 == 0:
            s2.add(i)
        if i % 3 == 0:
            s3.add(i)
        if i % 4 == 0:
            s4.add(i)
    print(s2)
    print(s3)
    print(s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))


def sets_2():
    s = set('python')
    print(s)
    s.add('i')
    print(s)
    fs = frozenset('marathon')
    print(fs)
    print(s.union(fs))
    print(s.intersection(fs))

if __name__ == '__main__':
    dict_1()
    sets_1()
    sets_2()
