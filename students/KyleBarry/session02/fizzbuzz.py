def fizz_buzz():
    """Print Fizz for numbers that are divisible by 3,
    Buzz for numbers divisible by 5, and FizzBuzz for
    numbers divisible by both (from 1 to 100)"""
    for i in range(1,101):
        if i % 5 == 0 and i % 3 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizz_buzz()