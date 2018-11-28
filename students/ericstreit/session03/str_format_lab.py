#Lesson##
#XXXXX Exercise ##
#
#!/usr/bin/env python3
#define variables

#Task 1
mytup = ( 2, 123.4567, 10000, 12345.67)
print("file{:03} : {:.2f} {:.2e} {:.2e}".format(mytup[0], mytup[1], mytup[2], mytup[3]))

#Task 2
#same as 1 but use an alternative tpe of format string
print(f'file{mytup[0]:03} : {mytup[1]:.2f} {mytup[2]:.2e} {mytup[3]:.2e}')


#Task 3 formatter function
mytup = (1,2,3,4,5)
#define formatter function
#does not work properly!
#swaps the first and last tuples????
#I practically copied this from your video
#It looks like the value of 'l' is not being placed at the first {}
def formatter(n):
    """string exercise task 3"""
    l = len(n)
    print("the {} numbers are: " + ",".join(["{}"] * l).format(l, *n))

#task 4
mytup = (4, 30, 2017, 2, 27)
print("{:02} {} {} {:02} {}".format(mytup[3],mytup[4],mytup[2],mytup[0],mytup[1]))


#task 5
mylist = ['orange', 1.3, 'lemon', 1.1]
print(f'The weight of an {mylist[0]} is {mylist[1]} and the weight of a {mylist[2]} is {mylist[3]}')
#change f-string to display in uppercase and weight 1.2 higher
print(f'The weight of an {mylist[0].upper()} is {mylist[1] * 1.2} and the weight of a {mylist[2].upper()} is {mylist[3] * 1.2}')


#task 6
print('{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09'))


#task 6 - print three colums with alignment specifiers
list1 = ["Ann Fang", 35, 10123], ["Katherine Valentine", 27, 218000], ["Hester Shaw", 25, 1], ["Tom Natsworthy", 22, 503], ["Grikes", 107, 1098]
print()
print("{:30} {:10} {}".format("Name", "Age", "Cost"))
print("{:-<60}".format("--"))
for i in range(len(list1)):
    print(f'{list1[i][0]:30} {list1[i][1]:<10} ${list1[i][2]:<}')
print()


#task 6 extra
mytup=(1,2,3,4,5,6,7,8,9,0)
print("".join(["  |   {}  "] * 10).format(*mytup), end=" |\n")

#for testing
if __name__=="__main__":
    pass
    mytup = (1,2,3,4,5,6,7,8)
    print("my formatter is not working correctly")
    formatter(mytup)
