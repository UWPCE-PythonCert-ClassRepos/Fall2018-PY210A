#!/usr/bin/env python3
def fibonacci(n):
    a, b = 0, 1

    if n <= 0:
        return 1
    else:
        for i in range(n):
            print(a, end=" ")

            c = a + b
            a = b
            b = c
fibonacci(10)
