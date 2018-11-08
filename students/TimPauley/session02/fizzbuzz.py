#Tim Pauley
#Assignment 02
#Date due: 10/23/2018


def fizzbuzz(f):
	for i in range(1, 101):
    		options_to_print = [i, 'Fizz', 'Buzz', 'FizzBuzz']
    		index = 0  # index is zero
    		index += (i % 3 == 0)  # multiple of 3
    		index += (2 * (i % 5 == 0))  # multiple of 5
    		print(options_to_print[index])  # print the selection.

fizzbuzz(1)

