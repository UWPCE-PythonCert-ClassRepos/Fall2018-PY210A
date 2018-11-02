# PY210A - session02
# Cheng Liu
# A function that:
# (1) prints "Fizz" for multiples of 3
# (2) prints "Buzz" for multiples of 5
# (3) prints "FizzBuzz" for multiples of both 3 and 5
# (4) prints the number for the rest


def fizz_buzz(n):
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


fizz_buzz(100)
