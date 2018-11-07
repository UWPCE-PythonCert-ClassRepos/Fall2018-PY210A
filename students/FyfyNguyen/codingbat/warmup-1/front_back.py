# Given a string, return a new string where the first and last chars have been exchanged.

# Returns "string index out of range" when run in codingbat
# Returns correct values when run in ipython
def front_back(str):
    front = str[0]
    back = str[-1]
    mid = str[1:-1]
    return back + mid + front

# # CodingBat solution
# def front_back(str):
#   if len(str) <= 1:
#     return str
  
#   mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
#   # last + mid + first
#   return str[len(str)-1] + mid + str[0]