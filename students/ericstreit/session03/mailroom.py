#Lesson03
#Mailroom Part 1 Project
#
#!/usr/bin/env python3

#define variables - the donor list
donor1 = ["Anna Fang", 23, 5000]
donor2 = ["Tom Natsworthy", 99, 783, 3]
donor3 = ["Hester Shaw", 5, 92, 101]
donor4 = ["Katherine Valentine", 1000, 2000, 3000]
donor5 = ["Grike", 1]
donors = [donor1] + [donor2] + [donor3] + [donor4] + [donor5]
l = len(donors)
print(donors)
print(l)
#define function
def myfunc(n):
    """Update the DocString"""
    pass
# input
choice = int(input("(1) Send a Thank You (2) Create a Report or (3) Quit - (1,2,or 3) : "))
if choice == "1":
    name = input("Please enter the full name (or 'list' to list current names): ")
    for i in range(5):
        




#for testing
if __name__=="__main__":
    pass
