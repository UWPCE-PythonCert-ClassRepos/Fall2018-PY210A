#!/usr/bin/env python3

# Series 1

# Create a list
alist = ["Apples", "Pears", "Oranges", "Peaches"]

# Display the list
print(alist)

# Ask the user for another fruit and add it to the end of the list
response = input("Please enter a fruit >")
alist.append(str(response).title())


# Display the list.
print(alist)

# Ask the user for a number and display the number back to the user
# and the fruit corresponding to that number
response = input("Please enter a number 1-5 >")
print(int(response))
print(alist[int(response)-1])

# Add another fruit to the beginning of the list using “+” and display the list
alist = ["Bananas"] + alist
print(alist)

# Add another fruit to the beginning of the list using insert() and display the list
alist.insert(0,"Blueberries")
print(alist)

# Display all the fruits that begin with “P”, using a for loop
l = []
for i in alist:
    if i.startswith("P"):
        l.append(i)

print(l)

# Series 2

alist = ["Apples", "Pears", "Oranges", "Peaches"]

# Display the list.
print(alist)

# Remove the last fruit from the list.
alist = alist[:-1]

# Display the list.
print(alist)

# Ask the user for a fruit to delete, find it and delete it.
response = input("Please enter a fruit to delete >")
response = str(response).title()
if response in alist:
    alist.remove(response)
print(alist)


# Multiply the list times two. Keep asking until a match is found. 
# Once found, delete all occurrences        
alist = ["Apples", "Pears", "Oranges", "Peaches"]
alistDouble = alist*2
response = input("Please enter a fruit to delete >")
response = str(response).title()
while response not in alist:
    response = input("Please enter a fruit to delete >")
    response = str(response).title()
    alist_new = [x for x in alist if x != response]
print(alist_new)

# Series 3
alist = ["Apples", "Pears", "Oranges", "Peaches"]
# Ask the user for input displaying a line like “Do you like apples?” 
# for each fruit in the list (making the fruit all lowercase).
alist_lower = [x.lower() for x in alist] 
fruit_you_like = alist_lower.copy()
for i in alist_lower:
    response = input("Do you like "+ i + "? >")
    response = str(response)
    while response.lower() != "yes" and response.lower() != "no":
        response = str(input("Please enter 'yes' or 'no' >"))
    if response.lower() == "no":
        fruit_you_like.remove(i) # For each “no”, delete that fruit from the list.
print(fruit_you_like)

# Series 4
alist = ["Apples", "Pears", "Oranges", "Peaches"]
# Make a copy of the list and reverse the letters in each fruit in the copy
alist_copy = alist.copy()
for i in alist_copy:
    i = i[::-1]
    alist_copy = alist_copy[1:] + [i]

# Delete the last item of the original list. Display the original list and the copy.
alist = alist[:-1]
print(alist)
print(alist_copy)














