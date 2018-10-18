def fibonacci(n):
    """Return the nth value (the index of the list) in fibonacci sequence.
    fib[n-1] to return the value in the n position"""
    a = 0
    b = 1

    fib = [a, b]
    for i in range(n):
        a,b = b, a+b
        fib.append(b)
    print(fib[n])

fibonacci(10)