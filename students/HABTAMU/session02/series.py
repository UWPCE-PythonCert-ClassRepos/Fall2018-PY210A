# Fibonacci Series Exercise.

def fibonacci(n):
    """ compute the nth Fibonacci number """
    a, b = 0, 1

    if n <= 0:
        return 1
    else:
        for i in range(n):
            print(a, end=" ")

            c = a + b
            a = b
            b = c

def lucas(n):
    """ compute the nth Lucas number """
    a, b = 2, 1

    if n <= 0:
        return 1
    else:
        for i in range(n):
            print(a, end=" ")

            c = a + b
            a = b
            b = c
