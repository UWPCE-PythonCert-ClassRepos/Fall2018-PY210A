# Lesson 03 Exercise: List Lab

# Series 1
print("Series 1")


# Create a list of fruits and print it
def print_fruit_list(fruits):
    """
    Prints a formatted string with my fruit list.
    """
    print("My fruit list contains: {}".format(fruits))


my_fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print_fruit_list(my_fruits)

# Ask the user for a fruit and add it to my list
user_fruit = "Apples"

while user_fruit in my_fruits:
    user_fruit = input("\nWhich fruit do you want to add?: ").capitalize()

my_fruits.append(user_fruit)

# Print new list
print_fruit_list(my_fruits)

# Ask the user for a number.  Print the number and the corresponding fruit (1 = first)
user_number = 0

while user_number < 1 or user_number > len(my_fruits):
    user_number = input("\nChoose a number between 1 and {}: ".format(len(my_fruits)))
    user_number = int(user_number)

print("{}: {}".format(user_number, my_fruits[user_number - 1]))

# Add another fruit to the beginning of the list using + and print the list
print("\nI'm going to add a fruit to the beginning of this list.")
my_fruits = ["Strawberries"] + my_fruits

print_fruit_list(my_fruits)

# Add another fruit to the beginning fo the list using insert and print the list
print("\nI'm going to add another fruit to the beginning of this list.")
my_fruits.insert(0, "Blueberries")
print_fruit_list(my_fruits)

# Print all the fruits that begin with "P" using a for loop
p_fruits = []

for x in my_fruits:
    if x.startswith("P"):
        p_fruits.append(x)

print("\nHere are all the fruits that begin with the letter P: {}".format(p_fruits))

# Series 2
print("\nSeries 2")

# Print my fruit list
print_fruit_list(my_fruits)

# Remove the last fruit from the list
print("\nI'm going to remove the last item from the list.")
my_fruits2 = my_fruits[:]
my_fruits2.pop(-1)

print_fruit_list(my_fruits2)

# Multiply the list times two.
print("\nI'm going to double my list.")
my_fruits_doubled = my_fruits2 * 2
print_fruit_list(my_fruits_doubled)

# Ask the user for a fruit to delete.  Find it and delete all occurrences.
user_delete_fruit = ""

while user_delete_fruit not in my_fruits_doubled:
    user_delete_fruit = input("\nWhich fruit would you like to delete?: ").capitalize()

for x in my_fruits_doubled:
    if x == user_delete_fruit:
        my_fruits_doubled.remove(x)

print_fruit_list(my_fruits_doubled)


# Series 3
print("\nSeries 3")


def like_fruit(fruit):
    answer = ""

    while not (answer == "Yes" or answer == "No"):
        answer = input("Do you like {}? Yes or No: ".format(fruit.lower())).capitalize()

    if answer == "No":
        return False

    elif answer == "Yes":
        return True


# Make a new list to hold favorite fruits
favorite_fruits = []

for i in range(len(my_fruits)):
    if like_fruit(my_fruits[i]):
        favorite_fruits.append(my_fruits[i])
    else:
        continue

print_fruit_list(favorite_fruits)

# Series 4
print("\nSeries 4")
# Make a copy of the list and reverse the letters in each fruit in the copy

reverse_fruits = my_fruits[:]

for i in range(len(reverse_fruits)):
    reverse_fruits[i] = reverse_fruits[i][::-1]

# Delete the last item of the original list
my_fruits.pop()

# Print the original list and the copy.
print("The original list is: {}".format(my_fruits))
print("The reversed list is: {}".format(reverse_fruits))
