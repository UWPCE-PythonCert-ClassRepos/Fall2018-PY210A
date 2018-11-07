def fizz_buzz(high_num = 100):
    lst = list(range(1, high_num + 1))
    fizz = list(range(3,101,3))
    buzz = list(range(5,101,5))

    for f in fizz:
        lst[f-1] = 'Fizz'
    for b in buzz:
        if isinstance(lst[b-1], str):
            lst[b-1] = lst[b-1] + 'Buzz'
        else:
            lst[b-1] = 'Buzz'
    for each in lst:
        print(each)
fizz_buzz()
