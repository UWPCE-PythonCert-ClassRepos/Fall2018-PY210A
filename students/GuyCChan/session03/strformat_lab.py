# Task One. Write a format string that takes the four element tuple.

print("file_{:03d} : {:>9.2f}, {:9.2e}, {:9.3e}".format( 2, 123.4567, 10000, 12345.67))


# Task Two. Use an alternate type of format string.

f"(file_{2:03d} : {123.4567:>9.2f}, {10000:9.2e}, {12345.67:9.3e})"


# Task Three. Dynamically Build up format strings.

def formatter(in_tuple):
    t = (1,2,3,4,5)
    fstring = "The {} numbers are: {{}}".format(len(t), ({},)*len(t))
    print(fstring.format(t))


# Task Four. Use string formating to print: '02 27 2017 04 30'
b = ( 4, 30, 2017, 2, 27)
print(b[3], b[4], b[2], b[0], b[1])

# Use f-string
f"{b[3]:02d}, {b[4]}, {b[2]}, {b[0]}, {b[1]}"


# Task Five. Write an f-string that will display:
#The weight of an orange is 1.3 and the weight of a lemon is 1.1

fruits = ["oranges", 1.3, "lemons", 1.1]
f"The weight of {fruits[0]} is {fruits[1]} and that of {fruits[2]} is {fruits[3]}."

#Now see if you can change the f-string so that it displays the names of the fruit in
#upper case, and the weight 20% higher (that is 1.2 times higher).

f"The weight of {fruits[0].upper()} is {fruits[1]/fruits[3]:.1f} times that of {fruits[2].upper()}."


# Task Six. Print a table of several rows, each with a name, an age and a cost.

def prnt_tab():
    print("{:<30} | {:>5} | {:>15}".format("Name", "Age", "Cost"))
    print("{:<30} | {:>5} | {:>15.2f}".format("Abigail Ack", 32, 345.50))
    print("{:<30} | {:>5} | {:>15.2f}".format("Benjamin Bannister", 45, 1643.75))
    print("{:<30} | {:>5} | {:>15.2f}".format("Deborah Dibden", 64, 875.00))
    print("{:<30} | {:>5} | {:>15.2f}".format("Larry Lock", 47, 2450))
    print("{:<30} | {:>5} | {:>15.2f}".format("Yoshiko Yamaguchi", 28, 98))

prnt_tab()

# Print the tuple in columns that are 5 charaters wide.
the tuple = (90, 91, 92, 93, 94, 95, 96, 97, 98, 99)
print(("{:>5}"*len(the tuple)).format(*the tuple))