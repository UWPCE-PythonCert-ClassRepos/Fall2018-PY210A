# series 1. I do not have all the codes here to account for user input error
def fruit_basket():

	fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
	print(fruit_list)
	response1 = input("What fruit would you like to add to the list? ")
	response1 = response1.capitalize()
	fruit_list.append(response1)
	print("You added {} and the fruits in the list are: {} ".format(response1, fruit_list))
	response2 = int(input("What fruit would you like? Please choose from 1 to 5. "))
	if response2 < 0 or response2 > 6:
		print("You are out of range.")
	else:
		response3 = response2 - 1
	print("You like number {} and the fruit is {}.".format(response2, fruit_list[response3]))
	# Add Grapes and then Watermelons to the list
	fruit_list = ["Grapes"] + fruit_list
	print("We added 'Grapes'. The list contains: {}.".format(fruit_list))
	fruit_list.insert(0, "Watermelons")
	print("We just added 'Watermelons' and now we have {}.".format(fruit_list))
	for fruit in (fruit_list):
		if "P" in(fruit):
			print("The word {} starts with 'P'.".format(fruit))
		else:
			pass

# series 2. Remove items from the list
	fruit_list1 = fruit_list
	# Remove the last item on the list
	fruit_list1.pop(-1)
	print("We took out the last item and now have:{}".format(fruit_list1))
	# Get input to delete items on the list
	response4 = input("Which fruit would you like to delete from the list? ")
	response4 = response4.capitalize()
	while response4 not in fruit_list1:
		print("Please enter a fruit on the list.")
		break
	else:
		fruit_list1.remove(response4)
		print("We have 2 lots of each fruit and they are:{}".format(fruit_list1*2))

# series 3. Remove more or keep fruit items on the list
	fru_list2 = fruit_list1*2
	for fruit in fru_list2[:]:
		response5 = input("Do you like {}? Please answer Yes or No? ".format(fruit))
		if response5.lower() == "n":
				fru_list2.remove(fruit)
		elif response5.lower() == "y":
			pass
		else:
			print("That is not a valid answer. Please answer yes or no.")
	print("These fruits are left in the basket: {}.".format(fru_list2))

# Series 4. Make a copy of the list and reverse the letters in each fruit in the copy.
# Delete the last item of the original list. Display the original list and the copy.
	fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
	fru_list3 = fruit_list[:]
	print("A copy of the original list is:{}".format(fru_list3))
	for i, fruit in enumerate(fru_list3):
		fru_list3[i] = fruit[::-1]
	print("The list with each letter in the item reversed looks like:{}".format(fru_list3))
	fruit_list.pop(-1)
	print("With the last item deleted, the original list looks like this:{}".format(fruit_list))


if __name__ == "__main__":
	fruit_basket()