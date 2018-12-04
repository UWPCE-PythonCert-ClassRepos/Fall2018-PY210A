#! python3

for i in range (1,101):
    
    if ((i%3 == 0) & (i%5 != 0)):
        i = 'Fizz'
    
    elif ((i%5 == 0) & (i%3 !=0)):
        i = 'Buzz'
        
    elif ((i%3 == 0) & (i%5 ==0)):
        i = 'FizzBuzz'
    print (i)
