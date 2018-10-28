def fizz_buzz():
    """Print Fizz for numbers that are divisible by 3,
    Buzz for numbers divisible by 5, and FizzBuzz for
    numbers divisible by both (from 1 to 100)"""
    for i in range(1,101):
        if i % 5 == 0:
            if i % 3 == 0:
                print('FizzBuzz')
            else:
                print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)

fizz_buzz()