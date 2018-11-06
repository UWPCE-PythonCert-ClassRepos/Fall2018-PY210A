for num in range(1,101):
	if num % 3 == 0 and num % 5 == 0:
		print('FizzBuzz')
	elif num % 3 == 0:
		print('Fizz')
	elif num % 5 == 0:
		print('Buzz')
	else:
		print(num)





def fizzbuzz2(n):
	for i in range(1, n + 1):
		if i % 15 == 0:
			print("FizzBuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)




def fizzbuzz3(n):
	for i in range(1, n + 1):
		msg = ""
		if not(i % 3):
			msg += "Fizz"
		if not(i % 5):
			msg += "Buzz"

		if msg:
			print(msg)
		else:
			print(i)


			# the if not(i% 3) is a double negative