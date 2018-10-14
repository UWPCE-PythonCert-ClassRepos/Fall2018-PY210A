import random

for i in range(1,10):

    test_num = random.randint(1,100)
#    print("This is the num:  ",test_num)
#    nother comment


    if (test_num % 3 == 0) and (test_num % 5 == 0):
        print("\tBING: we have a fizzbuzz ->", test_num)
    elif test_num % 3 == 0:
        print("\tBING: we have a fizzz ->", test_num)
    elif test_num % 5 == 0:
        print("\tBING: we have a buzzz ->", test_num)
    else:
        print("Just another number that isn't fizzbuzz worthy",test_num)
