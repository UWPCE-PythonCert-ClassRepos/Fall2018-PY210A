# Function definaton
def printme(string):
    print(string)
    return

# 1. NameError
printme(c)

# Traceback (most recent call last):
#  File "<pyshell#28>", line 1, in <module>
#    printme(c)
# NameError: name 'c' is not defined


# 2. TypeError
printme()

# Traceback (most recent call last):
#  File "<pyshell#13>", line 1, in <module>
#    printme()
# TypeError: printme() missing 1 required positional argument: 'str'


# 3. SyntaxError
printme "c"

# SyntaxError: invalid syntax


# 4. AttributeError
printme('a'.spli())

# Traceback (most recent call last):
#  File "<pyshell#94>", line 1, in <module>
#    printme('a'.splt())
# AttributeError: 'str' object has no attribute 'splt