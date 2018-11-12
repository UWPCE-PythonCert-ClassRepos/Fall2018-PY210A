#Lesson04
#Dictonary and Set Lab Exercise ##
#
#!/usr/bin/env python3

#define dictionary
mydict = dict(name = 'Chris', city = 'Seattle', cake = 'Chocolate')


#Display the dictionary
print(mydict)
#delete the entry for cake
mydict.pop('cake')
#display the dictionary
print(mydict)
#add an entry for 'fruit' with 'Mango' and display the dictionary
mydict['Fruit'] = 'Mango'
print(mydict)
#display dict keys
print(mydict.keys())
#display dict values
print(mydict.values())
#display whether or not 'cake'  is a key in the dictionary
def key_check(word):
    for key in mydict.keys():
        if key == word:
            print("I found {} as a key in the dictionary".format(word))
    else:
        print("I didn't find {} as a key in the dictionary".format(word))
key_check('cake')

#display whether or not 'mango' is a value in the dictionary
def value_check(word):
    for val in mydict.values():
        if val == word:
            print("I found {} as a value in the dictionary." .format(word))
            break
    else:
        print("Didn't find {} as a value in the dictionary".format(word))
        #     print("{} is a value in the dictionary.".format(word))
        # else:
        #     print("I did not find {} as a value in the dictionary.".format(word))
value_check('Mango')

### Dictionaries 2
# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).
print("Dictionaries Part 2!")
mydict = dict(name = 'Chris', city = 'Seattle', cake = 'Chocolate')
print(mydict)
for k,v in mydict.items():
    # print(set(v))
    # print(v.count('t'))
    mydict[k] = v.count('t')
    # vlist.update([v])
    # t_count = vlist.count('t')
    # mydict[k] = t_count
print(mydict)

#####Sets
#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
s2 = set()
s3 = set()
s4 = set()
for num in range(1,21):
    if num % 4 == 0:
        s4.add(num)
        s2.add(num)
    elif num % 2 == 0:
        s2.add(num)
    elif num % 3 == 0:
        s3.add(num)
#Display the sets.
print(s2)
print(s3)
print(s4)

#Display if s3 is a subset of s2 (False)
if s3.issubset(s2):
    print("set 3 is a subset of set 2")
if not s3.issubset(s2):
    print("set 3 is not a subset of set 2")
#and if s4 is a subset of s2 (True).
if s4.issubset(s2):
    print("set 4 is a subset of set 2")
if not s4.issubset(s2):
    print("set 4 is not a subset of set 2")

#####SETS 2
#Create a set with the letters in ‘Python’ and add ‘i’ to the set.
word = set()
word.update('Python')
print(word)
word.update('i')
print(word)
#Create a frozenset with the letters in ‘marathon’.
frozen = frozenset('marathon')
print(frozen)
#display the union and intersection of the two sets.
print(frozen.union(word))
print(frozen.intersection(word))
