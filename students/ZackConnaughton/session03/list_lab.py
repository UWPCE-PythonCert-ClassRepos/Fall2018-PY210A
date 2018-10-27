#!/usr/bin/env python

def series1():
    """
    Shows what can be done with a simple list of fruitsself.
    """
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruits)
    response = input('Input another Fruit: ')
    fruits.append(response)
    print(fruits)
    fruit_number = input('Enter the number fruit you want to see (from 1 '
                         'to ' + str(len(fruits)) + '):')
    print(fruits[int(fruit_number) - 1])
    fruits = ['Plum'] + fruits
    print(fruits)
    fruits.insert(0, 'Banana')
    print(fruits)
    p_fruits = []
    for f in fruits:
        if f[0] == 'P':
            p_fruits.append(f)
    print(p_fruits)


if __name__ == '__main__':
    series1()
