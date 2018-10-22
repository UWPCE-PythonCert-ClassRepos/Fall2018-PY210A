# Fibonacci Series Exercise.

def fibonacci(n):
    x = [0]
    if n == 0:
        return 1
    elif n == 1:
        x = [0,1]
        return 1
    else :
#        for i in range(n):
        return fibonacci(n-2) + fibonacci(n-1)
        # x = {0,1,i}
        # print(x)



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
