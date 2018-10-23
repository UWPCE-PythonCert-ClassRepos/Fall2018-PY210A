'''Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.'''


start_num = 0
end_num = 100

while start_num < 1 and end_num < 101:
    start_num += 1
    if (start_num % 3 == 0 and start_num % 5 == 0):
        print ("FizzBuzz")
    elif(start_num % 3 == 0):
        print("Fizz")
    elif (start_num % 5 == 0):
        print("Buzz")
    else:
        print(start_num)
