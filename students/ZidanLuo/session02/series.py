import sys


def fibonacci(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(sys.argv[1])))