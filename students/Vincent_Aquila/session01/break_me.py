"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
assignment objective: break_me.py assignment to test gitHub functionality and
learn the four common exceptions:
- NameError
- TypeError
- SyntaxError
- AttributeError
"""

#instructions - uncomment each script of code individually and run

#NameError
#imput("What is your name?") #change imput to input to correct error
"""
imput (instead of input) generates the following error message:
Traceback (most recent call last):
  File "break_me.py", line 13, in <module>
    imput("What is your name?")
NameError: name 'imput' is not defined
"""

#TypeError
#cat_inventory = "cat" + 1 #add quotes around 1 to make it a string; can't add strings and intergers
#print(cat_inventory)
"""
1 with no quotes generates the following error message:
Traceback (most recent call last):
      cat_inventory = "cat" + 1
TypeError: can only concatenate str (not "int") to str
"""

#SyntaxError
#print("I have three cats) #add a closing quote after cats to correct
"""
the missing closing quote generates the following error;
File "break_me.py", line 33
    print("I have three cats)
                            ^
SyntaxError: EOL while scanning string literal
"""

#AttributeError
greeting = "Hello, my name is {}".fmt("Vince") #change fmt to format to correct
print(greeting)
"""
.fmt is spelled incorrectly; it should be the command called format
.format("Vince") is an attribute of the ...my name is {}; if format is mispelled
it throws and attribute error - such as:

File "break_me.py", line 45, in <module>
    greeting = "Hello, my name is {}".fmt("Vince")
AttributeError: 'str' object has no attribute 'fmt'
"""
