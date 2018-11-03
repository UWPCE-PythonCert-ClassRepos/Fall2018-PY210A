
#fizzbuzz exercise
#this creates a function that prints up to the first variable
#and prints 'fizz' if divisible by the second variable
#and 'buzz' if divisible by the third variable
#print 'fizzbuzz' if divisible by both
def fizzbuzz(num, div1,div2):
    for i in range(1,num+1):
        if (i % div1 == 0) and (i % div2 == 0):
            print('fizzbuzz')
        elif (i % div1 == 0):
            print("fizz")
        elif (i % div2 == 0):
            print("buzz")
        else:
            print(i)

#for testing
if __name__=="__main__":
    fizzbuzz(100,2,5)
