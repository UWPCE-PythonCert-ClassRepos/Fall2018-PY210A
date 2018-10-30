"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
assignment objective: List Lab

Note - I am using many/extra print statements in the code for the purpose of
testing.  Comment and Doc Strings might be explaining the obvious to experienced
developers; if they seem redundant, it is for my learning purposes.

There are four sections, each beginning with #Series 1, #Series 2, etc.
"""



#Series 1
"""
-Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
-Display the list (plain old print() is fine…).
-Ask the user for another fruit and add it to the end of the list.
-Display the list.
-Ask the user for a number and display the number back to the user and the fruit
corresponding to that number (on a 1-is-first basis). Remember that Python uses
zero-based indexing, so you will need to correct.
-Add another fruit to the beginning of the list using “+” and display the list.
-Add another fruit to the beginning of the list using insert() and display the
list.
-Display all the fruits that begin with “P”, using a for loop.
"""

list = ["Apples", "Pears", "Oranges", "Peaches"]
for i in list:
    print(i)
"""
list = ["Apples", "Pears", "Oranges", "Peaches"] - *note to self* the list
positioned below a for loop throws a TypeError - list needs to be above for loop
"""
response = input("Please select one other fruit you want added to this list. > ")
new_fruit = response.title()
"""
The purpose of .title() is to ensure the first letter of the word is capitalized.
Later in the program, in a for loop, the loop searches for words, and those words
begin with a capital letter.  If a user entered a word, where the first letters
is not capitalized, then the program would not work properly.  .title() ensures
the program works correctly.
"""
#print(new_fruit) #test point to see the new fruit that was requested

list.append(new_fruit)
print(list) #this prints the amended list with the new fruit added to the end

response = input("Please pick a number between 0 and 4. > ")
number = response
print(number)
#note, further work could be done - when entering numbers outside 0-4

for j, item in enumerate(list): #generates two columns: numbers and fruits
    print(j, item)
print(list)

#add second fruit to the beginning of the list using +
list.insert(0, "Strawberry")
print(list)
"""
I learned a lot here - tried to use:
    l = (str(k)[1:-1])
which removes brackets from the list in the terminal display - but - after
stripping brackets from a list and then employing an insert method -
it won't work - throws an attribute error.  Insert only works with a bracketed
list.  Unable to use the + sign to add the second fruit to the beginning of the
list.
"""

#add a thrid fruit to the beginning of the list using insert()
list.insert(0, "Kiwi")
print(list)

#display all the friuts that begin with "P" using a for loop
for item in list:
	if "P" in item:
		print(item)
print("---End of Series 1 Exercises---")
#end of Series 1



#Series 2
"""
Using the list created in series 1 above:
-Display the list.
-Remove the last fruit from the list.
-Display the list.
-Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once
found, delete all occurrences.)
"""

print(list)
list2 = list
#remove the last fruit from the list and display the new list
list2.pop()
print(list2)

#ask the user for a fruit to delete and delete it
response = input("Select a fruit to delete from the list. > ")
response = response.title()
list2.remove(response)
print(list2)

double_list = list2 * 2
print(double_list)
print("---End of Series 2 Exercises---")
#end of Series 2



#Series 3
"""
Again, using the list from series 1:
-Ask the user for input displaying a line like “Do you like apples?” for each
fruit in the list (making the fruit all lowercase).
-For each “no”, delete that fruit from the list.
-For any answer that is not “yes” or “no”, prompt the user to answer with one of
those two values (a while loop is good here)
-Display the list.
"""

list3 = ["Apples", "Pears", "Oranges", "Peaches"] #original list
response_apples = input("Do you like apples?  Please respond with yes or no > ")
if response_apples == "no":
    list3.remove("Apples")
print(list3)
response_pears = input("Do you like pears?  Please respond with yes or no > ")
if response_pears == "no":
    list3.remove("Pears")
print(list3)
response_oranges = input("Do you like oranges?  Please respond with yes or no > ")
if response_oranges == "no":
    list3.remove("Oranges")
print(list3)
response_peaches = input("Do you like peaches?  Please respond with a yes or no > ")
if response_peaches == "no":
    list3.remove("Peaches")
print(list3)
print("---End of Series 3 Exercies---")
#end of Series 3



"""
Series 4
Once more, using the list from series 1:
-Make a copy of the list and reverse the letters in each fruit in the copy.
-Delete the last item of the original list. Display the original list and the copy.
"""

list = ["Apples", "Pears", "Oranges", "Peaches"]
list4 = list[:] #making a copy of list, now called list4
print(list4)

Apples = (list[0])
print(Apples)
reverse_Apples = Apples[::-1]
print(reverse_Apples)

Pears = (list[1])
print(Pears)
reverse_Pears = Pears[::-1]
print(reverse_Pears)

Oranges = (list[2])
print(Oranges)
reverse_Oranges = Oranges[::-1]
print(reverse_Oranges)

Peaches = (list[3])
print(Peaches)
reverse_Peaches = Peaches[::-1]
print(reverse_Peaches)

#delete the last item of the original list - using pop() to remove Peaches
list.pop()
print(list) #prints the new list minus Peaches
print(list4) #prints the copy of the list
print("---End of Series 4 Exercies---")
#end of Series4
