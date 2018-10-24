def FizzBuzz():
	i=1
	m=100
	while i<m+1:
		if i%3==0:
			print ("Fizz",end="")
			if i%5==0:
				print("Buzz",end="")
		elif i%5==0:
			print ("Buzz",end="")
		else:	
			print (i,end="")
		print()	
		i+=1
	pass

FizzBuzz()