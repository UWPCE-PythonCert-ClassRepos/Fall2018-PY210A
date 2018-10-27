#!/usr/bin python3

#Series 1
original_fruits = ["Apples", "Pears", "Oranges", "Peaches"]
fruits = original_fruits[:]
print(fruits)
new_fruits = input("Enter a new fruits: ")
fruits.append(new_fruits)
print(fruits)
index = int(input(f"Give a number between 1 and {len(fruits)}: "))
print("You chose: " + (fruits[index - 1] if index > 0 and index <= len(fruits) else "Error!"))

print()
fruits = ["Grapes"] + fruits
print(fruits)

fruits.insert(0, "Plums")
print(fruits)

print()
print("Fruits that tart with P:")
for fruit in fruits:
    if fruit[:1].lower() == "p":
        print(fruit)


#Series 2
print()
print("Series 2:")
fruits = original_fruits[:]
print(fruits)
del fruits[-1:]

print(fruits)
fruits = fruits * 2
print("Doubling Fruit List")
print(fruits)
found = False
while found is False:
    find = input("What fruit should we remove?: ")

    for fruit in fruits:
        if fruit == find:
            fruits.remove(fruit)
            found = True

print(fruits)

#Series 3
print()
print("Series 3")
fruits = original_fruits[:]
print(fruits)
for fruit in fruits[:]:
    answer = input(f"Do you like {fruit.lower()}? ").lower().strip()
    while answer not in ["yes", "no"]:
        answer = input("Please answer yes or no: ")
    if answer == "no":
        fruits.remove(fruit)
print(fruits)

#Series 4
print()
print("Series 4")
fruits = original_fruits[:]
fruits_copy = fruits[:]
for index in range(len(fruits_copy)):
    fruits_copy[index] = fruits_copy[index][::-1]
del fruits[-1:]
print(f"Fruits Orig: {fruits}")
print(f"Fruits Copy: {fruits_copy}")