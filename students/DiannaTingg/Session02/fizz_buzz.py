# Lesson 02 Exercise: Fizz Buzz


def fizzbuzz():
    # Use numbers from 1 to 100 inclusive
    for x in range (1, 101):
        # Check if multiple of 3 and 5 - print "FizzBuzz"
        if x % 15 == 0:
            print ("FizzBuzz")
        # Check if multiple of 3 - print "Fizz"
        elif x % 3 == 0:
            print ("Fizz")
        # Check if multiple of 5 - print "Buzz"
        elif x % 5 == 0:
            print ("Buzz")
        # Otherwise print the number
        else:
            print (x)

# Test
fizzbuzz()
