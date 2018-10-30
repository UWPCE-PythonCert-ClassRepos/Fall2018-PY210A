"""In a list of 1-100, if num is divisible by three, print 'Fizz', if num is divisible by 5, 
rint 'Buzz', and if the num can be divided by 3 and 5, print 'FizzBuzz'"""

def fizz_buzz():
    for num in range(1,101):
        num_range = ''
        if num % 3 == 0:
            num_range = "Fizz"
        if num % 5 == 0:
            num_range += 'Buzz'
        if len(num_range) == 0:
            num_range = num
        print(num_range)

