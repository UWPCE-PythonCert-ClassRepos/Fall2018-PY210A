#!/usr/bin/env python3
#
############### Series 4 #######################
#
#
# re-Create list of fruits from Series 1 and lowercase
#
#
fruits = ["Apples", "Pears", "Oranges", "Peaches"]	
fruits = [fruit.lower() for fruit in fruits]
#
# Create empty list for copy of fruits
#
fruits_c = []

for fruit in fruits:
    item = "".join(reversed(fruit))
    fruits_c.append(item)
#
# take last item out of ORIG list
#
fruits.pop()

print("The REV list: ",fruits_c)
print("The ORIG list: ",fruits)
#
#

