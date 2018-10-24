def fizzbuzz(n=100):
    for x in range(n):
        num = x + 1
        str = ""
        if not num % 3:
            str = str + "Fizz"
        if not num % 5:
            str = str + "Buzz"
        if str == "":
            str = num
        print(str)
