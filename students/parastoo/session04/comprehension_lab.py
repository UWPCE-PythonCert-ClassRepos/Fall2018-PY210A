#!/usr/bin/env python3

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

# use string format
print('1. String Foramt\n')
print('{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} \
      salad, and {pasta} pasta'.format(**food_prefs))

#use list comprehension to make a dict
print('2. List Comprehension\n')
numbers = [x for x in range(16)]
hexds = [hex(x) for x in numbers]
new_dict = dict(zip(numbers, hexds))

#use dict comprehension for number 2 in one line
print('3. Dict Comprehension\n')
d = {x:  hex(x) for x in range(16)}

#use dict comprehension with number of 'a's in each value
print('4. Count\n')
a_dict = {k: v.count('a') for k, v in food_prefs}

print('5. Division sets\n')
#a) use set comprehension
s2 = {x for x in range(21) if x%2 == 0}
s3 = {x for x in range(21) if x%3 == 0}
s4 = {x for x in range(21) if x%4 == 0}

#b)a code for set building
div_list = [2,3,4,5]
for div in div_list:
    s = {x for x in range(21) if x%div == 0}

#c) write the loop code in one line
s = {x for x in range(21) for div in div_list if x%div == 0}



