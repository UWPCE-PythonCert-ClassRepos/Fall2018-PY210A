# Goal:
# Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Option 1
# Here, I tried to eliminate, change hard coded number with name 'n', to fit for any number 'n', but it needs to be multiple of 5.

def print_rectangle(n) :
    for i in range(n+1) :
        for j in range(n+1):
            if ((i in range (0,n+5,5) and j%5 == 0)) :
                print("+", end=" ")            
            elif ((i in range(0,n+5,5) and j > 0 and j < n)) :
                print("-", end=" ")            
            elif ((j in range(0,n+5,5) and i > 0 and i < n)) :
                print("|", end="     ")           
            else :
                print("", end=" ")
        print()
n = 25
print_rectangle(n)

# Option 2

# def print_rectangle(row, col) :
#     for i in range(11) :
#         for j in range(11):
#             if ((i in range (0,15,5) and j%5 == 0)) :
#                 print("+", end=" ")            
#             elif ((i in range(0,15,5) and j > 0 and j < 10)) :
#                 print("-", end=" ")            
#             elif ((j in range(0,15,5) and i > 0 and i < 10)) :
#                 print("|", end="     ")           
#             else :
#                 print("", end=" ")
#         print()
# Driver program for above function
# row = 10
# col = 10
# print_rectangle(row, col)

# Option 3
# def print_rectangle(row, col) :
#     for i in range(11) :
#         for j in range(11):
#             if ((i == 0 and j%5 == 0) or (i == 5 and j%5 == 0) or i == 10 and j%5 == 0) :
#                 print("+", end=" ")           
#             elif ((i == 0 and j > 0 and j < 10) or (i == 5 and j > 0 and j < 10) or (i == 10 and j > 0 and j < 10)) :
#                 print("-", end=" ")
#             elif ((j == 0 and i > 0 and i < 10) or (j == 5 and i > 0 and i < 10) or (j == 10 and i > 0 and i < 10)) :
#                 print("|", end="     ")        
#             else :
#                 print("", end=" ")
#         print()

# # Driver program for above function
# row = 10
# col = 10
# print_rectangle(row, col)

