def fibonacci(n):
    a = 0
    b = 1

    fib = [a, b]
    for i in range(n):
        a,b = b, a+b
        fib.append(b)
    print(fib[n])

fibonacci(10)