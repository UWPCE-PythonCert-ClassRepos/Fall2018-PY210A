#!/usr/bin/env python3
import sys

def series1():
	ls = ['Apple', 'Pears','Oranges','Peaches']
	print(ls)

	new_fruit = input("Please enter a fruit that is not in the list >>>")
	ls.append(new_fruit)
	print(ls)

	index = input("Please choose a number from 1 - 5 >>>")
	print(index + ": " + ls[int(index) - 1])

	ls =  ['Pineapple'] + ls
	print(ls)
	
	ls.insert(0,'Strawberry')
	print(ls)
	for fruit in ls:
		if fruit[0] == "P":
			print(fruit, end=" ")
	print()		

	print ("----------------------------END OF SERIES1---------------------------")
	return ls

def series2(ls):
	print(ls)
	ls2 = ls.copy()
	ls2.pop()
	print(ls2)

	fruit_to_delete = input("Please enter a fruit that is to be deleted in the list >>>")
	ls2 = ls2 * 2

	ls2[:] = [fruit for fruit in ls2 if fruit != fruit_to_delete]
	print(ls2)
	print ("----------------------------END OF SERIES2---------------------------")

def series3(ls):
	ls3 = ls.copy()
	index = 0

	while index < len(ls):
		response = input("Do you like " + ls[index].lower() + "? ")
		if response == "yes":
			index += 1
		elif response == "no":
			ls3.remove(ls[index])
			index += 1
		else:
			print("Not a valid option!")

	print(ls3)
	print ("----------------------------END OF SERIES3---------------------------")

def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

def series4(ls):
	ls4 = ls.copy()
	index = 0
	while index < len(ls):
		ls4[index] = reverse(ls4[index])
		index += 1
	print("ls4: ")
	print(ls4)
	ls.pop()
	print(ls)
	print(ls4)

def main():
	ls = series1()

	series2(ls)

	series3(ls)

	series4(ls)
if __name__ == "__main__":
	main()
