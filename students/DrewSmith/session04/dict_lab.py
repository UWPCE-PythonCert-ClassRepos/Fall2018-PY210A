#!/usr/bin/env python3

def dict_1():
    person = {"name" : "Chris", "city": "Seattle", "cake": "Chocolate"}
    print(f"Person dict: {person}")
    del person["cake"]
    print(f"Removed cake: {person}")
    person["fruit"] = "Mango"
    print(F"With fruit: {person}")
    print(f"Keys: {person.keys()}")
    print(f"Values: {person.values()}")
    print(f"Is there cake? {'cake' in person}")
    print(f"Is there Mango? {'Mango' in person.values()}")

def dict_2():
    person = {"name" : "Chris", "city": "Seattle", "cake": "Chocolate"}
    person_t = {}
    for item in person:
        person_t[item] = person[item].lower().count('t')
    print(person_t)

def set_1():
    s2 = set(range(0, 21, 2))
    print(f"s2: {s2}")
    s3 = set(range(0, 21, 3))
    print(f"s3: {s3}")
    s4 = set(range(0, 21, 4))
    print(f"s4: {s4}")
    print(f"Is s3 a subset of s2? {s3.issubset(s2)}")
    print(f"Is s4 a subset of s2? {s4.issubset(s2)}")

def set_2():
    py = set('Python')
    py.add('i')
    marathon = frozenset('marathon')
    print(f"Union: {py.union(marathon)}")
    print(f"Intersection: {py.intersection(marathon)}")

dict_1()
dict_2()
set_1()
set_2()