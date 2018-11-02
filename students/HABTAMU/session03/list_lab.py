# #!/usr/bin/env python3
# """Series 1: This is Section 1 List Lab """

# a_list = ["Apples","Pears","Oranges","Peaches"]
# print(a_list)

# # Ask the user for another fruit and add it to the end of the list.
# new_fruit = input("Which fruit would you like to add? \>").strip().title()
# a_list.append(new_fruit)

# print ("There are", len(a_list), "fruits:", a_list)

# new_num = int(input("Enter any number? \>").strip())
# z_fruit = a_list[new_num]
# output = "You added a number {} and fruit that corspond to is {}".format(new_num,z_fruit)
# print(output)
# another_fruit = input("Let's add another fruit to the beginning of the list using and display the list:> ").strip()

# # to add another fruit to the beginning of the list using “+” and display the list.
# x = [another_fruit] + a_list

# # Add another fruit to the beginning of the list using insert() and display the list.
# a_list.insert(0,another_fruit)
# print(x)
# print(a_list)

# # Display all the fruits that begin with “P”, using a for loop.
# for i in range(len(a_list)):
#     if a_list[i][0] == "P":
#         print(a_list[i])
#     else:
#         print("")

# """Series 2: This is Section 2 List Lab """
# # Using the list created in series 1 above:

# # Display the list.
# print(a_list)

# # Remove the last fruit from the list.
# a_list.remove(a_list[-1])

# # Display the list.
# print(a_list)

# # Ask the user for a fruit to delete, find it and delete it.
# fruit_del = input("which fruit you like to delete? >").strip()
# if fruit_del in a_list:
#     a_list.remove(fruit_del)
#     print(a_list)
# else:
#     print("")
# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

"""Series 3: This is Section 3 List Lab """

# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list(making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values(a while loop is good here)
# Display the list.
# a_list = ["Apples", "Pears", "Oranges", "Peaches"]
# #answer = []
# for i in range(len(a_list)):
#     a = a_list[i]
#     answer = input("Do you like {} (y/n) ?:".format(a).strip().lower())
#     if answer == 'y':
#         print(a_list)
#     elif answer == 'n':
#         a_list.remove(a)
#         print(a_list)
#     else:
#         print("pls type (y/n)")

# Got issue with at a = a_list[i], IndexError: list index out of range, and escape 2nd element on n.

# """Series 4: This is Section 4 List Lab """

# Make a copy of the list and reverse the letters in each fruit in the copy.
# a_list = ["Apples", "Pears", "Oranges", "Peaches"]
# b_list = a_list[:]
# for i in range(len(b_list)):
#     print(b_list[i][::-1])

# Delete the last item of the original list. Display the original list and the copy.
a_list = ["Apples", "Pears", "Oranges", "Peaches"]
for i in range(len(a_list)):
    print(a_list)
    a_list.remove(a_list[-1])
    print(a_list)
