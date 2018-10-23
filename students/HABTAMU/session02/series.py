# Fibonacci Series Exercise.

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

# I rerun 
# In [362]: run fibonacci_series.py

# In [363]: fibonacci(6)
0 1 1 2 3 5

# In [364]: fibonacci(9)
0 1 1 2 3 5 8 13 21



# def fibonacci(n):
#    x = [0]
#    if n == 0:
#        return 1
#    elif n == 1:
#        x = [0,1]
#        return 1
#    else :
#        for i in range(n):
#        return fibonacci(n-2) + fibonacci(n-1)
#        # x = {0,1,i}
#        # print(x)



# def fibonacci(n):
#     x = { 0 }
#     if n == 0:
#         return 1
#     elif n == 1:
#         x = {0,1}
#         return 1
#     else :
# #        for i in range(n):
#         n = fibonacci(n-2) + fibonacci(n-1)
#         x.append('n')
#         return x
#         # x = {0,1,i}
#         # print(x)
