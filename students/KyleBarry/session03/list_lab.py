#!/usr/bin/env python3

def main():
	#Series 1
	fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

	print("Here are all our current fruits:")
	print(', '.join(fruits))

	response = input('What other fruit do we need? ').title()
	fruits.append(response)

	print(', '.join(fruits))

	while True:
		num_response = input('enter an integer between 1-5: ')
		try:
			num_response = int(num_response)
		except ValueError:
			print('Please enter an integer between 1-5: ')
			continue
		if num_response in range(1,6):
			break
		else:
			print('Please enter an integer between 1-5: ')

	print(num_response, ': ' + fruits[num_response-1])

	fruits = ["Melons"] + fruits
	print(fruits)

	for i in fruits:
		if i[0] == 'P':
			print(i)

	# Series 2
	# print(fruits)
	# #pop() removes the last item of the list by default
	# fruits.pop()
	# print(fruits)

	# while True:
	# 	to_delete = input('Which fruit would you like to delete? ')
	# 	try:
	# 		fruits.remove(to_delete)
	# 		break
	# 	except ValueError:
	# 		print("That's not in the list!")
	# 		continue
			
	# print(fruits)

	#Series 3
	# f = []
	# for i in fruits:
	# 	resp = input("Do you like {} ".format(i)).lower()
	# 	while True:
	# 		if resp[0] == 'n':
	# 			#if .remove() here, for loop skips new index of next value
	# 			f.append(i)
	# 			break
	# 		if resp[0] == 'y':
	# 			break
	# 		else:
	# 			resp = input('Please say yes or no: ').lower()

	# for i in f:
	# 	fruits.remove(i)

	# print(fruits)

	#Series 4
	frutki = fruits[:]
	for i in range(len(frutki)):
		frutki[i] = frutki[i][::-1]

	fruits.pop()
	print(fruits)
	print(frutki)


main()