

def fibonacci(n):
	#first create our list with starting integers
	fiblist = [0,1]
	#appends to the end list of integers the sum of the previous two integers
	#this will loop until the length of the list is n long
	#finally we return the n value of the list
	while len(fiblist) < n:
		fiblist.append(sum(fiblist[-2:]))
	return fiblist[n-1]

print(fibonacci(7))
print(fibonacci(9))
print(fibonacci(5))

def lucas(n):
	#first create our list with starting integers
	lucaslist = [2,1]
	#appends to the end list of integers the sum of the previous two integers
	#this will loop until the length of the list is n long
	#finally we return the n value of the list
	while len(lucaslist) < n:
		lucaslist.append(sum(lucaslist[-2:]))
	return lucaslist[n-1]

print(lucas(7))
print(lucas(9))
print(lucas(5))

def sum_series(n, x=0, y=1):
	#first create our list with starting integers
	sum_list = [x , y]
	#appends to the end list of integers the sum of the previous two integers
	#this will loop until the length of the list is n long
	#finally we return the n value of the list
	while len(sum_list) < n:
		sum_list.append(sum(sum_list[-2:]))
	return sum_list[n-1]

print(sum_series(7))
print(sum_series(9,2,1))
print(sum_series(5,6,4))

#here we write our unit tests. 
#no Assertion Errors mean the code is working as expected
assert fibonacci(7) == 8
assert lucas(7) == 18
assert sum_series(5,6,4) == 24