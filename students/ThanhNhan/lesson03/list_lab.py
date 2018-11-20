#!/usr/bin/env python3

#Series 1
fruit =['Apples', 'Pears', 'Oranges', 'Peaches']
print (fruit) #display a list of fruit
response = input("Add another fruit > ")
print (response) #display food to add
fruit.append(response)
print(list(enumerate(fruit, start=1)))
#print (fruit)
num_disp = input("Enter Number and fruit display back to user >")
print (fruit[int(num_disp) - 1])
add_a_fd = input("Add another fruit from the beginning using >") 
fruit= [add_a_fd] +  fruit #add fruit using +
print (fruit)
add_a_finsert = input("Add another fruit from the beginning using >") 
fruit.insert(0, add_a_finsert) #add fruit using insert
print (fruit)
print ("Display all the fruit that begin with P:")
for i in range(len(fruit)):
	if(fruit[i][0] == "P"):
	    print (fruit[i]) #print element start with P

#Series 2
print (fruit)
fruit.pop() #remove last fruit from the list
print ("remove last fruit from the list")
print (fruit)
ask_fruit_rm = input("Enter name of the fruit from the list that you want delete? >")
fruit.remove(ask_fruit_rm)
print ("{} Fruit delete from list".format(ask_fruit_rm))
print (fruit)
#bonus will be determine later

#Series 3

i = 0
while True:
	print(i)
	if len(fruit) == 0:
		print("Sorry fruit out from the list")
		break

	ask_fv = input("Do you like {}? (yes/no) >".format(fruit[0]))

	for x in range (len(fruit)):
		fruit[x] = fruit[x].lower()
	print(fruit)
	
	if (ask_fv == "no" and len(fruit) > 0):
		fruit.remove(fruit[0])  
		print(fruit)

	if (ask_fv == "yes"):
		break
	i += 1

#Series 4
fruit =['Apples', 'Pears', 'Oranges', 'Peaches']
copy_fruit = fruit[:] #copy a list
print (copy_fruit)

fruit.pop()
print("delete last item of the list using pop method")
print(fruit)
print("copy of the list original")
print(copy_fruit)
    
	# for x in range(len(fruit)):
	# 	fruit[x] = fruit[x].lower()

    # if (ask_fv == "no"):
    # 	fruit.pop(i)


